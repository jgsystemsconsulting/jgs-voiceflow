# FAQ

## Is it really free?

Yes — VoiceFlow is **free to use**. It is *proprietary* software (the source isn't public, and you
may not copy, modify, or redistribute it), but you can install and run it free of charge for
personal or internal business use. See the [LICENSE](../LICENSE).

## Does it work offline?

Yes. On the default settings, speech-to-text and cleanup both run on your machine, and the installer
bundles the speech models — so you can dictate with no internet at all.

## Do I need a GPU?

No. VoiceFlow runs on CPU. An **NVIDIA GPU** (with CUDA) makes transcription faster, but it's
optional. AMD/Intel GPUs aren't used for acceleration — those machines fall back to CPU, which is
still fast enough for everyday dictation.

## Which languages does it support?

VoiceFlow uses Whisper, which supports many languages. It works best when you set your language
explicitly in Settings (that's also faster than auto-detect).

## How do I get better cleanup (summary / prompt modes)?

The `clean` mode works offline with no setup. For `summary` and `prompt`, results are better with a
language model:

- **Local LLM:** point VoiceFlow at a local OpenAI-compatible server (for example, Ollama or LM
  Studio). This keeps everything on your machine — see [privacy](privacy.md) for the on-device
  caveat.
- **Cloud LLM:** point it at a cloud provider for the fastest, highest-quality cleanup (your text is
  sent to that provider).

Both are opt-in and configured in Settings / the config file. If no LLM is configured,
`summary`/`prompt` fall back to the offline cleaner.

## How big is the download, and why?

About **700 MB**. The installer bundles the Whisper speech models so VoiceFlow works fully offline
out of the box, with no separate model download.

## Does it send my voice anywhere?

**No, not on the default path** — audio and text stay on your machine. Cloud providers are opt-in
only. See [privacy](privacy.md) for the full statement and a recipe to verify it yourself.

## How do I uninstall VoiceFlow?

Uninstall it like any Windows app: **Settings → Apps → Installed apps → VoiceFlow → Uninstall** (or
use the **"Uninstall VoiceFlow"** Start-Menu shortcut). That removes the per-user install, including
the bundled speech models.

A couple of things are **left behind on purpose** so you don't lose data if you reinstall — remove
them manually if you want a clean wipe:

- Your settings and dictation history in `%APPDATA%\VoiceFlow\` (the `config.toml` and the history
  database).
- Any extra speech models you downloaded later (in the faster-whisper / Hugging Face model cache).

## How do I update to a new version?

VoiceFlow v0.1.x has **no auto-update**. To update, download the latest `VoiceFlow-Setup.exe` from
the [releases page](https://github.com/jgsystemsconsulting/jgs-voiceflow/releases/latest) and run it over your
existing install — your settings and history in `%APPDATA%\VoiceFlow\` are preserved. Each installer
is the full ~700 MB (models are re-bundled); there's no smaller delta update yet.

## Is the source code available?

No — VoiceFlow is proprietary. It isn't code-signed yet (that's a paid certificate we may add
later), so download only from the
[official releases page](https://github.com/jgsystemsconsulting/jgs-voiceflow/releases/latest) and
[verify the SHA-256 checksum](verifying-downloads.md) to confirm your copy is intact.
