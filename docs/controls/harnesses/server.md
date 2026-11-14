---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Server Harnesses & Connections

Scope: server-room equipment, readout links, and rack services. Related operations:
[computer management](../operations/computer-management.md),
[networking](../operations/networking.md), and [power control](../operations/power-control.md).

Interactive diagram: <a href="../../_static/archwrap.html?selected=imager_readout.svg">Imager readout</a>.
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
| Server-room switch | Readout computers, DRP, NAS, UPS management | Network | Ethernet management in the diagram baseline |
| U/V/Z detectors | Matching PCI cards in ZImager readout computer | CoaXPress | Three optical transports through the rack readout panel |

The NAS provides NFS storage for the readout and DRP computers. Mounts and service configuration are
in [computer management](../operations/computer-management.md).

## Readout interfaces

| Instrument end | Server end | Related harness |
| --- | --- | --- |
| Three imager channels | U/V/Z readout cards | [ZImager](zimager.md) |
| Three VIS and three NIR Archons | ZSpec readout computer | [ZSpec VIS](zspec-vis.md) and [ZSpec NIR](zspec-nir.md) |

The baseline uses external CXP optical receivers and a UPS-fed DC converter supply. Confirm
receiver power with the selected transport hardware. Rack drawings must assign panel locations,
ports, cable assemblies and connectors.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Size UPS coverage and the facility uplink for the selected equipment and readout
traffic. The CXP transport and receiver supply need qualification as a complete path.

:::
