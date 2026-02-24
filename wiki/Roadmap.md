# Roadmap 🔭

> _"Features that will happen… when they happen. No promises, no sprints, no OKRs."_

---

## Current State (v1.1.x)

Piper does what it says on the tin:

- ✅ Single video download (up to 1080p MP4)
- ✅ Audio extraction (192 kbps MP3)
- ✅ Live progress bar + log
- ✅ Custom save folder
- ✅ Thread-safe GUI
- ✅ Single-file codebase

---

## Planned Features

### 🔜 Near Term (probably next)

| Feature | Description | Status |
|---------|-------------|--------|
| **Playlist support** | Detect playlist URLs and download all videos in sequence | Investigating |
| **Format / resolution selector** | Dropdown to pick 720p, 480p, etc. instead of always maxing out | Planned |
| **Download queue** | Queue multiple URLs and process them one after another | Planned |

### 📅 Medium Term (when motivation strikes)

| Feature | Description |
|---------|-------------|
| **Windows `.exe` release** | Packaged binary via GitHub Actions CI |
| **macOS `.app` bundle** | For people who don't want to install Python |
| **Subtitle download** | Optionally download `.srt` subtitles alongside video |
| **Thumbnail preview** | Show video thumbnail before downloading (fetched from yt-dlp metadata) |
| **Speed limiter** | Cap download speed via yt-dlp's `ratelimit` option |

### 🌌 Long Term (ambitious, possibly never)

| Feature | Description |
|---------|-------------|
| **Dark/light theme toggle** | Because apparently some people use light mode |
| **Download history** | Simple log of what you've downloaded and where |
| **Auto-update yt-dlp** | Detect and offer to update yt-dlp when a new version is available |
| **Chapters** | Split video by YouTube chapters into separate files |
| **Sponsorblock integration** | Skip sponsor segments via SponsorBlock + yt-dlp's built-in support |

---

## Non-Goals

Things that will *not* be added:

- **Browser extension** — that's a different project
- **Mobile app** — that's a very different project
- **Web interface** — you have the CLI for that
- **DRM bypass** — won't happen, ever
- **Automatic content scraping** — this is a manual download tool
- **Account integration** — no logins, ever, full stop

---

## How to Influence the Roadmap

Open an issue with the `enhancement` label and make your case. If enough people want it and it's in scope, it moves up the list.

PRs are even better than issues. See [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## Version History

See [CHANGELOG.md](../CHANGELOG.md) for what has shipped.

---

_Last updated: February 2025. Subject to the entropy of side projects._
