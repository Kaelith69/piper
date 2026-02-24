# Privacy 🔏

> _"We don't track you. We don't even want to know what you're downloading. That's your business."_

---

## The Short Version

**Piper collects zero data about you or your usage.**

No analytics. No telemetry. No crash reports. No user accounts. No cloud sync. Nothing leaves your machine except the download request to YouTube.

---

## What Network Requests Does Piper Make?

The **only** outbound network activity is initiated when you click Download:

1. yt-dlp contacts YouTube servers to fetch video metadata and stream URLs
2. yt-dlp downloads the stream data from YouTube's CDN servers
3. (Nothing else)

These are the same requests your browser makes when you watch the video. The difference is that yt-dlp saves the data to a local file instead of playing it in a player.

---

## What Data Does Piper Store?

| Data | Stored? | Where? |
|------|---------|--------|
| Your YouTube URLs | No | Not logged or saved anywhere |
| Downloaded files | Yes — by you | Wherever you choose with the Browse button |
| App settings | No | No config file is created |
| Usage statistics | No | — |
| Crash reports | No | — |
| IP address | No | — |

The only persistent output of Piper is the file you downloaded.

---

## Third-Party Components

Piper uses two external components that make their own network connections:

### yt-dlp

yt-dlp is the download engine. It contacts YouTube to:
- Fetch video metadata (title, available formats, stream URLs)
- Download the video/audio streams

yt-dlp itself does not phone home or collect usage data. It is open source: [github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)

### ffmpeg

ffmpeg runs locally as a subprocess. It performs audio/video processing on files already downloaded to your machine. It makes no network connections.

---

## YouTube's Terms of Service

Downloading YouTube videos may violate YouTube's Terms of Service depending on your use case. Piper is a tool — the user is responsible for how they use it.

**Legal uses typically include:**
- Videos with Creative Commons licenses
- Your own uploaded content
- Content where the creator explicitly permits downloading
- Educational/personal use under applicable fair use provisions (varies by jurisdiction)

**Consult a lawyer for specifics.** This is not legal advice.

---

## Running Piper Offline

After you download a file, Piper (and the downloaded file) work entirely offline. There's no license check, no activation, no "phone home on startup." You can copy the files anywhere.

---

## Source Code Transparency

Piper's entire logic is in one file: `piper.py` (~222 lines). You can read exactly what it does in a few minutes. There are no obfuscated modules, no binary blobs, no compiled dependencies inside the repo itself.

If you're paranoid (healthy), read the source before running it. If you're extra paranoid, run it in a network-isolated VM and inspect the traffic. You'll find it talks to YouTube and nowhere else.
