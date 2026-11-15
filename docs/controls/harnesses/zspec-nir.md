---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZSpec NIR Harnesses & Connections

Scope: the removable NIR assembly, including its EBox, cryostat, feedthroughs, cold wiring,
YJ/H/K readout, external CRED2 slit viewer, and coldhead/compressor connections.

Related operations: [ZSpec](../operations/zspec.md) and
[environmental services](../operations/environmental-services.md).

Interactive diagram: <a href="../../_static/archwrap.html?selected=zspec_nir_connections.svg">NIR panels</a>.
The [drawing guide](diagram-guide.md) records the selected interfaces and visual conventions.

## Assembly boundaries

- **NIR EBox:** computer, network, motion/temperature controllers, DC distribution, and
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
| Power | DC feed | From VIS DC distribution, through the NIR service input panel |
| Network | NIR control and Archon links | VIS switch to NIR switch through the two EBox panels |

The mating panel is on the [VIS EBox](zspec-vis.md#vis-ebox-to-nir-ebox). NIR plugs into a separate <a href="../../_static/archwrap.html?selected=zspec_nir_support.svg">support cabinet</a>
for power, network and cooling during standalone AIT and maintenance. Warm-side disconnects must allow NIR removal while VIS remains operational.

### NIR EBox to cryostat and warm devices

| Connection | Harness / service |
| --- | --- |
| Support/motion VIB: mechanisms | Actuator and position-sensor wiring; [cold-side connections](#support-motion-vib) |
| Support/motion VIB: thermal control | Temperature-sensor and heater wiring |
| YJ/H/K Archons | Power and network; detector harnesses run to the detector VIB |
| Enclosure probes | USB hub with 1-Wire branches |

The cryostat connections continue through the [support/motion VIB](#support-motion-vib).
The [CRED2 slit viewer](#slit-viewer-connections) remains outside vacuum.

## EBox internal wiring

The incoming VIS DC feed and local distribution power the computer, controllers, hubs, and network electronics.
A Beckhoff EtherCAT master serves the motion drives. The module computer retains local USB
connections for the temperature hub and the gauge USB/FTDI serial cable.
The Thermocopia temperature controller connects to the local network. NIR has no separate DC UPS.

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

Each Archon provides its detector's sensor/heater circuits through the detector VIB. The
Thermocopia controller serves the general cryostat sensors and heaters through the support VIB.

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

| Camera | Location | Baseline connections |
| --- | --- | --- |
| NIR CRED2 | Outside vacuum | DC and Ethernet through the auxiliary panel; glycol from the NIR manifold |

The viewing port is baffled and has a cold shortpass filter to exclude warm infrared background.

## Coldhead and compressor connections

| From | To | Service | Detail |
| --- | --- | --- | --- |
| Mechanical-room compressor | Coldhead | Helium lines | Direct compressor-to-coldhead run |
| Compressor/control equipment | Coldhead | Vane-motor cable | Direct compressor-to-coldhead run |
| Cryo monitor | Cryogenic equipment / network | Monitoring and control | Local equipment connection and facility-network uplink |

Compressor facility power and cooling are in the [power](power.md) and [glycol](glycol.md)
harnesses.

## Glycol connections

| From | To | Detail |
| --- | --- | --- |
| ZFront smart glycol manifold | NIR glycol manifold | Direct supply/return connection |
| NIR distribution | EBox exchanger, YJ/H/K Archons, CRED2 | Separate supply/return branches; assign hoses with the mechanical layout |

## Vacuum connections

The NIR cryostat connects to a gauge and automatic gate-valve branch. The shared pump, manifold,
and removable-NIR isolation connection are in the [vacuum harness](vacuum.md).

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The location and any glycol connection of the NIR coldhead need confirmation with
the cryogenic design.

:::
