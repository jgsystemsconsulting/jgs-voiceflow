# Verifying your download

Every VoiceFlow release ships with a **SHA-256 checksum** so you can confirm your
`VoiceFlow-Setup.exe` downloaded correctly and hasn't been tampered with before you run it. The
check takes under a minute in PowerShell.

> **Note: VoiceFlow is not code-signed yet.** This is a free release and does not (yet) carry a
> paid code-signing certificate, so Windows will show an **"unknown publisher"** warning when you
> run the installer (see [troubleshooting](troubleshooting.md)), and you **cannot** verify a
> publisher signature. The SHA-256 checksum below is therefore the way to confirm your download is
> intact and matches the official release. **Always download from the
> [official releases page](https://github.com/jgsystemsconsulting/jgs-voiceflow/releases/latest)** — never from a
> mirror or third-party site.

## Check the SHA-256 checksum

Each release includes a `SHA256SUMS.txt` file alongside the installer. Download **both** from the
official release, then in PowerShell (in the folder where you saved them):

```powershell
Get-FileHash .\VoiceFlow-Setup.exe -Algorithm SHA256
Get-Content .\SHA256SUMS.txt
```

The hash printed by `Get-FileHash` must match the one in `SHA256SUMS.txt` (case-insensitive).

## If the checksum doesn't match

If the hashes differ, **do not run the installer** — your download is corrupted or has been
tampered with. Re-download from the
[official releases page](https://github.com/jgsystemsconsulting/jgs-voiceflow/releases/latest); if it still doesn't
match, please report it privately via [SECURITY](../SECURITY.md).

> Because the checksum file is published on the same release page as the installer, it confirms the
> file is intact and matches what we published — it does not, on its own, prove who built it (that's
> what a code signature would add). Downloading only from the official release page above is what
> ties the file to us.
