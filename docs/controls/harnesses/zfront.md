---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZFront Harnesses & Connections

Scope: ZFront enclosure and local control/actuator connections, calibration equipment, and the
interfaces to shared services. Related operations: [ZFront and ZCal](../operations/zfront-zcal.md)
and [environmental services](../operations/environmental-services.md).

Diagram:
[ZFront entities](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zfront.d2).
Item inventory: ZShooter Item Ledger.

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
| Calibration light sources | LEDs + quartz cable | Source and connector allocation open |
| Calibration lamps | HVAC for each lamp; cable bundle | Lamp and connector allocation open |
| Calibration insertion / point-source mechanisms | Actuator harness | Motor versus air selection open |
| Neighbor selector | Actuator harness | Actuator selection open |
| ZImage/ZSpec selector | Actuator harness | Motor versus air selection open |
| Air manifold | Power/sense | Controller interface open |
| Glycol manifold | Power/sense | Controller interface open |

### ZFront EBox to ZImager

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Network | Copper; 100 Mb/s sufficient | ZImager local network |
| Power | AC | ZImager local supply |

The ZImager CoaXPress route remains open between fiber transceivers and local compute. Cable
coiling, storage, and routing are external to the ZFront EBox; the readout route does not pass
through the EBox. The detector-to-readout connections are in the [ZImager harness](zimager.md).

### ZFront EBox to ZSpec VIS EBox

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Power | 120 VAC | VIS EBox |
| Network, option A | Fiber | One combined network link to the VIS EBox |
| Network, option B | Fiber | Individual links to six Archons, plus a link to the VIS EBox |

### Panel details

| Field | Assignment |
| --- | --- |
| Panel identity and location | Unassigned |
| Connector/port designation and face | Unassigned |
| External connection and internal termination | To be added to the connection tables above |
| Assembly drawing | Pending; cable models and pin assignments will be linked here |

## Air connections

| From | To | Detail |
| --- | --- | --- |
| RNAS | Exposed air manifold | Facility supply |
| Air manifold | ZImager | Enclosure air |
| Air manifold | ZSpec VIS | Enclosure air |
| Air manifold | ZFront point-source, calibration insertion, and ZImage/ZSpec selector actuators | If pneumatic actuators are selected |

## Glycol connections

| From | To | Detail |
| --- | --- | --- |
| RNAS | Exposed glycol manifold | Supply and return |
| Glycol manifold | ZImager manifold | Supply and return |
| Glycol manifold | ZSpec manifold | Supply and return |
| Glycol manifold | ZFront EBox | Heat exchanger supply and return |

Shared services: [power](power.md), [networking](networking.md), [glycol](glycol.md), and
[air](air.md).

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Calibration source inventory, controller count, actuator type (including motor
versus air), enclosure layout, panel identities, and connector families remain open. The present
CXP-6 copper run-length estimate is 40–60 m, motivating the fiber-transceiver or local-compute
choice.

:::
