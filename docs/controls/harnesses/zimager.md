---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZImager Harnesses & Connections

Scope: the removable imager module, its mechanisms and detectors, and external readout/services.
Related operations: [ZImager](../operations/zimager.md).

Interactive diagram: <a href="../../_static/archwrap.html?selected=zimager_full.svg">ZImager panels</a>.
The [drawing guide](diagram-guide.md) records the selected interfaces and visual conventions.

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
| ADC pair | Actuator and position-sensor wiring | Separate prism-axis circuits |
| U/V/Z detector rotators | Actuator and position-sensor wiring | One circuit per detector rotator |
| Common focus | Actuator and position-sensor wiring | Common-focus circuit |
| Middle-channel filter selector | USB | V-channel filter connection |
| Temperature monitor hub | USB; 1-Wire from hub to probes | Hub in the EBox; probes through the auxiliary panel |
| Local DC feeds | DC | 12 VDC to each detector; separate CXP converter feed |

Assign panel locations, connector designations and contacts in the assembly drawings.

## EBox internal wiring

The local computer connects to a Beckhoff EtherCAT master on the module network.
The master serves the motion drives; local USB devices connect to the computer. Local DC distribution supplies the electronics
and mechanisms.

## Detector readout

| Detector | Readout endpoint | Connection |
| --- | --- | --- |
| U | U PCI card in ZImager readout computer | CoaXPress optical transport |
| V | V PCI card in ZImager readout computer | CoaXPress optical transport |
| Z | Z PCI card in ZImager readout computer | CoaXPress optical transport |

The baseline uses separate U/V/Z optical transmitters and server-room receivers. Coiling, storage
and routing stay outside the ZFront EBox. The [server harness](server.md) covers the readout-computer
end.

Detector rotation needs cable travel and service slack. Timing/trigger connections will be added
when the acquisition hardware is selected.

## Air connections

| From | To | Detail |
| --- | --- | --- |
| ZFront air manifold | ZImager enclosure | Air feed with dryer through the fluid service panel |

## Glycol connections

| From | To | Detail |
| --- | --- | --- |
| ZFront glycol manifold | ZImager submanifold | Supply and return |
| ZImager submanifold | U/V/Z detectors | Local cooling branches |
| ZImager submanifold | EBox heat exchanger | Supply and return |

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Qualify the optical CXP path with the detectors and readout cards before fixing
connector assignments. Bench services must support the imager independently while ZFront and
ZSpec stay available.

:::
