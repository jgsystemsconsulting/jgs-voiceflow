# Quickstart

From download to your first dictation in a few minutes. (The one-time download and first-run setup
take a little longer — see the notes below — but the hands-on steps are quick.)

## 1. Download

Go to the [latest release](https://github.com/jgsystemsconsulting/jgs-voiceflow/releases/latest) and download
**`VoiceFlow-Setup.exe`**.

> **Heads up:** the installer is **~700 MB** because the offline speech models are bundled inside
> it (so you can dictate with no internet afterward). On a typical connection the download takes a
> few minutes. If you'd like, [verify the download](verifying-downloads.md) before running it.

## 2. Run the installer

Double-click `VoiceFlow-Setup.exe`.

> **Windows SmartScreen / "Windows protected your PC".** VoiceFlow is a free release and is **not
> code-signed**, so Windows shows a blue **"Windows protected your PC — unknown publisher"** screen.
> This is expected. Click **More info**, then **Run anyway**.
>
> ![SmartScreen "More info → Run anyway"](images/smartscreen.png)
>
> To confirm your download is intact and matches the official release before running it, check its
> [checksum](verifying-downloads.md). For antivirus warnings, see
> [troubleshooting](troubleshooting.md).

The installer is **per-user** (no administrator rights needed). It adds a Start-Menu shortcut and
offers an optional **start-on-login** checkbox.

![Installer options](images/install-wizard.png)

## 3. First launch (one-time auto-configuration)

The first time VoiceFlow runs, it **configures itself for your hardware** — it checks your CPU,
memory, and GPU and picks the best local speech model and settings.

- This happens **once**, and runs **entirely on your machine** (nothing is uploaded).
- It typically takes **about 30 seconds to a few minutes**, depending on your hardware.
- You'll see a "configuring…" indicator while it works — a normal wait, not a freeze.

![First-run auto-configuration](images/first-run.png)

## 4. Your first dictation

1. Place your cursor where you want text (any app — editor, browser, chat).
2. **Hold `Ctrl+Space`**, speak a sentence, then **release**.
3. VoiceFlow transcribes locally, cleans the text, and pastes it at your cursor.

> The **very first** transcription after launching (or after an update) also loads the speech model
> into memory, which adds a one-off few-second delay. After that, dictation is fast.

## 5. Settings and modes

Open the tray icon → **Settings…** to change the hotkey, output mode, and providers. The output
mode (`raw` / `clean` / `summary` / `prompt`) can also be switched per-capture from the tray menu —
see the [FAQ](faq.md) for what each mode does and how to enable optional LLM cleanup.

Settings live in `%APPDATA%\VoiceFlow\`.

---

Stuck? See [troubleshooting](troubleshooting.md) or the [FAQ](faq.md).
