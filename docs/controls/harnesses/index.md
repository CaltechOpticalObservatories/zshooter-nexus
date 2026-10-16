---
zs-mode: internal
myst:
  heading_anchors: 3
---

# Harnesses

Harnesses and connections for installing, removing, and testing the four instrument assemblies.

## Instrument assemblies

| Assembly | Connection records |
| --- | --- |
| [ZFront](zfront.md) | RNAS feeds, local electronics, selectors, calibration, and downstream modules |
| [ZImager](zimager.md) | Local motion/control, detector readout, and removable-module services |
| [ZSpec VIS](zspec-vis.md) | VIS EBox, warm mechanisms, B/G/R detector packages, slit viewer, and services |
| [ZSpec NIR](zspec-nir.md) | NIR EBox, cryostat, feedthroughs, cold wiring, YJ/H/K readout, and services |

## Shared services

| Service | Connection records |
| --- | --- |
| [Server room](server.md) | Readout computers, acquisition cards, storage, and network connections |
| [Networking](networking.md) | Uplinks, module links, switches, and patching |
| [Power](power.md) | Facility/UPS feeds, AC/DC distribution, and module isolation |
| [Glycol](glycol.md) | Supply/return circuits, manifolds, monitoring, and isolation |
| [Air](air.md) | Supply, enclosure pressure, and proposed pneumatic actuators |
| [Vacuum](vacuum.md) | Four vessel branches, gauges, gate valves, and shared pump |

[Operations](../operations/index.md) describes the behavior controlled through these connections.

```{toctree}
:hidden:
:maxdepth: 1

ZFront <zfront>
ZImager <zimager>
ZSpec VIS <zspec-vis>
ZSpec NIR <zspec-nir>
Server room <server>
Networking <networking>
Power <power>
Glycol <glycol>
Air <air>
Vacuum <vacuum>
```
