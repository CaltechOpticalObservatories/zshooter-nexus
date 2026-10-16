---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Server Harnesses & Connections

Scope: server-room equipment, readout links, and rack services. Related operations:
[computer management](../operations/computer-management.md),
[networking](../operations/networking.md), and [power control](../operations/power-control.md).

Diagram:
[server-room composition](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zshooter_hardware.d2).

## Assembly boundaries

- Server-room managed switch and UPS
- ZImager readout computer with U/V/Z PCI cards
- ZSpec readout computer
- DRP computer
- NAS
- Rack ingress and RNAS readout links

## Electrical patch panels

| From | To | Service / medium | Detail |
| --- | --- | --- | --- |
| Facility AC | Managed UPS | AC | Circuit and input connection open |
| UPS/distribution | Server equipment | AC | Outlet/load assignment open |
| Facility network | Server-room switch | Network uplink | Medium and ports open |
| Server-room switch | Readout computers, DRP, NAS, UPS management | Network | UPS may instead use USB; ports open |
| U/V/Z detectors | Matching PCI cards in ZImager readout computer | CoaXPress | Fiber conversion/local-compute choice and rack ingress open |

The NAS provides NFS storage for the readout and DRP computers. Mounts and service configuration are
in [computer management](../operations/computer-management.md).

## Readout interfaces

| Instrument end | Server end | Related harness |
| --- | --- | --- |
| Three imager channels | U/V/Z readout cards | [ZImager](zimager.md) |
| Three VIS and three NIR Archons | ZSpec readout computer | [ZSpec VIS](zspec-vis.md) and [ZSpec NIR](zspec-nir.md) |

Rack/panel locations, ports, cable assemblies, and any optical conversion will be added with the
rack layout. Drawing links will carry the detailed cable and connector assignments.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The imager readout transport and Archon network arrangement are the main choices
affecting rack ingress. Server UPS coverage and the facility uplink also need to be assigned.

:::
