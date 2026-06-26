# Changelog

All notable changes to VoiceFlow are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and VoiceFlow aims to follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

_Nothing yet._

## [0.2.0] - 2026-06-26

Adds a code-focused dictation mode for developers who dictate to AI coding assistants.

### Added

- **`code` output mode** (rule-based, no LLM, instant and on-device): trims spoken politeness
  and filler down to the imperative, keeps words that matter in code, and fixes programming
  terms. Selectable per capture from the tray menu. This brings the output modes to five.
- **Code-aware dictionary**: a built-in table that rewrites spoken programming terms into the
  symbols and names you meant (for example "dunder init" to `__init__`, "fast api" to `FastAPI`,
  "triple equals" to `===`). It merges with your personal dictionary, where your entries win,
  and applies in every mode, not just `code`.

### Changed

- The output modes are now `raw`, `clean` (default), `summary`, `prompt`, and `code`.

## [0.1.0] - 2026-06-19

First public release.

### Added

- **Push-to-talk dictation** with a global hotkey (default `Ctrl+Space`), hold-to-talk or
  toggle mode, plus a cancel hotkey and a "paste last result" hotkey.
- **On-device speech-to-text** via Whisper (faster-whisper). Optional cloud STT is opt-in.
- **Transcript cleanup**: a built-in rule-based cleaner that works fully offline, plus optional
  LLM-backed cleanup (local or cloud), with graceful fallback to the offline cleaner.
- **Four output modes**: `raw`, `clean` (default), `summary`, and `prompt`.
- **Custom dictionary** for forcing specific spellings and replacements.
- **Local searchable history** (with a privacy-off switch).
- **System-tray app** with a mode menu, settings window, and an always-on-top recording overlay.
- **First-run auto-configuration**: profiles your hardware and selects the best local settings.
- **Fully-offline installer** with bundled Whisper models: install and dictate with no internet.

[Unreleased]: https://github.com/jgsystemsconsulting/jgs-voiceflow/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/jgsystemsconsulting/jgs-voiceflow/releases/tag/v0.2.0
[0.1.0]: https://github.com/jgsystemsconsulting/jgs-voiceflow/releases/tag/v0.1.0
