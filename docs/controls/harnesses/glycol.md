---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Glycol Harnesses & Connections

Scope: supply/return circuits, manifolds, cooling loads, and module disconnects. Related operations:
[environmental services](../operations/environmental-services.md#glycol).

Diagrams:
[hardware composition](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zshooter_hardware.d2)
and
[glycol view](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/views/glycol_only.d2).

## Assembly boundaries

- ZFront manifold with temperature, flow, leak monitoring, and shutoff
- ZImager submanifold
- ZSpec VIS submanifold
- ZSpec NIR submanifold
- Mechanical-room compressor cooling

## Supply and return connections

| From | To | Detail |
| --- | --- | --- |
| RNAS facility supply/return | ZFront manifold | Facility interface, isolation, and sensing |
| ZFront manifold | ZFront EBox heat exchanger | Local cooling branch |
| ZFront manifold | ZImager submanifold | Removable-module connection |
| ZImager submanifold | U/V/Z detectors and EBox heat exchanger | Branch layout open |
| ZFront manifold | ZSpec distribution | Removable-module connection |
| VIS distribution | EBox heat exchanger, B/G/R Archons and cryocoolers | Branch layout open; slit-viewer cooling conditional |
| NIR distribution | EBox heat exchanger, YJ/H/K Archons, external CRED2 | Branch layout open |
| Mechanical-room facility cooling | NIR compressor | Separate facility circuit |

The vacuum pump also has a cooling connection; its supply/return route is unassigned. Any NIR
coldhead glycol connection remains to be confirmed with the cryogenic design.

## Manifold and hose details

Manifold ports, supply/return fittings, hose assemblies, and isolation points will be added with the
circuit drawings. Electrical connections for the ZFront manifold are in the
[ZFront harness](zfront.md).

Leak monitoring must remain available when ZImager or ZSpec is disconnected. Each removable branch
needs isolation and caps while the other circuits remain in use.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Branch layout, flow allocation, service fluid, fittings, and shutoff coverage remain
open. The disconnected-module arrangement is part of the manifold design.

:::
