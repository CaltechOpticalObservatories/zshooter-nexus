---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter computer management operations

Scope: hosts, services, readout, and storage. Connections are in the
[server](../harnesses/server.md), [networking](../harnesses/networking.md), and subsystem harnesses.

## Computer roles

| Computer | Role | Details still needed |
| --- | --- | --- |
| ZImager readout | U/V/Z acquisition through three PCI readout cards | Channel/port mapping and acquisition services |
| ZSpec readout | B/G/R and YJ/H/K acquisition through six Archons | Controller connections and acquisition services |
| DRP | Data reduction | Services and data paths |
| NAS | NFS storage for readout and DRP | Mounts, capacity, and storage outage handling |
| ZFront | Local mechanisms, calibration, and shared services | Service and controller assignments |
| ZImager | Local mechanisms and environmental monitoring | Service and controller assignments |
| ZSpec VIS | Local mechanisms and environmental control | Service and controller assignments |
| ZSpec NIR | Standalone AIT/maintenance and spare capability | Normal role and changeover arrangements |

## Operations and status

| Function | Inputs | Status or result |
| --- | --- | --- |
| Inspect a computer | Host | Identity, time, resource use, storage, running services |
| Inspect configuration | Host or service | Software/configuration versions and connected hardware |
| Start, stop, or restart | Service | Running state and current device/acquisition state |
| Shut down or reboot | Host | Shutdown/restart progress and storage status |

Restarting a service should recover the current hardware state and preserve a usable science
configuration. Homing or moving a mechanism will depend on whether its position is still known.

Restoring/replacing a computer needs an unattended setup script for new computers.

## Storage and standalone operation

A NAS outage needs a defined acquisition response: available local buffering, remaining capacity,
and handling of completed and partial files. These details belong with the readout services once
storage is selected.

Module-local computers support independent AIT and maintenance. Their deployed service lists and
bench configurations will be linked here as they develop.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The NIR computer's normal and spare roles need agreement. A changeover must leave
one computer controlling the affected hardware. The mechanism for doing that remains open.

:::
