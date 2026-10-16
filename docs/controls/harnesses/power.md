---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Power Harnesses & Connections

Scope: facility feeds, UPS arrangements, AC/DC distribution, and module isolation. Related
operations: [power control](../operations/power-control.md). Diagram:
[hardware composition](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zshooter_hardware.d2).

## Assembly boundaries

- Server-room UPS and rack distribution
- RNAS feed and ZFront AC/DC distribution
- ZImager DC distribution
- ZSpec VIS and NIR DC distribution
- Mechanical-room cryogenic equipment

## AC connections

| From | To | Service | Detail |
| --- | --- | --- | --- |
| Facility AC | Server-room UPS | AC | Circuit and UPS selection open |
| Server UPS/distribution | Server loads | AC | Outlet/load map open |
| RNAS facility UPS | ZFront AC distribution | 120 VAC | Feed and isolation point open |
| ZFront AC distribution | ZFront local supply | AC | Supply and local loads open |
| ZFront AC distribution | ZImager EBox | AC | Module isolation and connector open |
| ZFront AC distribution | ZSpec VIS EBox | 120 VAC | Module isolation and connector open |
| Mechanical-room facility power | Compressor and cryo monitor | Equipment supplies | Circuits and equipment inputs open |

## DC connections

| Distribution | Loads / scope | Detail |
| --- | --- | --- |
| ZFront | Local computer, lamp/motion controllers, mechanisms, manifold sensing/control | Output and branch allocation open |
| ZImager | Local electronics and mechanisms | Output and branch allocation open |
| ZSpec VIS | Local electronics and mechanisms | Output and branch allocation open |
| ZSpec NIR | Local electronics and mechanisms | VIS supply relationship and standalone input open |

Panel IDs, branch ratings, connector assignments, and grounding/bonding details will be linked
through the electrical assembly drawings. The item ledger holds the load budget.

## Module isolation

| Assembly removed | Services retained |
| --- | --- |
| ZImager | ZFront, ZSpec, and central glycol monitoring |
| NIR | VIS and the remaining instrument |
| Complete ZSpec | ZFront, ZImager, and routing to neighboring instruments |

The physical isolation points remain to be assigned.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Facility UPS is the working RNAS arrangement. Local ZFront, ZImager, and VIS
battery/UPS provisions need review against that choice. NIR needs a power connection for standalone
AIT and maintenance.

:::
