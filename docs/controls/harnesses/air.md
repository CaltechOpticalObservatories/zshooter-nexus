---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Air Harnesses & Connections

Scope: facility air, enclosure feeds, and the selected ZFront pneumatic actuators.
Related operations: [environmental services](../operations/environmental-services.md#air). Diagram:
<a href="../../_static/archwrap.html?selected=zshooter_connections.svg">instrument connections</a>.

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
| ZFront manifold | ZImager enclosure | Positive pressure, with dryer | Direct feed to the enclosure air dryer |
| ZFront manifold | ZSpec VIS enclosure | Positive pressure, with dryer | Dryer placement and module connection open |
| ZFront manifold | Point-source, calibration insertion, ZImage/ZSpec selector actuators | Pneumatic supply | Valve ports, exhaust, and actuator connections open |

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
