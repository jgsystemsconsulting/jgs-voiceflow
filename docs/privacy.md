# Privacy

**On the default path, nothing you say or type with VoiceFlow leaves your machine.** This page
explains exactly what that means — and how you can verify it yourself rather than take our word for
it.

## The guarantee

With the default settings (or a fresh install with no changes):

- **Speech-to-text runs on your device.** Your audio is transcribed locally by Whisper. The audio
  is never uploaded.
- **Cleanup runs on your device.** The built-in rule-based cleaner fixes punctuation and removes
  filler entirely locally. Your text is never uploaded.
- **No telemetry.** VoiceFlow does not phone home, send usage analytics, or report crashes to us.

## What is opt-in (and off by default)

VoiceFlow *can* use cloud services, but only if **you** turn them on:

- **Cloud speech-to-text** and **cloud LLM cleanup** are disabled by default. Enabling them requires
  editing the configuration to point at a provider and supply credentials — it cannot happen by
  accident.
- If you enable a cloud provider, then (and only then) the relevant audio or text is sent to that
  provider so it can do the work. That's the trade-off you opt into for cloud quality/speed.

> **One caveat worth knowing.** If you configure a *local* LLM through a tool like Ollama, make sure
> you use an on-device model. Some model names that look local (for example, anything ending in
> `:cloud`) actually route through a remote server — so your text would leave the machine despite
> the "local" label. For true zero-egress, use a genuinely on-device model.

## Verify it yourself

You don't have to trust us. You can prove that a default dictation sends nothing over the network:

1. **Block VoiceFlow from the network.** Either:
   - Create an **outbound block rule** in Windows Defender Firewall for the installed app at its full
     path:
     `%LOCALAPPDATA%\Programs\VoiceFlow\VoiceFlow.exe`
     (a bare program name won't create a working rule — use the full path), **or**
   - simply **disable your network adapter / unplug** for the test.
2. **Dictate as normal** — hold the hotkey, speak, release.
3. **Confirm the text still appears** at your cursor, with **no network traffic** (watch
   **Resource Monitor → Network**, or note that the firewall rule didn't prompt).

If transcription and cleanup still work with the network blocked, you've confirmed the default path
is fully local.

> Notes: this recipe verifies the **running app's** network use, not the installer download — for
> that, see [verifying downloads](verifying-downloads.md). It also assumes the **standard installer**
> (the normal `.exe` you downloaded); a portable build would run from a different path, in which case
> disabling the network adapter is the build-independent check.

---

Questions about offline use, GPUs, or enabling cloud providers? See the [FAQ](faq.md).
