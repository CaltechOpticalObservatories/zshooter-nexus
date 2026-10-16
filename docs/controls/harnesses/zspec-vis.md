---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZSpec VIS Harnesses & Connections

Scope: the VIS EBox, warm mechanisms, B/G/R detector packages, slit viewer, and module services.
The [ZSpec NIR harness](zspec-nir.md) covers the separately removable NIR assembly.

Related operations: [ZSpec](../operations/zspec.md) and
[environmental services](../operations/environmental-services.md). Diagrams:
[ZSpec](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zspec.d2)
and
[detector assemblies](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/subsystems.d2).

## Assembly boundaries

- **VIS EBox:** computer, network, motion and cryocooler controllers, AC/DC distribution, and
  heat exchanger.
- **Internal mechanisms and slit viewer:** entrance shutter, ADC pair, field rotator, X/Y
  steering, slit selector, and slit viewer with focus if fitted.
- **B/G/R detector packages:** one detector cryostat, focus stage, coldhead, vacuum gauge, and
  automatic gate-valve per channel.
- **Warm detector electronics:** B/G/R Archons, outside the detector cryostats.
- Exposed glycol manifold
- Enclosure air feed connector

The relative VIS/NIR focus actuator's mounting location is not yet assigned.

## Electrical patch panels

### ZFront EBox to VIS EBox

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Power | 120 VAC | From ZFront AC distribution |
| Network, option A | Fiber | One combined link to the VIS EBox |
| Network, option B | Fiber | Individual links to six Archons, plus a link to the VIS EBox |

The mating panel is on the [ZFront EBox](zfront.md#zfront-ebox-to-zspec-vis-ebox).

### VIS EBox to ZSpec VIS

| Connection | Harness / service |
| --- | --- |
| ADC pair | Actuator and position-sensor wiring for two prism axes |
| Field rotator | Actuator and position-sensor wiring |
| X/Y steering | Actuator and position-sensor wiring for two axes |
| Slit selector | Actuator and position-sensor wiring |
| Relative VIS/NIR focus | Actuator and position-sensor wiring; actuator location determines final panel assignment |
| B/G/R detector focus | Actuator and position-sensor wiring, one focus per channel |
| VIS slit-view focus, if fitted | Actuator and position-sensor wiring |
| VIS entrance shutter | Power and control; [Archon trigger wiring](#shutter-triggers) is separate |
| B/G/R Archons | AC power and network; detector harnesses run to the detector vessels |
| B/G/R Coldheads | Power and control |
| VIS slit viewer | Power and data; camera/interface selection is described [below](#slit-viewer-connections) |
| Temperature monitor hub | USB to hub; 1-Wire branches to enclosure probes |

### VIS EBox to NIR EBox

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Power | NIR supply feed | Supply arrangement between VIS and NIR is not yet selected |
| Network | NIR control and Archon links | Routing depends on the combined-link or individual-fiber choice above |

These connections terminate at the [NIR EBox input panel](zspec-nir.md#vis-ebox-to-nir-ebox).
The disconnect must leave VIS operating when NIR is removed.

## EBox internal wiring

Local AC/DC distribution powers the computer, controllers, hubs, and network electronics.
Computer-to-controller/hub links are USB, Ethernet, or EtherCAT, according to controller selection.

## Detector harnesses and feedthroughs

| Detector assembly | External harness | Physical boundary |
| --- | --- | --- |
| VIS B | B Archon to B detector | B vessel feedthrough |
| VIS G | G Archon to G detector | G vessel feedthrough |
| VIS R | R Archon to R detector | R vessel feedthrough |

The VIS cryocooler controllers have separate power, control, and sensing connections to their
B/G/R detector assemblies.

## Shutter triggers

| Shutter controller | Trigger inputs | Connection to shutter |
| --- | --- | --- |
| VIS entrance | Hardware OR of B/G/R Archon signals | Warm shutter actuator |

The OR circuit and shutter-position sensing connections still need definition.

## Slit-viewer connections

| Camera | Location | Connections | Details still needed |
| --- | --- | --- | --- |
| VIS slit viewer | Outside vacuum | Power, data, possible glycol | Camera/interface selection and cooling need |

## Air connections

| From | To | Detail |
| --- | --- | --- |
| ZFront air manifold | VIS enclosure | Air feed with dryer; removal connection open |

## Glycol connections

| From | To | Detail |
| --- | --- | --- |
| ZFront glycol manifold | VIS distribution | Supply and return |
| VIS distribution | EBox exchanger, B/G/R Archons and coldheads | Branch layout open; slit-viewer cooling conditional |

## Vacuum connections

Each B/G/R detector vessel connects to a gauge and automatic gate-valve branch. Shared pump and
manifold connections are in the [vacuum harness](vacuum.md).
