# Installation 📦

> _"Software installation should not be a rite of passage. Let's keep it simple."_

---

## Requirements

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.7+ | Comes with `tkinter` on Windows and most Linux distros |
| yt-dlp | Latest | The actual downloader — fetches from PyPI |
| ffmpeg | Any recent | External binary — required for merging video/audio and MP3 conversion |

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/Kaelith69/piper.git
cd piper
```

Or download the ZIP from GitHub and extract it — same result.

---

## Step 2 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs `yt-dlp`. That's the only pip dependency. One line file, one package.

> **Using a virtual environment?** Good. Do it.
>
> ```bash
> python -m venv venv
> source venv/bin/activate   # Linux/macOS
> venv\Scripts\activate      # Windows
> pip install -r requirements.txt
> ```

---

## Step 3 — Install ffmpeg

ffmpeg is not a Python package — it's a standalone binary that yt-dlp calls for post-processing. You need it for:

- Merging separate video + audio streams into `.mp4`
- Converting audio to `.mp3`

Without ffmpeg, video downloads will fail the merge step and audio downloads won't produce MP3.

### Windows

1. Download a build from [ffmpeg.org/download.html](https://ffmpeg.org/download.html) (Gyan.dev or BtbN builds are reliable)
2. Extract the archive
3. Add the `bin/` folder to your system `PATH`
4. Verify: open a new terminal and run `ffmpeg -version`

Alternatively, if you have [Scoop](https://scoop.sh/) or [Chocolatey](https://chocolatey.org/):

```powershell
scoop install ffmpeg
# or
choco install ffmpeg
```

### macOS

```bash
brew install ffmpeg
```

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install ffmpeg
```

### Fedora

```bash
sudo dnf install ffmpeg
```

### Arch Linux

```bash
sudo pacman -S ffmpeg
```

---

## Step 4 — Verify Your Setup

```bash
python --version      # Should be 3.7+
python -c "import yt_dlp; print(yt_dlp.version.__version__)"  # Should print a version
ffmpeg -version       # Should print ffmpeg version info
python -m tkinter     # Should open a small test window
```

If all four work, you're good.

---

## Step 5 — Run Piper

```bash
python piper.py
```

The window should open immediately.

---

## Optional: Package as Standalone Executable (Windows)

If you want a distributable `.exe` that doesn't require Python to be installed:

```powershell
pip install pyinstaller
pyinstaller --onefile --noconsole piper.py
```

The executable lands in `dist/piper.exe`.

**Caveats:**
- The exe is ~15–30 MB depending on yt-dlp's size
- Recipients still need ffmpeg in their PATH (ffmpeg cannot be bundled inside the exe cleanly)
- The `--noconsole` flag suppresses the terminal window; remove it if you want to see debug output

---

## Troubleshooting Installation

| Problem | Fix |
|---------|-----|
| `ModuleNotFoundError: yt_dlp` | Run `pip install -r requirements.txt` |
| `python -m tkinter` shows nothing | On Linux, install: `sudo apt install python3-tk` |
| `ffmpeg: command not found` | Install ffmpeg and add it to PATH (see Step 3) |
| `python: command not found` | Make sure Python 3 is installed and in PATH; try `python3` |

See [Troubleshooting](Troubleshooting.md) for more.
