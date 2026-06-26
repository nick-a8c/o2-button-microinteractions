# Handoff — O2 / P2 post-footer page replica

_Last updated: 2026-06-26_

## TL;DR

`o2-page-replica.html` is a **pixel-ish recreation of a WordPress.com P2 post page at 1920×1080**, built to test the animated **Reply / Following / Like** flair buttons in their real context and at near-final size. The three buttons are driven by After Effects → Lottie exports (the `v2` 65×65 set), and the page also models the *surrounding behavior*: the Follow label flips, the Like count + avatar stack react, and a working replies thread can be composed/published/removed.

Every file is self-contained — the only external dependency is `lottie-web` from a CDN and `pravatar.cc` placeholder avatars. All Lottie JSON is inlined.

---

## Files

| File | Purpose |
|---|---|
| **`o2-page-replica.html`** | The main deliverable — full P2 page (1920px) with the live buttons, tuner panels, and the replies/likes behavior. **This is the one to look at.** |
| `o2-footer-replica.html` | Standalone footer-only version (just the action row + intralinks). Older; does **not** have the replies/label/avatar state work. |
| `icons-test.html` | Isolated 65×65 icon tester — the three icons side by side with their live dimensions, for sanity-checking exports. |
| `o2-anim-gallery / o2-buttons / reply-arrow / star-heart .html` | Early explorations, kept for reference. |

Lottie sources live outside the repo in `~/Desktop/json test/v2/`: **`reply-2.json`, `follow-2.json`, `like_i2b.json`** (all 65×65). They are inlined into the HTML, so the HTML is the source of truth at runtime; re-inline if you re-export.

---

## The three animated buttons

Each button overlays a Lottie SVG on a real-looking O2 button. The SVG's `viewBox` is overridden to **crop** to just the icon art (the comps have the icon off-centre in a larger canvas). A per-button JS state machine drives playback.

### Frame maps (absolute comp frames @30fps)

**Reply** — `reply-2.json` (`ip44–op91`), hover-only:
- hover-on `44→84`, hover-off `85→91`, rest `44`. Crop `viewBox 10 18 50 30`.

**Following** — `follow-2.json` (`ip0–op145`), full toggle, **starts switched OFF**:
- rest (off) `~10` · hover-on (off) `11→33` · **select** `40→74` · rest (on) `74` · hover-on (on) `102→106` · **deselect** `106→122` · hover-off (off) `125→130`. Crop `viewBox 8 8 50 50`.
- The **label flips** with state: off = "Follow", on = "Following".

**Like** — `like_i2b.json` (`ip0–op169`), full toggle:
- rest `0` · **hover-on `0→64` plays at 200%** · **select** `75→111` · **deselect** `120→140` · hover-off `142→168`. Crop `viewBox -2 -8 64 69`.
- Liking bumps the **count** (11→12) and animates **your avatar** into the likes stack (see below).

### Crops are size-independent
Crops are `viewBox` strings (comp-coordinate units), so resizing the icon container doesn't change the crop. The reply Like-stars reuse the Like crop at a smaller container (27px).

---

## Surrounding behavior (state/context, not just hover)

- **Follow label** — text + icon toggle together (`Follow` ⇄ `Following`).
- **Like → likes row** — count `11 ⇄ 12`; on like, your avatar **animates into the front** of the stack and the rest **shift right with a staggered FLIP**; on unlike it reverses. Tunable (see below).
- **Replies thread** — starts **empty** (“0 replies”). The Reply button's number and the “N replies” heading are both driven by the live reply count.
  - Click **Reply** → a compose field (textarea + Publish/Cancel) appears under the thread.
  - **Publish** → renders a reply (random persona — 10 of them — name + avatar), increments the count everywhere.
  - Each reply has a **hover-only “×”** to delete it (updates the count) and its **own animated Like star** (same `like_i2b` animation, 27px).
  - **Cap: 3 replies total** (test limit) — change `MAX` in the replies script.

---

## Tuner panels (dev tools)

Four collapsible gear pills, top-right, **one open at a time**, hidden by default:

| Gear | Controls |
|---|---|
| **Reply ⚙ / Following ⚙ / Like ⚙** | Per-button: button width/height, icon size, icon paddings, icon X/Y nudge, line thickness, crop X/Y/W/H, icon↔label gap (can go negative), label paddings, label vertical position. |
| **Avatars ⚙** | The likes-stack animation: New avatar appear (ms), Others shift (ms), Stagger delay (ms), Appear start scale, plus **Replay** (previews it) and **Reset**. |

Each panel's defaults + Reset map are baked into the script — they reflect the last dialled-in values. **Liked-avatars defaults:** appear **200ms**, shift **430ms**, stagger **20ms**, start scale **0.45**.

To bake new values: edit the control `val:` AND the reset-map object for that control (and the `var P={…}` init for the avatars panel).

---

## Gotchas / lessons (read before changing animation code)

1. **`goToAndStop(f, true)` is relative to `firstFrame`, not absolute.** To rest on an absolute frame use `goToAndStop(absFrame − anim.firstFrame, true)`, reading `firstFrame` **live** (it mutates after every `playSegments`). Getting this wrong rests on the wrong frame (e.g. Like once showed an up-arrow instead of the star).
2. **`playSegments([s,e], true)` uses absolute frames** and mutates `firstFrame` to `s`. That's why it's used for all transitions.
3. **`ip` offsets bite.** `reply-2` is `ip44`; `like_i2b` is `ip0` (an earlier export was `ip16`, which shifted every frame by 16 — re-check `ip`/`op` on every re-export).
4. **Crop via `viewBox`, never `transform: scale()`** (scaling rasterizes/blurs the SVG). When the canvas size changed (100→65, 418→65) the crops had to be re-derived for the new coordinate space.
5. **Per-frame stroke override** (`stroke-width` via CSS `!important`) wins over Lottie's attribute, but it also affects burst lines — fine, just be aware.
6. **Avatar FLIP** records `getBoundingClientRect` before/after the DOM insert, inverts with `transition:none`, forces a reflow (`offsetWidth`), then plays with a per-index stagger delay. The overshoot easing (`cubic-bezier(.34,1.4,.5,1)`) gives the bounce.

---

## Run / view

No build step. It's a fixed **1920px-wide** canvas — open at that width to see it 1:1:
```sh
# from this folder:
python3 -m http.server 4822
# then open http://localhost:4822/o2-page-replica.html  (view at ≥1920px wide)
```
Buttons: hover Reply; click Following / Like to toggle; click Reply to compose a thread reply. Tune via the gear pills.

---

## Open items / next steps

- **Only `o2-page-replica.html`** has the label/likes/replies/avatar work. The footer + test files are older; mirror if needed.
- Avatars, names, like count, and reply personas are **placeholders** (pravatar + a hardcoded list). Productionizing means wiring to the real user/likes/comments data.
- Reply is **hover-only** as an icon; the page's Reply *button* opens the compose flow, but the icon has no press/active state. A cleaner reply export would be needed for a full toggle.
- The whole thing is a **standalone prototype** — no real O2 wiring. Inlined JSON would be replaced by proper asset loading in production.
