---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZFront Harnesses & Connections

Scope: ZFront enclosure and local control/actuator connections, calibration equipment, and the
interfaces to shared services. Related operations: [ZFront and ZCal](../operations/zfront-zcal.md)
and [environmental services](../operations/environmental-services.md).

Interactive diagram: <a href="../../_static/archwrap.html?selected=zfront_full.svg">ZFront panels</a>.
The [drawing guide](diagram-guide.md) records the selected interfaces and visual conventions.

## Assembly boundaries

- Exposed glycol manifold
- Exposed air manifold
- ZFront EBox: local computer/controller electronics
- Internal mechanisms: neighbor selector, ZImage/ZSpec selector, calibration insertion and
  point-source mechanisms, source assembly

## Electrical patch panels

### RNAS to ZFront EBox

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Network uplink | Fiber, 10G | RNAS to ZFront switch |
| AC feed | 120 VAC on facility UPS | ZFront AC distribution |

### ZFront EBox to ZFront mechanisms and manifolds

| Connection | Harness / service | Detail |
| --- | --- | --- |
| Calibration light sources | LEDs + quartz cable | Source circuits terminate at the mechanism/service panel |
| Calibration lamps | HVAC for each lamp; cable bundle | Separate lamp supplies through the mechanism/service panel |
| Calibration insertion / point-source mechanisms | Pneumatic actuation and position feedback | Valve/service I/O in the EBox |
| Neighbor selector | Motor and position harness | Ethernet-connected controller |
| ZImage/ZSpec selector | Pneumatic actuation and position feedback | Valve/service I/O in the EBox |
| Air manifold | Power/sense | DC supply and valve/service I/O |
| Glycol manifold | Power/sense | DC supply and valve/service I/O |

### ZFront EBox to ZImager

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Network | Copper; 100 Mb/s sufficient | ZImager local network |
| Power | AC | ZImager local supply |

The diagram uses separate U/V/Z CoaXPress optical transports to the server room. Cable
coiling, storage, and routing are external to the ZFront EBox. The detector-to-readout connections are in the [ZImager harness](zimager.md).

### ZFront EBox to ZSpec VIS EBox

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Power | 120 VAC | VIS EBox |
| Network | 10G fiber | Combined control and Archon traffic to the VIS switch |

### Panel details

The diagrams name functional panels and their circuits. The assembly drawings must assign
physical locations, connector designations, cable models and contacts.

## Air connections

| From | To | Detail |
| --- | --- | --- |
| RNAS | Exposed air manifold | Facility supply |
| Air manifold | ZImager | Enclosure air |
| Air manifold | ZSpec VIS | Enclosure air |
| Air manifold | ZFront point-source, calibration insertion, and ZImage/ZSpec selector actuators | Pneumatic baseline |

## Glycol connections

| From | To | Detail |
| --- | --- | --- |
| RNAS | Exposed glycol manifold | Supply and return |
| Glycol manifold | ZImager manifold | Supply and return |
| Glycol manifold | VIS and NIR manifolds | Independently isolated supply/return branches |
| Glycol manifold | Vacuum pump station | Supply and return |
| Glycol manifold | ZFront EBox | Heat exchanger supply and return |

Shared services: [power](power.md), [networking](networking.md), [glycol](glycol.md), and
[air](air.md).

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The three pneumatic mechanisms are the diagram baseline. Size the valves and
position feedback with the mechanical design. The estimated 40–60 m readout route motivates
optical transport; select and qualify the CXP converters before assigning connectors.

:::
