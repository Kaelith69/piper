# Troubleshooting 🔧

> _"Something broke. Let's fix it. Probably ffmpeg."_

---

## Quick Diagnosis

Before diving into specific issues, run these checks:

```bash
python --version              # 3.7+?
python -c "import yt_dlp; print('yt-dlp OK')"
python -m tkinter             # Opens a test window?
ffmpeg -version               # Prints ffmpeg info?
```

If any of these fail, that's your first fix.

---

## Common Issues

### ❌ `ModuleNotFoundError: No module named 'yt_dlp'`

yt-dlp is not installed.

```bash
pip install -r requirements.txt
```

If you're using a virtual environment, make sure it's activated before running Piper.

---

### ❌ `ffmpeg not found` / `FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'`

ffmpeg is either not installed or not in your `PATH`.

**Verify:**
```bash
ffmpeg -version
```

**Fix:**
- Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html), add `bin/` to PATH, restart your terminal
- macOS: `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt install ffmpeg`
- Fedora: `sudo dnf install ffmpeg`

After installing, open a **new** terminal (PATH changes don't apply to open terminals).

---

### ❌ Progress bar stuck at 0%

Some video streams don't report `total_bytes` upfront. When this happens:

- The bar stays at 0% during the download
- It jumps to 100% when the download finishes
- The log will still show progress text

This is expected behavior, not a bug. The download is actually proceeding.

---

### ❌ Download appears to finish but no file appears

Possible causes:

1. **Post-processing failed** — ffmpeg not installed or not in PATH. Check the log for error messages.
2. **Wrong folder** — check which folder is shown in the save path label. The file might be in `~/Downloads` even if you thought you changed it.
3. **Permission error** — you don't have write access to the chosen folder. Try a different folder (e.g., Desktop or your home directory).

---

### ❌ `Permission denied` when saving

You don't have write permission to the save directory.

Click **Browse…** and choose a folder you own (Desktop, Documents, Downloads).

---

### ❌ Window is too small / widgets are clipped

Resize the window — the app is set to `480x520` and `resizable(False, False)` by default.

If you need a larger window, open `piper.py` and change:

```python
root.geometry("480x520")
root.resizable(False, False)
```

to a larger geometry, e.g.:

```python
root.geometry("600x650")
root.resizable(True, True)
```

---

### ❌ `_tkinter.TclError: ...` or GUI crashes

This usually means something tried to update a widget from the wrong thread. If you've modified `piper.py`, make sure all widget reads/writes happen on the main thread. See [Architecture](Architecture.md) for details.

If you haven't modified anything and this is happening, open an issue with the full traceback.

---

### ❌ GUI doesn't open at all

1. Confirm Python ≥ 3.7: `python --version`
2. Confirm tkinter is installed: `python -m tkinter` (should open a test window)
3. On Linux, tkinter may need to be installed separately:
   ```bash
   sudo apt install python3-tk    # Debian/Ubuntu
   sudo dnf install python3-tkinter  # Fedora
   ```

---

### ❌ Download fails with `ERROR: ...` in the log

Read the error message carefully. Common ones:

| Error message | Cause | Fix |
|--------------|-------|-----|
| `ERROR: Unsupported URL` | URL isn't a valid YouTube video | Check the URL |
| `ERROR: Video unavailable` | Private, age-restricted, or removed | Can't download unavailable videos |
| `HTTP Error 429: Too Many Requests` | YouTube rate-limiting | Wait a bit and try again |
| `[ffmpeg] ERROR: ...` | ffmpeg failed during post-processing | Check ffmpeg is installed and in PATH |

---

### ❌ Audio download gives a video file instead of MP3

ffmpeg is not installed or not accessible. Without it, yt-dlp downloads the audio stream but cannot convert it to MP3. Install ffmpeg (see [Installation](Installation.md)).

---

### ❌ yt-dlp fails with format errors (`Requested format is not available`)

YouTube occasionally changes available formats. Update yt-dlp:

```bash
pip install --upgrade yt-dlp
```

yt-dlp releases frequently specifically to handle these format changes.

---

## Still Stuck?

Open an issue on [GitHub](https://github.com/Kaelith69/piper/issues) and include:

- Your OS and Python version
- The full error message from the log
- The URL you were trying to download (or a similar one that reproduces the issue)
- Whether ffmpeg is installed and accessible
