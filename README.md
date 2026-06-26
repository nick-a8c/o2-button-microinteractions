# O2 button microinteractions

Animated **Reply / Following / Like** flair buttons for the O2 / WordPress.com (P2) post footer, built from After Effects → Lottie exports, shown inside a faithful recreation of a P2 post page.

## ▶ Live preview

**[Open the page →](https://nick-a8c.github.io/o2-button-microinteractions/o2-page-replica.html)** — the full 1920px P2 post page with the live buttons, the dev tuner panels, and the working replies/likes behavior.

> Best viewed at **≥1920px wide** for the 1:1 layout. No Pages? One-click render via [htmlpreview](https://htmlpreview.github.io/?https://github.com/nick-a8c/o2-button-microinteractions/blob/main/o2-page-replica.html).

## What's here

| File | What it is |
|---|---|
| `o2-page-replica.html` | The prototype — a 1920px P2 post page with the three animated buttons (Reply hover, Following + Like toggles), four collapsible tuner panels, the Follow label flip, the Like count + animated avatar stack, and a working replies thread (compose / publish / remove). **Fully self-contained** — inlines its Lottie JSON, only `lottie-web` (CDN) + placeholder avatars load externally. |
| `PAGE-REPLICA-HANDOFF.md` | Full notes — per-button frame maps, crops, the tuners, and the Lottie gotchas. |

## Lottie frame gotcha (important)

`lottie-web`'s `playSegments([s,e])` uses **absolute** comp frames and mutates `anim.firstFrame` to `s`. `goToAndStop(f)` is relative to the **current** `firstFrame`, so to rest on an absolute frame use `goToAndStop(absFrame − anim.firstFrame)`, read live. Also sanity-check comps with `ip ≠ 0` (segment numbers may be `ip`-relative). More in the handoff.
