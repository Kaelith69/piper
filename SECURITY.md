# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest on `main` | ✅ |
| Older tagged releases | Best-effort |

---

## Reporting a Vulnerability

Found something sketchy? Please don't post it as a public issue — that gives bad actors a head start.

**Instead:**

1. Go to the [GitHub Security Advisories](https://github.com/Kaelith69/piper/security/advisories/new) page for this repo and open a private advisory.
2. Or email the maintainer directly (see GitHub profile for contact info).

**What to include:**

- Description of the vulnerability
- Steps to reproduce it
- Potential impact
- Suggested fix (if you have one — it's appreciated but not required)

**What happens next:**

- You'll get an acknowledgement within a few days (this is a solo project, not a security team)
- If it's valid, a fix will be prioritized and a new release cut
- You'll be credited in the changelog unless you'd prefer otherwise

---

## Scope

Piper is a desktop GUI app. Its attack surface is intentionally small:

- It makes no incoming network connections
- It writes only to paths the user explicitly chooses
- It has no web server, no API, no authentication system
- The only outbound network activity is yt-dlp downloading from YouTube

**Relevant threat categories:**

| Category | Notes |
|----------|-------|
| Remote code execution via crafted URL | yt-dlp handles URL parsing — report upstream to yt-dlp if relevant |
| Local file write outside user-chosen directory | Would be a bug — please report |
| Dependency vulnerabilities in yt-dlp | Report upstream, then open an issue here to pin/update |
| ffmpeg vulnerabilities | Report to the ffmpeg project |

---

## Dependency Security

Piper has one pip dependency: `yt-dlp`. Keep it up to date:

```bash
pip install --upgrade yt-dlp
```

yt-dlp releases frequently to keep up with YouTube's format changes, and security patches are included in those releases.

---

_We take security seriously even for a small project. A tool that downloads files to your computer warrants at least basic hygiene._
