# O2 button microinteractions

A prototype of animated **Reply / Follow / Like** flair buttons for the O2 / WordPress.com post footer, built from After Effects → Lottie exports. Presented in a modal.

Open **`index.html`** in a browser (or via any static server). Hover and click the buttons to see the interactions; press the close ✕ / backdrop / `Esc` to dismiss the modal, then "Open dialog" to reopen.

## What's here

| File | What it is |
|---|---|
| `index.html` | The demo modal — all 6 Lottie animations inlined, self-contained (only `lottie-web` loads from CDN). |
| `segment-mapper.html` | A tool to scrub each Lottie, read exact frames, and mark per-state start/end segments, then export them as JSON. |
| `build_states.py` | Generates `index.html` from the JSONs in `states/` + the per-button config (segments, hold frames, crops). Re-run after editing config: `python3 build_states.py`. |
| `build_mapper.py` | Generates `segment-mapper.html`. |
| `states/*.json` | The raw AE Lottie exports (reply-all, reply_i1–i3, follow_i1, star_i1). |

## Buttons & states

- **Reply** (`reply_i1`, top) + `reply_i2` / `reply_i3` — hover-only variants (play hover-on, hold; play hover-off on leave).
- **Follow** (`follow_i1`) and **Like** (`star_i1`) — full toggles: hover-on/off and click-to-select/deselect, with distinct active-state hovers.

Each button is the exact O2 button SVG (box + label) with the live Lottie cropped onto the icon area via the SVG `viewBox`. A generic state machine drives hover/press per the per-button segment map.

## Lottie frame gotcha (important)

`lottie-web`'s `playSegments([s,e])` uses **absolute** comp frames *and mutates* `anim.firstFrame` to `s`. `goToAndStop(f)` is relative to the **current** `firstFrame` — so to rest on an absolute frame you must use `goToAndStop(absFrame - anim.firstFrame)`, read live. Using a captured `ip` lands on the wrong frame (this caused icons to "disappear" after one play). Comps with `ip ≠ 0` also need their segment numbers checked (some exports number segments relative to `ip`).
