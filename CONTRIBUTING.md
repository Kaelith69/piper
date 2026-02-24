# Contributing to Piper 🛠️

Hey, thanks for even reading this file. That already puts you ahead of most people.

Piper is a small open-source project and contributions are absolutely welcome — whether it's a bug fix, a feature, a typo correction, or just pointing out that a comment is wrong. All of it helps.

---

## Before You Start

1. **Check existing issues** — someone may have already filed the bug or requested the feature.
2. **Open an issue first** for anything non-trivial — lets us align on approach before you spend hours coding something that gets closed for architectural reasons. (Been there. It's painful.)
3. For tiny fixes (typos, docstrings, obvious one-liners) — just send the PR directly.

---

## Branching Model

We keep it simple:

| Branch | Purpose |
|--------|---------|
| `main` | Stable. What users clone. |
| `feature/<name>` | New features (e.g. `feature/playlist-support`) |
| `fix/<name>` | Bug fixes (e.g. `fix/progress-bar-zero`) |
| `chore/<name>` | Docs, tooling, cleanup (e.g. `chore/update-readme`) |

Fork the repo, create your branch off `main`, do your thing, open a PR back to `main`.

```bash
git checkout -b feature/my-cool-thing
# hack hack hack
git push origin feature/my-cool-thing
# open PR on GitHub
```

---

## Commit Style

Please follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>

[optional body]
[optional footer]
```

**Types:**

| Type | When to use |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Restructuring without changing behavior |
| `test` | Adding or fixing tests |
| `chore` | Build config, tooling |

**Examples:**

```
feat(ui): add format selector dropdown
fix(thread): prevent race condition on progress bar reset
docs(readme): add architecture diagram
chore(deps): pin yt-dlp to >=2024.1.1
```

No need to be obsessive about it — just be descriptive enough that someone reading `git log` a year from now doesn't have to guess what "misc changes" means.

---

## Code Style

- Python 3.7+ compatible
- Follow PEP 8 loosely (we're not running `flake8` on CI… yet)
- Docstrings for anything that isn't immediately obvious
- No new dependencies without discussion — the whole point is keeping the dep count low
- Keep `piper.py` readable: someone new to Python should be able to follow the flow

---

## Testing

Currently there's no automated test suite (it's a GUI app — testing is mostly "run it and click stuff"). If you're adding logic that can be unit-tested without spinning up tkinter, add a test. We'd love to grow coverage over time.

---

## Pull Request Checklist

Before opening your PR:

- [ ] Code runs without errors
- [ ] You've tested the feature/fix manually
- [ ] Commit messages are descriptive
- [ ] You haven't added new dependencies without opening an issue first
- [ ] Any docs that need updating are updated

---

## Questions?

Open an issue with the `question` label. Or just start a Discussion. We don't bite.

---

_"Always leave the code better than you found it." — The Boy Scout Rule, applied to Python_
