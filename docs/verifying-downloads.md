# Verifying your download

Every VoiceFlow release ships with a **SHA-256 checksum** and a **code signature** so you can confirm
your `VoiceFlow-Setup.exe` is genuine and untampered before you run it. Both checks take under a
minute in PowerShell.

## 1. Check the SHA-256 checksum

Each release includes a `SHA256SUMS.txt` file alongside the installer. Download both, then in
PowerShell (in the folder where you saved them):

```powershell
Get-FileHash .\VoiceFlow-Setup.exe -Algorithm SHA256
Get-Content .\SHA256SUMS.txt
```

The hash printed by `Get-FileHash` must match the one in `SHA256SUMS.txt` (case-insensitive). If it
doesn't match, **do not run the installer** — re-download it, and if it still doesn't match, report
it (see [SECURITY](../SECURITY.md)).

## 2. Check the code signature

A valid signature proves the installer was signed by us and hasn't been modified since.

**The quick way:** right-click `VoiceFlow-Setup.exe` → **Properties** → **Digital Signatures** tab.
You should see a signature, and the signer name should be **`<CANONICAL-SIGNER-CN>`**.

**The thorough way (PowerShell):**

```powershell
$s = Get-AuthenticodeSignature .\VoiceFlow-Setup.exe

# (1) The signature must be valid:
$s.Status        # must be: Valid

# (2) The signer's common name must be ours:
$s.SignerCertificate.GetNameInfo('SimpleName', $false)   # must be: <CANONICAL-SIGNER-CN>
```

**Both** must be true:

1. `Status` is `Valid`, **and**
2. the signer common name equals **`<CANONICAL-SIGNER-CN>`**.

> A `Valid` status **alone is not enough** — *any* correctly-signed file shows `Valid`. The signer
> identity is what proves it's *ours*. Note: check the **common name** as shown above; don't try to
> match the full `SignerCertificate.Subject` string, which is a longer technical identifier
> (`CN=…, O=…, C=…`) and won't equal a plain name.

## If a check fails

A bad checksum, a `NotSigned`/`UnknownError` status, or a *valid-but-wrong-signer* result all mean
you should **not** run the file. Re-download from the
[official releases page](https://github.com/<OWNER>/voiceflow/releases/latest); if it still fails,
please report it privately via [SECURITY](../SECURITY.md).
