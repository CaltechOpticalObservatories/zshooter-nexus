---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZSpec NIR Harnesses & Connections

Scope: the removable NIR assembly, including its EBox, cryostat, feedthroughs, cold wiring,
YJ/H/K readout, external CRED2 slit viewer, and coldhead/compressor connections.

Related operations: [ZSpec](../operations/zspec.md) and
[environmental services](../operations/environmental-services.md). Diagrams:
[NIR assembly](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zspec.d2)
and
[mechanical-room connections](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zshooter_hardware.d2).

## Assembly boundaries

- **NIR EBox:** computer, network, motion/temperature controllers, AC/DC distribution, and
  heat exchanger.
- **Cryostat interior:** cold-pupil rotator, ADC pair, field rotator, X/Y steering, slit selector,
  cold shutter, YJ/H/K detectors and focus stages, and thermal sensors/heaters.
- **Cryostat interfaces:** support/motion VIB, detector VIB, vacuum gauge, and automatic
  gate-valve branch.
- **Outside vacuum:** YJ/H/K Archons, CRED2 slit viewer, and enclosure temperature probes.
- **Cooling services:** glycol manifold and coldhead; helium lines and vane-motor cable connect
  to the compressor/control equipment in the mechanical room.

## Electrical patch panels

### VIS EBox to NIR EBox

| Connection | Service / medium | Detail |
| --- | --- | --- |
| Power | NIR supply feed | From VIS EBox; supply arrangement is not yet selected |
| Network | NIR control and Archon links | Routing follows the [VIS network choice](zspec-vis.md#zfront-ebox-to-vis-ebox) |

The mating panel is on the [VIS EBox](zspec-vis.md#vis-ebox-to-nir-ebox). NIR also needs power,
network, and cooling for standalone AIT and maintenance, without the VIS assembly. Warm-side
disconnects must allow NIR removal while VIS remains operational.

### NIR EBox to cryostat and warm devices

| Connection | Harness / service |
| --- | --- |
| Support/motion VIB: mechanisms | Actuator and position-sensor wiring; [cold-side connections](#support-motion-vib) |
| Support/motion VIB: thermal control | Temperature-sensor and heater wiring |
| YJ/H/K Archons | Power and network; detector harnesses run to the detector VIB |
| Enclosure probes | May use the NIR temperature controller for monitoring |

The cryostat connections continue through the [support/motion VIB](#support-motion-vib).
The [CRED2 slit viewer](#slit-viewer-connections) remains outside vacuum.

## EBox internal wiring

Local AC/DC distribution powers the computer, controllers, hubs, and network electronics.
Computer-to-controller/hub links are USB, Ethernet, or EtherCAT, according to controller selection.
The NIR temperature controller connects to the local network.

## Cryostat feedthroughs

### Support/motion VIB

| Warm-side connection | Cold-side equipment | Wiring |
| --- | --- | --- |
| Motion controllers | Cold-pupil rotator, ADC pair, field rotator, X/Y steering, slit selector, cold shutter, YJ/H/K focus | Actuator and position-sensor wiring |
| Temperature controller | Thermal sensors and heaters | Sensor and heater circuits |

### Detector VIB

| Warm-side connection | Cold-side equipment | Wiring |
| --- | --- | --- |
| YJ Archon | YJ detector | YJ detector harness |
| H Archon | H detector | H detector harness |
| K Archon | K detector | K detector harness |

Detector temperature-sensor and heater wiring still needs a VIB assignment.

## Cryostat internal wiring

The support/motion VIB feeds the mechanism and thermal harnesses. The detector VIB feeds separate
YJ/H/K detector harnesses.

| Assembly | Drawing content |
| --- | --- |
| Support/motion VIB | Exterior connectors, feedthrough mapping, interior mechanism and thermal harnesses |
| Detector VIB | Exterior connectors, YJ/H/K channel mapping, internal detector harnesses |
| Internal harnesses | Vacuum-compatible assemblies, thermal anchoring, motion allowance, and accessible service breaks |

## Shutter triggers

| Shutter controller | Trigger inputs | Connection to shutter |
| --- | --- | --- |
| NIR cold | Hardware OR of YJ/H/K Archon signals | Actuator wiring through the support/motion VIB |

The OR circuit and shutter-position sensing connections still need definition.

## Slit-viewer connections

| Camera | Location | Connections | Details still needed |
| --- | --- | --- | --- |
| NIR CRED2 | Outside vacuum | Power, data, glycol | Supply, host/interface, and hose connections |

## Coldhead and compressor connections

| From | To | Service | Detail |
| --- | --- | --- | --- |
| Mechanical-room compressor | Coldhead | Helium lines | Line assemblies, route, and service breaks open |
| Compressor/control equipment | Coldhead | Vane-motor cable | Equipment connectors and route open |
| Cryo monitor | Cryogenic equipment / network | Monitoring and control | Signal allocation open |

Compressor facility power and cooling are in the [power](power.md) and [glycol](glycol.md)
harnesses.

## Glycol connections

| From | To | Detail |
| --- | --- | --- |
| ZFront glycol manifold | NIR distribution | Supply and return |
| NIR distribution | EBox exchanger, YJ/H/K Archons, CRED2 | Branch layout open |

## Vacuum connections

The NIR cryostat connects to a gauge and automatic gate-valve branch. The shared pump, manifold,
and removable-NIR isolation connection are in the [vacuum harness](vacuum.md).

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The location and any glycol connection of the NIR coldhead need confirmation with
the cryogenic design.

:::
