---
zs-mode: internal
myst:
  heading_anchors: 3
---

# Digital functions and coordinated operations

Scope: fine guiding, nodding/dithering, image display and quicklook, signal monitoring, and
astrometry/alignment. These functions use the capabilities described in
[ZFront/ZCal](zfront-zcal.md), [ZImager](zimager.md), and [ZSpec](zspec.md).

Measurements and observing flows are developed in the
[calibration and acquisition procedures](../../procedures/calibration.md).

## Fine guiding, nodding, and dithering

| Function | Inputs | Results and status | Details still needed |
| --- | --- | --- | --- |
| Measure slit-relative position | Slit-view image, target selection, slit calibration | Position, uncertainty, image time | Measurement method and usable signal range |
| Start/stop fine guiding | Arm, target/reference, requested position | Applied correction, tracking error, active/held state | Correction limits and update rate |
| Run a nod/dither pattern | Arm, positions, exposure/dwell settings | Current position and pattern progress | Pattern options and guiding during moves |
| Stop a pattern | Pattern | Final position and exposure state | Finish-current-exposure versus immediate interruption |

VIS and NIR need independent guiding and offset patterns, including non-sidereal operation. Internal
steering and telescope offsets will need an agreed division with the facility guider.

## Image display and quicklook

| Function | Inputs | Status and results | Details still needed |
| --- | --- | --- | --- |
| View images | Channel, raw/corrected view | Images, timestamps, acquisition settings | Stream interface and calibration selection |

## Signal monitor

| Measurement | Inputs | Output |
| --- | --- | --- |
| Source and slit placement | Slit-view or acquisition images, target and slit definition | Detection, position, acquisition quality |
| Signal quality | Science images, detector settings, applicable calibrations | Signal/noise estimate, saturation and technical warnings |
| Observing feedback | Measurements from the active exposure or series | Recommendation to continue, adjust, or reacquire, with the relevant measurements |

The operator retains the choice of observing intent. Missing images or stale measurements need a
clear indication in the displayed result.

## Astrometry and alignment solver

| Function | Inputs | Results and status | Details still needed |
| --- | --- | --- | --- |
| Solve a field | Image and catalog/reference | Coordinate solution, residuals, uncertainty | Solver and reference inputs |
| Measure relative alignment | Imager/slit-view images, optical configuration, calibration measurements | Relative positions and transforms | Configuration dependence |
| Use a calibration solution | Selected solution | Active solution and applicable configuration | Selection and storage interface |

Point-source, displaced-source, rotator/ADC, and on-sky measurements are described in the
calibration procedures. A service event need not discard a still-valid alignment solution.

## Coordinated operations

| Operation | Device capabilities used |
| --- | --- |
| Configure and acquire a target | Beam routing, slit selection, focus, rotation, ADC, images and steering |
| Take independent channel exposures | Per-channel acquisition with shared shutter/path constraints |
| Run a nod/dither pattern | Steering, guiding, and acquisition |
| Apply a named calibration configuration | Calibration insertion, point/extended source, source and brightness |

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Allocation among ICS, quicklook/DRP, and facility services remains open. The tables
can grow with concrete command examples as those interfaces are agreed.

:::
