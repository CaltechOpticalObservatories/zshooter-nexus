---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Glycol Harnesses & Connections

Scope: supply/return circuits, manifolds, cooling loads, and module disconnects. Related operations:
[environmental services](../operations/environmental-services.md#glycol).

Interactive diagram: <a href="../../_static/archwrap.html?selected=zshooter_glycol.svg">Glycol distribution</a>.
The [drawing guide](diagram-guide.md) records the selected interfaces and visual conventions.

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
| ZFront manifold | ZFront EBox heat exchanger | Through the EBox cooling panel |
| ZFront manifold | ZImager submanifold | Direct supply/return connection |
| ZImager submanifold | U/V/Z detectors and EBox heat exchanger | Branch layout open |
| ZFront manifold | VIS and NIR manifolds | Direct, independently isolated supply/return branches |
| ZFront manifold | Vacuum pump station | Supply/return through the pump service panel |
| VIS distribution | EBox heat exchanger, B/G/R Archons and cryocoolers | Branch layout open; slit-viewer cooling conditional |
| NIR distribution | EBox heat exchanger, YJ/H/K Archons, external CRED2 | Branch layout open |
| Mechanical-room facility cooling | NIR compressor | Separate facility circuit |

The pump cooling branch is part of this diagram baseline. Confirm any additional NIR coldhead
services with the selected cryogenic equipment.

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
