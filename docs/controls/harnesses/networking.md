---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Networking Harnesses & Connections

Scope: network links, switches, and patching. Addresses and network operations are in
[networking operations](../operations/networking.md).

Diagrams:
[hardware composition](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zshooter_hardware.d2)
and
[network view](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/views/network_only.d2).

## Assembly boundaries

- Server-room network
- RNAS/ZFront switch
- ZImager local network
- ZSpec VIS/NIR networks and Archon links
- Mechanical-room cryo monitor

## Network patch panels

| From | To | Medium / rate | Detail |
| --- | --- | --- | --- |
| Facility network | Server-room switch | Open | Uplink and ports to be assigned |
| RNAS network | ZFront switch | Fiber, 10G | RNAS and EBox panel connections open |
| ZFront switch | ZImager local network | Copper; 100 Mb/s sufficient | Removal connection open |
| ZFront | ZSpec VIS EBox | Fiber | Combined link, or separate EBox and six Archon links |
| VIS network | NIR local network | Open | Topology and standalone NIR connection open |
| Local computers/switches | Controllers | Ethernet, USB, or EtherCAT as selected | Local paths in subsystem harnesses |
| Server-room switch | Readout computers, DRP, NAS | Open | Port and traffic allocation open |
| Archon network links | ZSpec readout computer | Open | End-to-end route open |
| Facility network | Mechanical-room cryo monitor | Open | Port and route open |

The ZSpec alternatives are detailed in the
[ZFront harness](zfront.md#zfront-ebox-to-zspec-vis-ebox). Detector CoaXPress links are in the
[ZImager](zimager.md) and [server](server.md) harnesses.

## Port assignments

Switch ports, patch-panel ports, and cable IDs will be added to the connection table as the topology
is selected. The assembly drawings will supply cable models and connector details.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The shared uplink versus individual Archon fibers determines much of the VIS/NIR
switch layout. Module disconnects also need a straightforward temporary uplink for bench operation.

:::
