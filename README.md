# VoiceFlow

> **Push-to-talk voice dictation for Windows. On-device. Private.**
> Hold a hotkey, speak, release — VoiceFlow transcribes your speech locally, cleans it into
> tight, ready-to-use text, and pastes it at your cursor. Free to use.

[![Download](https://img.shields.io/github/v/release/<OWNER>/voiceflow?label=download&sort=semver)](https://github.com/<OWNER>/voiceflow/releases/latest)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11%20x64-blue)](#requirements)
[![License](https://img.shields.io/badge/license-Proprietary%20%C2%B7%20Free%20to%20use-green)](LICENSE)
[![Downloads](https://img.shields.io/github/downloads/<OWNER>/voiceflow/total)](https://github.com/<OWNER>/voiceflow/releases)

![VoiceFlow recording overlay and tray states](docs/images/hero.png)

---

## What it does

- **Hold-to-talk** with a global hotkey (default `Ctrl+Space`) — speak, release, done.
- **Transcribes on your machine** with Whisper — no audio is uploaded on the default path.
- **Cleans the text** — strips filler ("um", "uh", false starts), fixes punctuation, and can
  restructure rambling speech into a tight instruction.
- **Pastes at your cursor**, clipboard-safe (your previous clipboard is restored).
- **Lives in the system tray** with a mode menu, settings, and optional start-on-login.
- **Works fully offline** — the installer bundles the speech models; cloud is opt-in only.

## Download & install

**[⬇ Download the latest release](https://github.com/<OWNER>/voiceflow/releases/latest)** —
`VoiceFlow-Setup.exe` (**~700 MB**; the offline speech models are bundled, so the download is
large but you can dictate with no internet afterward — it may take a few minutes).

Run the installer (per-user; no administrator rights needed). **Windows will warn about an unknown
publisher** the first time — choose **More info → Run anyway**. VoiceFlow is a free release and is
not code-signed yet, so this warning is expected (see the [quickstart](docs/quickstart.md) for the
exact screen). You can [verify your download's checksum](docs/verifying-downloads.md) first.

Full step-by-step walk-through (with screenshots): **[Quickstart →](docs/quickstart.md)**.
Antivirus or SmartScreen questions: see [troubleshooting](docs/troubleshooting.md).

## Privacy

On the default path, **no audio and no text ever leave your machine** — speech-to-text runs
on-device and cleanup uses a built-in offline cleaner. Cloud services are strictly opt-in. You can
verify this yourself. See the **[privacy statement & how to verify zero network use](docs/privacy.md)**.

## Requirements

- **Windows 10 or 11, 64-bit.**
- No administrator rights required.
- An **NVIDIA GPU is optional** — it speeds up transcription, but VoiceFlow runs fine on CPU.
- A microphone.

## Output modes

Switch per-capture from the tray menu:

| Mode | What it does | Needs a cloud/LLM? |
|---|---|---|
| `raw` | Verbatim transcript, lightly punctuated | No |
| `clean` | Filler removed, grammar/punctuation fixed (**default**) | No (offline cleaner) |
| `summary` | Condensed into a tight brief | Optional (better with an LLM) |
| `prompt` | Reformatted into a structured prompt | Optional (better with an LLM) |

`raw` and `clean` work fully offline. `summary`/`prompt` are best with an optional local or cloud
LLM, and fall back to the offline cleaner if none is configured. See the [FAQ](docs/faq.md).

## Verifying your download

Every release ships with a **SHA-256 checksum** so you can confirm the installer downloaded
correctly and is untampered before running it. (VoiceFlow isn't code-signed yet — so always
download from the official releases page and check the checksum.) See
**[verifying downloads →](docs/verifying-downloads.md)**.

## Support & license

- Questions, bugs, feature requests: see **[SUPPORT](SUPPORT.md)** and the
  [docs](docs/).
- VoiceFlow is **proprietary software that is free to use** — you may install and run it free of
  charge for personal or internal business use; you may not copy, modify, redistribute, or
  reverse-engineer it. See the full **[LICENSE](LICENSE)**.

---

© 2026 JG Systems Consulting Ltd. "VoiceFlow" and "JG Systems Consulting" are trademarks of
JG Systems Consulting Ltd. VoiceFlow uses open-source components (including faster-whisper and
OpenAI Whisper models), each under its own license.
