---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter networking operations

Scope: control, detector readout, storage, and facility network connections. Physical routes and
ports are in the [networking harness](../harnesses/networking.md).

Facility network services are assumed for NTP/PTP, DNS, and access to telescope/observatory services.


## Network connections

| Area | Equipment and services | Details still needed |
| --- | --- | --- |
| Server room | Managed switch, UPS management, readout computers, DRP, NAS | Addresses, ports, and readout/storage traffic allocation |
| ZFront | RNAS uplink, local computer, lamp/motion controllers, shared service monitoring | Controller interfaces and switch ports |
| ZImager | Local control computer and mechanisms | Local interfaces and bench configuration |
| ZSpec VIS/NIR | Local computers, motion/environmental controllers, six Archons | Shared uplink versus individual Archon fibers; local switch arrangement |
| Mechanical room | Cryo monitor | Facility connection and address |

## Operations and status

| Function | Inputs | Status or result |
| --- | --- | --- |
| Inspect a connection | Host, device, or network branch | Link state, endpoint, service response, last successful contact |
| Inspect a managed switch | Switch | Port connections, link state, configuration |
| Configure an endpoint | Device and address/settings | Applied configuration |
| Reconnect a device | Device or service | Connection state and current device status |

A lost connection needs a visible indication of when the device last responded. On reconnection, the
current device state and any interrupted command need to be recovered before the operation
continues.

## Standalone operation

Each module needs a bench configuration for its local computer and controllers. The local
connections and temporary uplink will be listed with the module's harness.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The ZFront connection plan uses a 10G fiber uplink, copper to ZImager, and fiber to
ZSpec. The ZSpec Archon topology remains open. Controller choices will determine the remaining USB,
Ethernet, and EtherCAT connections. Address assignments and switch configuration can be added here
as those choices settle.

:::
