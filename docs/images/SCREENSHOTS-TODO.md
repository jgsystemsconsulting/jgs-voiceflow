# Screenshot manifest — capture before release

The docs reference six images. **`tray-states.png` is present** (copied from the source repo). The
other five **must be captured from a real install** before the public release goes live (they
can't be faked, and a couple show the actual SmartScreen/installer chrome).

| File | Status | What it shows | Referenced by |
|---|---|---|---|
| `tray-states.png` | ✅ present | Tray icon states (idle / recording / transcribing) | (spare / general) |
| `hero.png` | ⬜ TODO | Hero shot: recording overlay + tray, for the README top | `README.md` |
| `smartscreen.png` | ⬜ TODO | The exact SmartScreen "unknown publisher" dialog + "More info → Run anyway" | `docs/quickstart.md` |
| `install-wizard.png` | ⬜ TODO | The installer wizard (per-user / start-on-login options) | `docs/quickstart.md` |
| `first-run.png` | ⬜ TODO | First-launch auto-configuration / "configuring…" indicator | `docs/quickstart.md` |
| `overlay.png` | ⬜ TODO | The always-on-top recording overlay chip near the screen edge | (README hero / general) |

**When capturing:**
- `smartscreen.png` should show the **real unsigned "unknown publisher"** dialog users will see.
- Crop/resize for web.
- **Scrub anything sensitive** — no certificate thumbprints, usernames, private file paths, or
  other private data visible in any screenshot.

> Delete this file once all six images exist — it is a staging aid, not release content. (It is a
> `.md` under `docs/`, so it passes the repo allowlist, but it shouldn't ship in the final release.)
