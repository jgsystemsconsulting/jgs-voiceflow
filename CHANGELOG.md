# Changelog

All notable changes to VoiceFlow are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and VoiceFlow aims to follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

_Nothing yet._

## [0.1.0] - <RELEASE-DATE>

First public release.

### Added

- **Push-to-talk dictation** with a global hotkey (default `Ctrl+Space`), hold-to-talk or
  toggle mode, plus a cancel hotkey and a "paste last result" hotkey.
- **On-device speech-to-text** via Whisper (faster-whisper). Optional cloud STT is opt-in.
- **Transcript cleanup** — a built-in rule-based cleaner that works fully offline, plus optional
  LLM-backed cleanup (local or cloud), with graceful fallback to the offline cleaner.
- **Four output modes** — `raw`, `clean` (default), `summary`, and `prompt`.
- **Custom dictionary** for forcing specific spellings/replacements.
- **Local searchable history** (with a privacy-off switch).
- **System-tray app** with a mode menu, settings window, and an always-on-top recording overlay.
- **First-run auto-configuration** — profiles your hardware and selects the best local settings.
- **Fully-offline installer** with bundled Whisper models — install and dictate with no internet.

[Unreleased]: https://github.com/jgsystemsconsulting/jgs-voiceflow/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/jgsystemsconsulting/jgs-voiceflow/releases/tag/v0.1.0
