# Usage Guide 🎮

> _"You paste a URL, you click Download, you get a file. This page is longer than it needs to be."_

---

## Launching Piper

```bash
python piper.py
```

A 480×520 window opens. It looks like this:

```
┌──────────────────────────────────────┐
│               Piper                  │  ← neon cyan title
│                                      │
│  Enter YouTube URL:                  │
│  [_________________________________] │  ← url input
│                                      │
│  Select type:                        │
│  ◉ Video (1080p)                     │
│  ○ Audio (High Quality MP3)          │
│                                      │
│  ~/Downloads            [Browse…]    │
│                                      │
│          [ Download ]                │
│                                      │
│  [████████████░░░░░░░░░░░]           │  ← progress bar
│  ┌──────────────────────────────┐    │
│  │ Starting download…           │    │  ← scrolling log
│  │ Downloading… 42.3%           │    │
│  └──────────────────────────────┘    │
└──────────────────────────────────────┘
```

---

## Step-by-Step

### 1. Paste a YouTube URL

Click the input field and paste a full YouTube URL. Both formats work:

- `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- `https://youtu.be/dQw4w9WgXcQ`

> **Note:** Playlist URLs and channel URLs are not currently supported — single videos only.

### 2. Choose a Download Mode

**Video (1080p)**
- Downloads the best available video stream (up to 1080p) + best audio stream
- Merges them into a single `.mp4` file using ffmpeg
- Result: `<Title>-<VideoID>-video.mp4`

**Audio (High Quality MP3)**
- Downloads the best available audio stream
- Converts it to 192 kbps MP3 using ffmpeg
- Result: `<Title>-<VideoID>-audio.mp3`

### 3. Choose a Save Folder (Optional)

The default save location is `~/Downloads` (your home Downloads folder).

Click **Browse…** to pick a different folder. Your choice persists for the session.

### 4. Click Download

The button disables itself while downloading — this is intentional. One download at a time.

Watch the progress bar and log:

```
Starting download…
Downloading… 12.5%
Downloading… 31.8%
Downloading… 67.2%
Downloading… 99.9%
Download finished; post-processing…
```

### 5. Find Your File

Once the button re-enables, the file is in your chosen folder.

---

## File Naming

Files are named using the video's title and ID:

| Mode | Pattern | Example |
|------|---------|---------|
| Video | `<Title>-<VideoID>-video.mp4` | `Rick Astley - Never Gonna Give You Up-dQw4w9WgXcQ-video.mp4` |
| Audio | `<Title>-<VideoID>-audio.mp3` | `Rick Astley - Never Gonna Give You Up-dQw4w9WgXcQ-audio.mp3` |

The video ID suffix prevents collisions if you download multiple things with similar titles.

---

## Progress Bar Behavior

The progress bar moves based on `downloaded_bytes / total_bytes`. A few quirks:

- **Stuck at 0%?** Some streams don't report `total_bytes` upfront. The bar will jump to 100% when the download finishes — it's not frozen, just uninformed.
- **Jumps after 100%?** The post-processing step (ffmpeg merge/conversion) happens after the download completes. The bar stays at 100% during this phase.
- **Multiple hops?** For video mode, yt-dlp may download the video stream and audio stream separately, so you might see two progress cycles.

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+V` | Paste URL into input field (standard) |
| `Enter` | — (Download button must be clicked manually) |

---

## Use Cases

| What you want | How to do it |
|---------------|-------------|
| Watch a lecture offline | Video mode → `.mp4` → plays in VLC or any media player |
| Archive a podcast episode | Audio mode → `.mp3` → works in any audio player |
| Grab background music | Audio mode → `.mp3` |
| Save a tutorial to watch later | Video mode → `.mp4` |
| Extract audio from a music video | Audio mode → gets the best audio stream, not the video |

---

## Things Piper Cannot Do (Currently)

- Download playlists or channels (single videos only)
- Download multiple URLs simultaneously (one at a time)
- Let you choose resolution (1080p is the cap; lower resolutions are chosen automatically if 1080p isn't available)
- Show a thumbnail preview
- Auto-update yt-dlp

These are on the [roadmap](Roadmap.md).
