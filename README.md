# O2 button microinteractions

Animated **Reply / Following / Like** flair buttons for the O2 / WordPress.com (P2) post footer, built from After Effects → Lottie exports, shown inside a faithful recreation of a P2 post page.

## ▶ Live preview

- **[Generic P2 page →](https://nick-a8c.github.io/button-micro-interaction/o2-page-replica.html)** — the full 1920px P2 post page with the live buttons, dev tuner panels, and working replies / likes behavior.
- **[Designomattic replica →](https://nick-a8c.github.io/button-micro-interaction/designomattic-p2.html)** — the same live buttons dropped into a pixel-faithful frame of a real P2 (nav bars + sidebar are static captures); dev settings hidden behind a discreet ⚙ in the top-right corner.

> Best viewed at **≥1720px wide** for the 1:1 layout. No Pages? One-click render via [htmlpreview](https://htmlpreview.github.io/?https://github.com/nick-a8c/button-micro-interaction/blob/main/o2-page-replica.html).

## What's here

| File | What it is |
|---|---|
| `o2-page-replica.html` | The prototype (see features below). **Fully self-contained** — inlines its Lottie JSON; only `lottie-web` (CDN) + placeholder avatars load externally. |
| `designomattic-p2.html` | The same interactions inside a pixel-faithful frame of a real P2 — the two nav bars and the left sidebar are static image captures (base64-inlined); the post + interaction panel + intralinks are live. Dev gears collapse behind one discreet ⚙. |
| `PAGE-REPLICA-HANDOFF.md` | Deeper notes — per-button frame maps, crops, tuners, and the Lottie gotchas. |

## Features

**The three buttons**
- **Reply** — arrow draws in on hover.
- **Following** — toggle; label flips **Follow ⇄ Followed**.
- **Like** — toggle; label flips **Like ⇄ Liked**, bumps the count (11 ⇄ 12), and pops your avatar into the likes stack.

**Motion & feedback**
- **Press** — the whole button scales down uniformly (pressed straight-on), with a tunable **press depth**.
- **Label stretch** — when a toggle's text changes, the pill's width eases old→new with a slight overshoot instead of snapping.
- **Likes avatars** — a **hover "dock" wave**: the avatar under the cursor magnifies and the effect ripples out to its neighbors.
- **Likers dropdown** — click the **"N likes"** count to open a scrollable list of everyone who liked (you appear first once you've Liked).
- **Replies thread** — Reply opens a compose field (Publish / Cancel, **Ctrl/Cmd+Enter** to post); each reply gets a random persona, a hover-to-delete ×, and its own animated Like star. Cap: 3 (test limit).

**Dev tuner panels** (top-right gear pills, one open at a time, hidden by default)
- **Reply / Following / Like** — per-button geometry: sizes, paddings, icon nudge, line thickness, crop (viewBox), spacing, label position.
- **Avatars** — the likes-stack join animation **and** the hover-wave (peak scale, spread, lift, speed).
- **Label FX** — the label-stretch motion (duration, bounce) plus the button **press depth**.

## Lottie frame gotcha (important)

`lottie-web`'s `playSegments([s,e])` uses **absolute** comp frames and mutates `anim.firstFrame` to `s`. `goToAndStop(f)` is relative to the **current** `firstFrame`, so to rest on an absolute frame use `goToAndStop(absFrame − anim.firstFrame)`, read live. Also sanity-check comps with `ip ≠ 0` (segment numbers may be `ip`-relative). More in the handoff.
