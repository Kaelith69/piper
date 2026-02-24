# Architecture 🏗️

> _"It's not complicated. Two threads walk into a bar. Only one of them is allowed to touch the widgets."_

---

## Overview

Piper is a **single-file desktop application** with a deliberately simple architecture. The entire codebase lives in `piper.py` (~222 lines). There are no modules, no packages, no services — just one Python file doing its job.

The most interesting architectural decision is the thread model, which exists specifically because **tkinter is not thread-safe**.

---

## The Two-Thread Model

```
┌─────────────────────────────────┐       ┌──────────────────────────────────┐
│         MAIN THREAD             │       │        BACKGROUND THREAD          │
│                                 │       │                                  │
│  UI Setup (tkinter widgets)     │       │  download_thread(url, type, dir) │
│  browse_dir()                   │       │      └─ yt-dlp YoutubeDL         │
│  download()                     │──spawn─▶         └─ progress_hook()     │
│      └─ captures widget state   │       │               └─ puts tuples     │
│  check_queue() [every 100ms]   ◀──queue──┤                onto queue       │
│      └─ updates widgets         │       │  ffmpeg post-processing          │
│                                 │       │  → signal: enable_button         │
└─────────────────────────────────┘       └──────────────────────────────────┘
                         │
                  queue.Queue()
                  (thread-safe bridge)
```

### Why can't the background thread update widgets directly?

tkinter uses Tcl/Tk under the hood. Tcl's event loop is single-threaded. If two threads call widget methods simultaneously, you get undefined behavior ranging from "the UI glitches" to "the whole process crashes." Not great.

The solution: **the background thread never touches a widget**. Instead it posts messages to a `queue.Queue`. The main thread's `check_queue()` function runs every 100ms via `root.after()` and drains the queue, applying updates safely.

---

## Component Breakdown

### `main()`

All GUI setup lives inside a function (not at module level). This makes the file safe to `import` without immediately opening a window — useful for testing or future modularization.

### `browse_dir()`

Opens a native directory picker dialog. On selection, updates `download_dir_var` (a `tk.StringVar`). That's it. No side effects.

### `download()`

Runs on the **main thread**. Responsibilities:

1. Read the URL from `url_entry.get()` and validate it's not empty
2. Read `type_var.get()` and `download_dir_var.get()` (capturing widget state before the thread starts)
3. Disable the download button
4. Clear the log and progress bar
5. Spawn a daemon thread targeting `download_thread()`

This function is intentionally thin — all heavy lifting is in `download_thread()`.

### `download_thread(url, download_type, save_dir)`

Runs on the **background thread**. Receives all needed data as arguments (never accesses widgets). Builds the yt-dlp options dict and runs the download. On completion or error, posts `('enable_button', None)` to re-enable the button.

**Video options:**
```python
{
    'format': 'bestvideo[height<=1080]+bestaudio/bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'progress_hooks': [progress_hook],
    'outtmpl': '<dir>/%(title)s-%(id)s-video.%(ext)s',
}
```

**Audio options:**
```python
{
    'format': 'bestaudio/best',
    'progress_hooks': [progress_hook],
    'outtmpl': '<dir>/%(title)s-%(id)s-audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
```

### `progress_hook(d)`

Called by yt-dlp on progress events. Calculates percentage and posts `('text', ...)` and `('bar', pct)` tuples to `status_queue`. Guards against division by zero when `total_bytes` is unknown (some streams don't report it).

### `check_queue()`

Runs on the **main thread** every 100ms via `root.after(100, check_queue)`. Drains all pending messages from `status_queue` and applies them:

| Message type | Action |
|-------------|--------|
| `'text'` | Appends text to the log widget |
| `'bar'` | Updates the progress bar value |
| `'enable_button'` | Re-enables the download button, resets progress to 0 |

---

## Output File Naming

| Mode | Template | Example |
|------|----------|---------|
| Video | `%(title)s-%(id)s-video.mp4` | `Never Gonna Give You Up-dQw4w9WgXcQ-video.mp4` |
| Audio | `%(title)s-%(id)s-audio.mp3` | `Never Gonna Give You Up-dQw4w9WgXcQ-audio.mp3` |

The `%(id)s` suffix prevents filename collisions when downloading multiple videos with similar titles.

---

## Thread Safety Summary

| Operation | Thread | Safe? |
|-----------|--------|-------|
| Read widget value | Main only | ✅ |
| Write widget value | Main only | ✅ |
| Read widget value from background | ❌ Forbidden | 🚫 |
| Post to `status_queue` | Background | ✅ (Queue is thread-safe) |
| Drain `status_queue` | Main | ✅ |
| yt-dlp download | Background | ✅ |

---

## Why a Daemon Thread?

```python
thread = threading.Thread(..., daemon=True)
```

Daemon threads are killed when the main process exits. Without `daemon=True`, closing the Piper window while a download is in progress would leave the download thread running in the background as an orphan process. With it, close = close.
