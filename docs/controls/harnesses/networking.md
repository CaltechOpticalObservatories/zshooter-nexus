---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Networking Harnesses & Connections

Scope: network links, switches, and patching. Addresses and network operations are in
[networking operations](../operations/networking.md).

Interactive diagram: <a href="../../_static/archwrap.html?selected=zshooter_ethernet.svg">Network topology</a>.
The [drawing guide](diagram-guide.md) records the selected interfaces and visual conventions.

## Assembly boundaries

- Server-room network
- RNAS/ZFront switch
- ZImager local network
- ZSpec VIS/NIR networks and Archon links
- Mechanical-room cryo monitor

## Network patch panels

| From | To | Medium / rate | Detail |
| --- | --- | --- | --- |
| Facility network | 10G server-room switch | 10G Ethernet | Through the rack service panel |
| RNAS network | ZFront switch | Fiber, 10G | Through the RNAS and EBox facility panels |
| ZFront switch | ZImager local network | Copper; 100 Mb/s sufficient | Through the ZImager service input panel |
| ZFront | ZSpec VIS EBox | 10G fiber | Combined control and Archon traffic |
| VIS switch | NIR switch | Ethernet | Through the VIS output and NIR input panels |
| ZFront, ZImager and VIS switches | Local DC distribution | Ethernet | Output switching and status |
| Module switches | Beckhoff masters | Ethernet | One master each for ZImager, VIS and NIR |
| Beckhoff masters | Motion drives | EtherCAT | Local to each EBox |
| Server-room switch | ZImager readout host, DRP, NAS | 10G Ethernet | Separate host connections |
| Server-room switch | ZSpec readout host | 1G Ethernet | 10G may be fitted for common host specifications |
| Archons | ZSpec readout computer | Ethernet | Module switches → VIS uplink → facility network → server switch |
| Facility network | Mechanical-room cryo monitor | Ethernet | Direct network connection |

The combined ZSpec link is detailed in the
[ZFront harness](zfront.md#zfront-ebox-to-zspec-vis-ebox). Detector CoaXPress links are in the
[ZImager](zimager.md) and [server](server.md) harnesses.

## Port assignments

Assign switch ports, patch-panel ports and cable IDs when laying out the selected topology. The assembly drawings will supply cable models and connector details.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Check aggregate readout bandwidth and traffic isolation when choosing the
switches. Preserve a temporary uplink at each module disconnect for bench operation.

:::
