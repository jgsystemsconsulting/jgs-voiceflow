# Troubleshooting

## Antivirus or "Windows protected your PC" (SmartScreen) warnings

This is the most common first-run question, so here's the full picture.

- **Why it happens.** VoiceFlow's installer is a native, compressed Windows binary, and it is a free
  release that is **not code-signed** (a code-signing certificate is a paid, recurring cost). Two
  things can trigger a warning:
  1. **SmartScreen "unknown publisher".** Because the installer isn't signed, Microsoft SmartScreen
     can't identify a publisher, so it shows **"Windows protected your PC"** with an
     unknown-publisher message. This is expected for an unsigned app — it isn't a sign that anything
     is wrong with the file.
  2. **Antivirus heuristics.** Some antivirus engines flag freshly released, compressed, unsigned
     executables as a precaution (a "false positive"), even when nothing is wrong.
- **What to do.**
  - On the SmartScreen screen, click **More info → Run anyway**.
  - If your antivirus quarantines the installer, you can **allow/restore** it in your AV's
    quarantine or exclusions screen.
  - For peace of mind, download only from the
    [official releases page](https://github.com/jgsystemsconsulting/jgs-voiceflow/releases/latest) and
    [verify the SHA-256 checksum](verifying-downloads.md) before running it.

## No microphone / wrong device

If VoiceFlow can't find a microphone, you'll get a clear error on the first capture (it won't fail
silently). Check Windows **Settings → System → Sound → Input** and make sure the right device is set
as default and isn't muted, then try again.

## My GPU isn't being used

VoiceFlow only accelerates transcription on **NVIDIA GPUs (CUDA)**. AMD and Intel GPUs aren't used
for acceleration — those machines run on CPU, which is still fast enough for everyday dictation.

## The first dictation is slow / it looks frozen

The **first** transcription after you launch VoiceFlow (or after an update) loads the speech model
into memory, which adds a one-off delay of a few seconds. This is normal — subsequent dictations are
fast. If it seems stuck for much longer than that, see "no microphone" above and check the logs.

## Models / offline

The installer bundles the speech models, so transcription works with no download. If you select a
model that wasn't bundled, VoiceFlow may need to fetch it the first time (which requires a network
connection).

## Hotkey conflicts

If `Ctrl+Space` (or another hotkey) clashes with another app, rebind it in the tray →
**Settings…** → Hotkeys.

## Where are the logs and settings?

In `%APPDATA%\VoiceFlow\` — paste that into the File Explorer address bar. You'll find the config and
log files there (handy to attach to a [bug report](https://github.com/jgsystemsconsulting/jgs-voiceflow/issues/new/choose)).
