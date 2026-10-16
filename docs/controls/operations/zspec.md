---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZSpec operations and commands

Scope: VIS and NIR mechanisms, slit viewers, shutters, and B/G/R plus YJ/H/K science readout.

Connections: [ZSpec VIS](../harnesses/zspec-vis.md) and
[ZSpec NIR](../harnesses/zspec-nir.md). Related operations:
[environmental services](environmental-services.md), [digital functions](digital-functions.md), and
[calibration and acquisition procedures](../../procedures/calibration.md).

## Mechanisms

| Function | Settings and commands | Status and feedback | Details still needed |
| --- | --- | --- | --- |
| VIS/NIR ADC | Set correction; track/hold; individual prism adjustment | Prism positions, correction, tracking state | Coordinate conventions and tracking inputs |
| Field rotators | Set angle/offset; track/hold; stop | Angle, rate, reference state, limits | Field/pupil modes and coordinate conventions |
| NIR cold-pupil rotator | Set/track pupil orientation | Angle and tracking error | Relationship to field rotation and any mechanical coupling |
| X/Y steering | Set position or offset; halt | Requested and measured position | Coordinate conversion and usable range |
| Slit selectors | Select named slit; engineering position adjustment | Requested and sensed slit, moving/unknown/fault | Slit set, widths, and calibrated positions |
| VIS slit-view focus, if fitted | Set focus | Position | Whether an adjustable mechanism is needed |
| Detector focus | Set per-channel focus; get/set focus curve; start/stop maintenance | Position, active curve, process input | Units, warm/cold limits, and update interval |
| Relative VIS/NIR focus | Set relative focus | Requested and actual position | Units, reference, and actuator arrangement |
| VIS/NIR shutters | Exposure triggering; engineering controls as needed | Open/closed/unknown, fault | Trigger logic, sensing, and engineering modes |

The steering calibration uses slit-view coordinates, with slit-relative offsets derived from the
measured slit footprint. The [calibration procedures](../../procedures/calibration.md) develop that
relationship.

## Tracking and exposure overlap

VIS and NIR have independent steering, rotation, and ADC. Slit guiding and nod patterns are
described in [digital functions](digital-functions.md). Tracking needs current pointing/time inputs
and a defined response when those inputs stop updating.

Focus maintenance during observing and the allowed overlap of mechanism moves with exposure/readout
remain to be worked through for each path.

## Shutters

The VIS entrance shutter and NIR cold shutter are triggered by an OR of their Archon signals.
Exposure timing uses that hardware path.

| Shutter | Trigger sources | Details still needed |
| --- | --- | --- |
| VIS entrance | B/G/R Archons | OR implementation, opening/closing times, position sensing |
| NIR cold | YJ/H/K Archons | OR implementation, opening/closing times, position sensing |

The effect of a shared shutter on independent channel cadence, dark exposures, and a failed trigger
input still needs to be resolved.

## Science detectors and slit viewers

| Function | Inputs | Status and results | Details still needed |
| --- | --- | --- | --- |
| Configure science readout | Channel, exposure, readout mode, supported detector settings | Applied settings and readiness | Per-channel modes and cadence |
| Acquire, finish, or abort | Channel or series | Progress, completed and partial frames | Finish/abort behavior |
| VIS slit-view stream | Exposure, window, gain where supported | Images, timestamps, settings, source/slit measurements | Camera and interface selection |
| NIR slit-view stream | CRED2 acquisition settings | Images, timestamps, settings, source/slit measurements | Camera interface and supported modes |
| Detector characterization | Bias/pedestal, dark, gain, noise, linearity/persistence measurements as applicable | Images and acquisition settings | Measurement procedures |

The NIR slit viewer is a CRED2 outside vacuum. Its power, data, and cooling connections are in the
[ZSpec NIR harness](../harnesses/zspec-nir.md#slit-viewer-connections).

## Partial operation and recovery

VIS must remain usable with NIR warm, removed, or unavailable. A channel or controller failure needs
a recovery path that preserves the usable configuration of the remaining instrument. Cooling and
vacuum support continue according to the affected assembly's needs.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** The next additions are the actual slit options, controller/channel assignments,
shutter logic, and focus behavior during observing. Slit-view focus remains conditional. Normal and
standalone roles for the NIR computer also need agreement.

:::
