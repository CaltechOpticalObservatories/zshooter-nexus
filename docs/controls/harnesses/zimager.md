---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZImager Harnesses & Connections

Scope: the removable imager module, its mechanisms and detectors, and external readout/services.
Related operations: [ZImager](../operations/zimager.md).

Interactive diagram: <a href="../../_static/archwrap.html?selected=zimager_connections.svg">ZImager panels</a>.
The [drawing guide](diagram-guide.md) records the selected interfaces and visual conventions.

## Assembly boundaries

- ZImager EBox: computer, individual motion drives, DC supply/distribution/UPS, and three CXP optical transmitters
- One ZImager enclosure: ADC pair, filter selector, three detector rotators, common focus, and all U/V/Z detectors
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
| Temperature monitor hub | USB; 1-Wire from hub to probes | Hub in the EBox; probes through the mechanism/detector panel |
| Local DC feeds | DC | 12 VDC to each detector; separate CXP converter feed |

The mechanism/detector panel carries motion, filter, temperature, detector power and detector CXP
connections. Assign connector designations and contacts in the assembly drawings.

## EBox internal wiring

The local computer connects to a Beckhoff EtherCAT master on the module network.
The master serves the motion drives; local USB devices connect to the computer. The AC/DC supplies
feed smart Phoenix Contact DC distribution, which supplies the electronics and mechanisms. A DC UPS module connects to
that distribution for charging and backup power where needed.

## Detector readout

| Detector | Readout endpoint | Connection |
| --- | --- | --- |
| U | U PCI card in ZImager readout computer | CoaXPress optical transport |
| V | V PCI card in ZImager readout computer | CoaXPress optical transport |
| Z | Z PCI card in ZImager readout computer | CoaXPress optical transport |

Each detector connects through the common mechanism/detector panel to its optical transmitter in the
ZImager EBox. Fibers leave through the EBox fiber panel, cross the RNAS fiber panel, and emerge at the
server-room facility panel. Three receivers in the ZShooter rack connect to the cards inside the
readout host. The [server harness](server.md) covers that end of the path.

Detector rotation needs cable travel and service slack. Timing/trigger connections will be added
when the acquisition hardware is selected.

## Air connections

| From | To | Detail |
| --- | --- | --- |
| ZFront air manifold | ZImager enclosure | Direct feed to the enclosure air dryer |

## Glycol connections

| From | To | Detail |
| --- | --- | --- |
| ZFront smart glycol manifold | ZImager submanifold | Direct supply/return connection |
| ZImager submanifold | U/V/Z detectors | Local cooling branches |
| ZImager submanifold | EBox heat exchanger | Through the EBox cooling panel |

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Qualify the optical CXP path with the detectors and readout cards before fixing
connector assignments. Bench services must support the imager independently while ZFront and
ZSpec stay available.

:::
