---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZFront and ZCal operations and commands

Scope: beam routing, calibration injection, and calibration sources. Items share physical space but
do not necessarily share a controller or software owner.

Diagram:
[ZFront D2](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zfront.d2).
Connections: [ZFront harness](../harnesses/zfront.md). Related operations:
[digital functions](digital-functions.md) and
[calibration and acquisition procedures](../../procedures/calibration.md).

## Beam routing

| Function | Positions and optical path | Status and feedback |
| --- | --- | --- |
| Neighbor/instrument selection | Left, right, ZShooter | Requested route; actuator position/state; intermediate, unknown, or active route |
| ZImage/ZSpec selection | Full imager field, or central spectrograph field with the remaining field to the imager | Requested route; actuator position/state; active route |
| Calibration insertion | Upstream of ZI/ZS selection and compatible with adjacent-instrument operation | Inserted/retracted/unknown; actuator position/state |

### Motion capabilities

| Capability | Inputs | Status and feedback | Details still needed |
| --- | --- | --- | --- |
| Select neighbor or ZShooter path | Left, right, zshooter, engineering value | Requested and sensed position | Final route names, actuator, exposure overlap, sensor states and conflicting readings |
| Select ZImage/ZSpec configuration | zspec, zimage, engineering value | Requested and sensed position | Final route names, actuator, exposure overlap, sensor states and conflicting readings |
| Insert/retract calibration beam feed | in, out, engineering value | Requested and sensed position | Actuator, exposure overlap, sensor states and conflicting readings |
| Select point or extended illumination | Illumination mode | Requested and sensed position | Actuator, exposure overlap, sensor states and conflicting readings |
| Inspect or establish reference position | Mechanism | Whether position is known and how it is known | Reference method |
| Halt a move | Mechanism, if needed | Stationary state | Mid-travel state and impact on other axes |

Command latency, travel, settling, and optical readiness will need separate timing values as the
mechanisms are selected.

## Illumination capabilities

Setting a source's brightness selects and enables that source. A brightness of `0` or `off` turns it
off.

| Capability | Inputs | Status and feedback | Details still needed |
| --- | --- | --- | --- |
| Set brightness | Source and requested level | Commanded brightness, actual source state, and relevant fault | Brightness units and calibration; available electrical/optical measurements |
| Stop illumination | Source or selected group | Off state and relevant fault | Response time and behavior on control loss |

Illustrative commands:

| Example | Result |
| --- | --- |
| `UNe 100` | Select UNe, enable it, and set brightness to 100 |
| `UNe 0` or `UNe off` | Turn UNe off |

The syntax and brightness units are still to be settled with ICS.

## Operating case example: named calibration illumination config

UNe ZImager Point Source. This is an illustration of the requested configuration.

```text
config:
    name: UNe ZImager Point Source
    path: none  # don't care
    selector: zimage
    cal: in
    pointsource: in
    source: UNe
    brightness: 10
```

## Protection, faults, and recovery

Conditions that permit lamp activation and what locally prevents hazardous illumination still need
doing. Any hardware lockout/protection is yet to be defined and will be distinct from a software
inhibit.

For a failed move, failed lamp, lost controller, or interruption, the measured state, affected
capability, permitted recovery, and any effect on alignment/calibration need to be determined.
Recovery cannot require moving every selector or restarting unrelated components.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Controller consolidation, embedded/host interfaces, source inventory, actuator
selection, exposure overlap, and source-ready indications remain open. These choices need another
pass against the developing L2 and L3 requirements.

:::
