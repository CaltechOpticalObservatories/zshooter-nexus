---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZSpec VIS Harnesses & Connections

Scope: the VIS EBox, warm mechanisms, B/G/R detector packages, slit viewer, and module services.
The [ZSpec NIR harness](zspec-nir.md) covers the separately removable NIR assembly.

Related operations: [ZSpec](../operations/zspec.md) and
[environmental services](../operations/environmental-services.md).

Interactive diagram: <a href="../../_static/archwrap.html?selected=zspec_vis.svg">VIS panels</a>.
The [drawing guide](diagram-guide.md) records the selected interfaces and visual conventions.

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

The relative VIS/NIR focus actuator moves the first pre-optic, before the field rotator and ADC.

## Electrical patch panels

### ZFront EBox to VIS EBox

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Power | 120 VAC | From ZFront AC distribution |
| Network | 10G fiber | Combined control and Archon traffic to the VIS switch |

The mating panel is on the [ZFront EBox](zfront.md#zfront-ebox-to-zspec-vis-ebox).

### VIS EBox to ZSpec VIS

| Connection | Harness / service |
| --- | --- |
| ADC pair | Actuator and position-sensor wiring for two prism axes |
| Field rotator | Actuator and position-sensor wiring |
| X/Y steering | Actuator and position-sensor wiring for two axes |
| Slit selector | Actuator and position-sensor wiring |
| Relative VIS/NIR focus | Actuator and position-sensor wiring to the first pre-optic |
| B/G/R detector focus | Actuator and position-sensor wiring, one focus per channel |
| VIS slit-view focus, if fitted | Actuator and position-sensor wiring |
| VIS entrance shutter | Power and control; [Archon trigger wiring](#shutter-triggers) is separate |
| B/G/R Archons | DC power and network; detector harnesses run to the detector vessels |
| B/G/R Coldheads | Power and control |
| VIS slit viewer | Power and data; camera/interface selection is described [below](#slit-viewer-connections) |
| Temperature monitor hub | USB to hub; 1-Wire branches to enclosure probes |

### VIS EBox to NIR EBox

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Power | DC feed | From VIS DC distribution; NIR retains local conditioning/distribution |
| Network | NIR control and Archon links | VIS switch to NIR switch through the two EBox panels |

These connections terminate at the [NIR EBox input panel](zspec-nir.md#vis-ebox-to-nir-ebox).
The disconnect must leave VIS operating when NIR is removed.

## EBox internal wiring

Local AC/DC distribution powers the computer, controllers, hubs, and network electronics.
A Beckhoff EtherCAT master serves the motion drives. The module computer retains local USB
connections for the temperature hub, gauge interface, Cryotel controllers and slit viewer.

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

| Camera | Location | Baseline connections |
| --- | --- | --- |
| VIS slit viewer | Outside vacuum | DC power and USB through the auxiliary panel |

## Air connections

| From | To | Detail |
| --- | --- | --- |
| ZFront air manifold | VIS enclosure | Air feed with dryer through the fluid service panel |

## Glycol connections

| From | To | Detail |
| --- | --- | --- |
| ZFront glycol manifold | VIS distribution | Supply and return |
| VIS distribution | EBox exchanger, B/G/R Archons and coldheads | Separate supply/return branches; assign hoses with the mechanical layout |

## Vacuum connections

Each B/G/R detector vessel connects to a gauge and automatic gate-valve branch. Shared pump and
manifold connections are in the [vacuum harness](vacuum.md).
