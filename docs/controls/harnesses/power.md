---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Power Harnesses & Connections

Scope: facility feeds, UPS arrangements, AC/DC distribution, and module isolation. Related
operations: [power control](../operations/power-control.md). Diagrams:
<a href="../../_static/archwrap.html?selected=zshooter_power.svg">supply and distribution</a> ·
<a href="../../_static/archwrap.html?selected=zshooter_connections.svg">complete connections</a>.

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
| ZFront AC distribution | ZFront AC/DC supplies | AC | Local ZFront DC rails |
| ZFront AC distribution | ZImager AC/DC supplies | AC | Through the ZFront and ZImager EBox panels and local AC distribution |
| ZFront AC distribution | VIS AC/DC supplies | 120 VAC | Through the ZFront and VIS EBox panels and local AC distribution |
| Mechanical-room facility power | Compressor and cryo monitor | Equipment supplies | Circuits and equipment inputs open |

## DC connections

| Distribution | Loads / scope | Detail |
| --- | --- | --- |
| ZFront | Local computer, lamp/motion controllers, mechanisms, manifold sensing/control | Output and branch allocation open |
| ZImager | Local electronics and mechanisms | Output and branch allocation open |
| ZSpec VIS | Local electronics and mechanisms | Output and branch allocation open |
| ZSpec NIR | Local electronics, mechanisms and Archons | DC feed from VIS DC distribution; no separate NIR UPS |

The AC/DC supplies in ZFront, ZImager and VIS feed their local smart Phoenix Contact DC
distribution. Loads branch from its monitored, switchable outputs. A DC UPS module connects
to distribution where local battery support is needed. NIR takes DC from VIS through the
EBox panels and distributes it with its own Phoenix Contact modules. The separate NIR support
cabinet provides the off-instrument feed.

The drawing follows AC and DC distribution through the modeled loads and panel paths,
including motor, detector, heater and bus-powered sensor harnesses. Click a device or a
container label for its documentation; use Focus to inspect an EBox.

<iframe title="Instrument power supply and distribution" src="../../_static/archwrap.html?selected=zshooter_power.svg" style="width:100%;height:650px;border:1px solid #cbd5df"></iframe>

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

**Team notes:** Size the local DC UPS capacity and allocate its protected loads with the electrical design.

:::
