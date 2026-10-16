---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Air Harnesses & Connections

Scope: facility air, enclosure feeds, and ZFront actuators if pneumatic mechanisms are selected.
Related operations: [environmental services](../operations/environmental-services.md#air). Diagram:
[hardware composition](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zshooter_hardware.d2).

## Assembly boundaries

- ZFront air manifold and pressure sensing
- ZFront enclosure and mechanisms
- ZImager enclosure feed
- ZSpec VIS enclosure feed

## Air connections

| From | To | Service | Detail |
| --- | --- | --- | --- |
| RNAS facility air | ZFront manifold | Supply | Regulation, treatment, and isolation open |
| ZFront manifold | ZFront enclosure | Positive pressure | Local route open |
| ZFront manifold | ZImager enclosure | Positive pressure, with dryer | Dryer placement and module connection open |
| ZFront manifold | ZSpec VIS enclosure | Positive pressure, with dryer | Dryer placement and module connection open |
| ZFront manifold | Point-source, calibration insertion, ZImage/ZSpec selector actuators | Pneumatic supply, if selected | Valve ports, exhaust, and actuator connections open |

## Electrical connections

| From | To | Function |
| --- | --- | --- |
| ZFront EBox | Manifold | Power and pressure sensing |
| Mechanism controller | Valves and position sensors, if fitted | Mechanism actuation and position |

Local wiring is in the [ZFront harness](zfront.md). Tube assemblies, fittings, ports, and removal
connections will be linked through the manifold and harness drawings.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The actuator choice determines the valve arrangement and loss-of-air position.
Enclosure pressure/flow requirements, treatment, and isolation of removed modules remain to be
assigned.

:::
