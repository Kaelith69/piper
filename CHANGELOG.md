# Changelog

All notable changes to Piper are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

Stuff that's being worked on but hasn't shipped yet. Consider this the "chaotic WIP" section.

- Playlist download support (in design — turns out playlists are surprisingly complicated)
- Format/resolution selector dropdown
- Multi-URL download queue

---

## [1.1.0] — 2025-01-01

### Added
- **Thread-safety overhaul** — all widget reads now happen on the main thread before spawning the worker; all widget writes go through `queue.Queue` and are applied by `check_queue()` via `root.after(100, ...)`
- **Division-by-zero guard** in `progress_hook` — some streams don't report `total_bytes`, so we now fall back to `total_bytes_estimate` and guard against zero with `max(..., 1)`
- **`daemon=True`** on the download thread — so closing the window while downloading doesn't leave a zombie process lurking
- Scrolling log auto-scrolls to bottom on every update (`status_text.see(tk.END)`)
- `browse_dir()` saves the chosen directory into `download_dir_var` and it persists for the session

### Changed
- Progress bar resets to 0 when a new download starts
- Log clears on each new download instead of appending forever
- `download_button` disables during download and re-enables on completion (or error)

### Fixed
- GUI freeze during download (was running download on main thread — the classic mistake)
- Progress bar stuck at final value after download completion

---

## [1.0.0] — 2024-01-01

### Added
- 🎉 Initial release — it works!
- Neon dark GUI with cyan/purple theme (`#00FFF7` / `#A259FF`)
- YouTube video download (best quality up to 1080p, merged to `.mp4`)
- YouTube audio extraction (best quality, converted to 192 kbps `.mp3`)
- Live progress bar with percentage
- Scrolling status log
- Browse button for save directory
- Output file naming: `<Title>-<VideoID>-video.mp4` / `<Title>-<VideoID>-audio.mp3`
- `piper.spec` for PyInstaller packaging
- Orbitron font detection (uses it if installed, falls back to Segoe UI)

---

## Legend

- **Added** — new features
- **Changed** — changes to existing functionality
- **Deprecated** — soon-to-be removed features
- **Removed** — features removed in this release
- **Fixed** — bug fixes
- **Security** — vulnerability patches

---

_Dates marked `xx` are approximate — the author was not great at tagging releases. This is a judgment-free zone._
