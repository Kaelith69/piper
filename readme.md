<p align="center">
  <img src="banner.svg" alt="Piper — YouTube Downloader" width="800"/>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#use-cases">Use Cases</a> •
  <a href="#specs--architecture">Specs</a> •
  <a href="#troubleshooting">Troubleshooting</a> •
  <a href="#license">License</a>
</p>

---

**Piper** is a lightweight, futuristic desktop GUI for downloading YouTube videos and audio.  
Built on top of [yt-dlp](https://github.com/yt-dlp/yt-dlp) and Python's `tkinter`, it gives you a clean neon-themed interface without any command-line knowledge required.

---

## Features

| Feature | Detail |
|---------|--------|
| 🎬 Video download | Up to 1080p, merged into MP4 |
| 🎵 Audio extraction | Best-quality audio, saved as 192 kbps MP3 |
| 📊 Live progress | Progress bar + scrolling log with percentage |
| 📁 Configurable save path | Browse button to pick any folder at runtime |
| 🎨 Futuristic dark UI | Neon cyan/purple theme, no extra theme packages needed |
| 🔒 Thread-safe design | All Tkinter updates happen on the main thread via a queue |
| 📦 Single-file app | One Python file, easy to read and modify |

---

## Requirements

| Requirement | Version / Notes |
|-------------|----------------|
| Python | 3.7 or later |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Latest recommended |
| tkinter | Bundled with Python on Windows and most Linux distros |
| [ffmpeg](https://ffmpeg.org/) | Required for audio extraction and MP4 merging |

---

## Installation

### 1 — Clone the repository

```bash
git clone https://github.com/Kaelith69/piper.git
cd piper
```

### 2 — Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3 — Install ffmpeg

| Platform | Command |
|----------|---------|
| **Windows** | Download from [ffmpeg.org](https://ffmpeg.org/download.html), extract, add the `bin/` folder to `PATH` |
| **macOS** | `brew install ffmpeg` |
| **Ubuntu/Debian** | `sudo apt install ffmpeg` |
| **Fedora** | `sudo dnf install ffmpeg` |

### 4 — Run

```bash
python piper.py
```

---

## Usage

1. **Paste** a full YouTube URL into the input field (e.g. `https://www.youtube.com/watch?v=dQw4w9WgXcQ`).  
2. **Choose** a download type:
   - **Video (1080p)** — downloads video + audio streams and merges them into an MP4 file.
   - **Audio (High Quality MP3)** — extracts the best audio stream and converts it to 192 kbps MP3.
3. *(Optional)* Click **Browse…** to change the save folder.  
4. Click **Download**.  
5. Watch the progress bar and log. The button re-enables when the download is complete.

---

## Use Cases

- **Offline viewing** — save lectures, tutorials, or travel content to watch without internet.  
- **Music archiving** — extract audio from music videos, live sessions, or podcasts.  
- **Content creation** — grab reference footage or royalty-free background music.  
- **Research / accessibility** — local copies for students or users with limited bandwidth.

---

## Specs & Architecture

```
piper.py
└── main()                    # All GUI setup inside a function — safe to import
    ├── UI setup (tkinter)    # Window, styles, widgets
    ├── browse_dir()          # Opens directory picker, updates download_dir_var
    ├── download()            # Validates input (main thread), spawns worker thread
    ├── download_thread()     # yt-dlp download + progress_hook (background thread)
    │   └── progress_hook()   # Puts (type, data) tuples onto status_queue
    └── check_queue()         # Drains queue every 100 ms, updates GUI (main thread)
```

### Thread-safety model

Tkinter is **not thread-safe**. All widget reads (`url_entry.get()`, `type_var.get()`) are performed in `download()` on the **main thread** before the worker thread starts. All GUI writes from the worker are forwarded through a `queue.Queue` and applied by `check_queue()` running on the main thread via `root.after()`.

### Output file naming

| Mode | Template |
|------|----------|
| Video | `<Title>-<VideoID>-video.mp4` |
| Audio | `<Title>-<VideoID>-audio.mp3` |

### yt-dlp format strings

| Mode | Format string |
|------|--------------|
| Video | `bestvideo[height<=1080]+bestaudio/bestvideo+bestaudio/best` |
| Audio | `bestaudio/best` → post-processed to MP3 192 kbps |

---

## Packaging as a Standalone Executable (Windows)

```powershell
pip install pyinstaller
pyinstaller --onefile --noconsole piper.py
```

The executable is placed in `dist/piper.exe`.  
> **Note:** Users still need ffmpeg in their PATH for audio downloads and MP4 merging.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: yt_dlp` | Run `pip install -r requirements.txt` |
| `ffmpeg not found` | Install ffmpeg and add it to `PATH` (see [Installation](#3--install-ffmpeg)) |
| Progress stuck at 0% | Some streams don't report `total_bytes`; the bar will jump to 100% on finish |
| Window too small / clipped | Resize the window or increase `geometry` in `piper.py` |
| Permission denied on save | Choose a different folder with the **Browse…** button |
| GUI does not open | Confirm Python ≥ 3.7 and that `tkinter` is installed (`python -m tkinter`) |

---

## License

This project is released for educational and personal use.

