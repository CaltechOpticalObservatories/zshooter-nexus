---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZImager Harnesses & Connections

Scope: the removable imager module, its mechanisms and detectors, and external readout/services.
Related operations: [ZImager](../operations/zimager.md). Diagram:
[ZImage entities](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zimage.d2).

## Assembly boundaries

- ZImager EBox: computer, controllers, and DC distribution
- Internal Mechanisms: 
  - ADC pair, filter selector, three detector rotators, and common focus
  - U/V/Z detector assemblies
- Exposed glycol submanifold
- Enclosure air feed connector

## Electrical patch panels

### ZFront EBox to ZImager EBox

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Power | AC | ZImager AC distribution |
| Network | Copper; 100 Mb/s sufficient | ZImager local network |

### ZImager EBox to mechanisms, sensors, and manifold

| Connection | Harness / service | Detail |
| --- | --- | --- |
| ADC pair | Actuator and position-sensor wiring | Axis/channel allocation open |
| U/V/Z detector rotators | Actuator and position-sensor wiring | One rotator per detector; channel allocation open |
| Common focus | Actuator and position-sensor wiring | Axis/channel allocation open |
| Middle-channel filter selector | USB | Filter-wheel selection open |
| Temperature monitor hub | USB; 1-Wire from hub to probes | Hub placement, probe locations, and branches open |
| Local DC feeds | DC | External electronics and mechanism loads to be assigned |

Panel locations, connector/port designations, pin assignments, and assembly drawings remain open.

## EBox internal wiring

The local computer connects to the motion controllers through USB, Ethernet, or EtherCAT; interface
selection and controller consolidation remain open. Local DC distribution supplies the electronics
and mechanisms; load allocation remains open.

## Detector readout

| Detector | Readout endpoint | Connection |
| --- | --- | --- |
| U | U PCI card in ZImager readout computer | CoaXPress; transport route open |
| V | V PCI card in ZImager readout computer | CoaXPress; transport route open |
| Z | Z PCI card in ZImager readout computer | CoaXPress; transport route open |

The long readout route needs fiber conversion or a local-compute arrangement. Coiling, storage, and
routing remain outside the ZFront EBox. The [server harness](server.md) covers the readout-computer
end.

Detector rotation needs cable travel and service slack. Timing/trigger connections will be added
when the acquisition hardware is selected.

## Air connections

| From | To | Detail |
| --- | --- | --- |
| ZFront air manifold | ZImager enclosure | Air feed with dryer; isolation and removal connection open |

## Glycol connections

| From | To | Detail |
| --- | --- | --- |
| ZFront glycol manifold | ZImager submanifold | Supply and return |
| ZImager submanifold | U/V/Z detectors | Local cooling branches |
| ZImager submanifold | EBox heat exchanger | Supply and return |

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The next harness choices are controller interfaces, readout transport, and the
removable-module connections. Bench services need to support the imager independently while ZFront
and ZSpec remain available.

:::
