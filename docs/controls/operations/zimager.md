---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZImager operations and commands

Scope: the common ADC and focus, middle-channel filter, three detector rotators, and U/V/Z imaging
channels.

Connections: [ZImager harness](../harnesses/zimager.md) and
[server harness](../harnesses/server.md). Related work:
[calibration and acquisition procedures](../../procedures/calibration.md).

## Mechanisms

| Function | Settings and commands | Status and feedback | Details still needed |
| --- | --- | --- | --- |
| ADC | Set correction; track/hold; set individual prism positions for engineering | Prism positions, correction, tracking state | Coordinate conventions, tracking inputs, controller |
| Middle-channel filter | Select named filter | Requested and sensed filter, moving/unknown/fault | Filter list and mechanism |
| Detector rotators | Set orientation; track/hold; stop; individual channel adjustment | Per-channel angle, rate, limits, reference state | Field/pupil modes and whether channels can track independently |
| Common focus | Set focus; start/stop focus maintenance; get/set focus curve | Requested and actual position, active curve, temperature or other process input | Units, reference method, process input, update interval |

Focus maintenance is intended to make slow corrections during observing. The appropriate process
signal and update interval need to be established with the optical measurements.

(detector-acquisition)=
## Science detectors

| Function | Inputs | Status and results | Details still needed |
| --- | --- | --- | --- |
| Configure science readout | Channel, exposure time, full frame/subarray, supported detector settings | Applied settings and readiness | Available modes, rates, gain and cooling controls |
| Acquire, finish, or abort | Channel selection and exposure/series settings | Per-channel progress, completed and partial frames | Channel synchronization, independent cadence, and finish/abort behavior |
| Detector characterization | Bias/pedestal, dark, gain, noise, and linearity measurements as applicable | Images and acquisition settings | Measurement procedures |

Per-frame timing needs to support the high-speed imaging requirement, including the relationship
between channels. The timing source and hardware connections are still open.

## Partial operation and recovery

Fixed-channel imaging should be able to continue through middle-channel filter changes. A failed detector
channel should leave the remaining channels available. After a controller restart, position and
acquisition state need to be recovered without disturbing a usable optical configuration.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Controller consolidation and interfaces remain open. The common focus is retained
here; independent detector focus has not been added. The present channel labels are U/V/Z. Final
band names, filter positions, and supported acquisition modes will fill out these tables as the
design develops.

:::
