# Piper Wiki — Home 🏠

> _Welcome to the Piper wiki. Think of it as the manual nobody reads until something breaks._

---

## What is Piper?

**Piper** is a desktop GUI application for downloading YouTube videos and audio. It wraps [yt-dlp](https://github.com/yt-dlp/yt-dlp) — the gold standard of YouTube downloaders — in a clean, neon-styled tkinter interface so you don't have to memorize CLI flags at midnight.

It downloads things. It puts them in a folder. It does not phone home, track you, show ads, or require an account. That's the whole pitch.

---

## Navigation

| Page | What's in it |
|------|-------------|
| [Architecture](Architecture.md) | Thread model, component breakdown, why the queue exists |
| [Installation](Installation.md) | How to get it running on your machine |
| [Usage](Usage.md) | How to actually use it once it's running |
| [Privacy](Privacy.md) | What data leaves your machine (spoiler: nothing) |
| [Troubleshooting](Troubleshooting.md) | When it breaks and how to fix it |
| [Roadmap](Roadmap.md) | What might come next, if motivation holds |

---

## Quick Start

```bash
git clone https://github.com/Kaelith69/piper.git
cd piper
pip install -r requirements.txt
# install ffmpeg (see Installation.md)
python piper.py
```

---

## Tech Stack at a Glance

| Layer | Technology |
|-------|-----------|
| GUI | Python `tkinter` + `ttk` |
| Download engine | `yt-dlp` |
| Audio/video processing | `ffmpeg` (external binary) |
| Threading | Python `threading` + `queue.Queue` |
| Packaging | `PyInstaller` (optional) |

---

## File Structure

```
piper/
├── piper.py            # The entire app (~222 lines)
├── requirements.txt    # yt-dlp
├── piper.spec          # PyInstaller config
├── assets/             # SVG diagrams, demo GIF
└── wiki/               # This documentation
```

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) in the repo root. PRs welcome, drama not.

---

## License

MIT. Full text in [LICENSE](../LICENSE).
