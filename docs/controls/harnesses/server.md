---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Server Harnesses & Connections

Scope: server-room equipment, readout links, and rack services. Related operations:
[computer management](../operations/computer-management.md),
[networking](../operations/networking.md), and [power control](../operations/power-control.md).

Interactive diagram: <a href="../../_static/archwrap.html?selected=zimager_readout.svg">Imager readout</a>.
The [drawing guide](diagram-guide.md) records the selected interfaces and visual conventions.

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
| Facility AC | Managed UPS | AC | Through the rack service panel |
| UPS/distribution | Server equipment | AC | Assign outlets with the rack layout |
| Facility network | Server-room switch | Network uplink | Through the rack service panel |
| 10G server-room switch | ZImager readout host, DRP, NAS | 10G Ethernet | Separate host links |
| Server-room switch | ZSpec readout host | 1G Ethernet | 1G is sufficient; 10G may be fitted for common host specifications |
| Server-room switch | UPS management | Ethernet | Management connection |
| U/V/Z detectors | Matching PCI cards in ZImager readout computer | CoaXPress | Three optical transports through the RNAS and server-room facility fiber panels |

The NAS provides NFS storage for the readout and DRP computers. Mounts and service configuration are
in [computer management](../operations/computer-management.md).

## Readout interfaces

| Instrument end | Server end | Related harness |
| --- | --- | --- |
| Three imager channels | U/V/Z readout cards | [ZImager](zimager.md) |
| Three VIS and three NIR Archons | ZSpec readout computer | [ZSpec VIS](zspec-vis.md) and [ZSpec NIR](zspec-nir.md) |

Three CXP optical receivers sit in the ZShooter rack and take power directly from its managed UPS.
The U/V/Z readout cards are inside the ZImager readout host. Rack drawings must assign ports,
cable assemblies and connectors.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Size UPS coverage and the facility uplink for the selected equipment and readout
traffic. Qualify the complete CXP transport path.

:::
