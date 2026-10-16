# Optical Design

ZShooter receives the Keck I beam at the Right Nasmyth (RNAS) platform. ZFront feeds two
fixed-format
slit spectrographs covering **0.31–2.45 µm** and a three-channel optical imager, with selectable
paths
to neighboring instruments. ZShooter operates in natural seeing and will use STRATA seeing
enhancement when available.

(rnas-focus)=
## RNAS interface

The deployable tertiary, K1DM3, directs the telescope beam to ZShooter. The nominal f/14.5 focus
lies
386.5 mm in front of the elevation-bearing journal, whose inner diameter is 1.79 m. ZFront, ZImager,
and the two spectrographs are separately supported assemblies for independent alignment and removal.

The interface must accommodate facility guiding and STRATA wavefront-sensing optics alongside the
ZShooter and neighboring-instrument light paths.

## ZFront

The front-end selectors provide three observing routes:

- **ZImager:** a full fold sends the field to the imager.
- **ZSpec + ZImager:** a fold with a central approximately 30″ opening passes the central field to
  the spectrographs while reflecting the surrounding field to the imager.
- **Neighboring instruments:** the telescope beam is directed to positions left or right of ZShooter
  on the RNAS platform, at nominal 60° feed angles.

The ZCal launch enters upstream of the ZImager/ZSpec selector. An integrating sphere fed by
emission-line lamps and continuum sources provides common calibration illumination. The design
includes extended illumination for arcs and flats and an on-axis point source for registration,
focus, and steering measurements. Lamp selection, brightness ranges, and launch uniformity remain
to be finalized.

The internal source must cover the noddable spectroscopic field on every imager detector and
spectrograph slit. Full-field ZImager flats use dome or sky illumination.

The [optical-path diagram](_static/d2_diagrams/optical_train_full.svg) shows the component
connections.

## ZSpec summary

The visible and NIR spectrometers each have an independent 10″ slit, ADC, K-mirror field derotator,
slit viewer, and steering mechanism. Each asymmetric white-pupil echelle feeds three
cross-dispersers
and f/1.8 cameras. The gratings, dichroics, and cameras remain fixed during observing; the design
requires no detector or echelle mosaics.

| Spectrometer | Channel | Passband (nm) |
| --- | --- | --- |
| VIS | B | 310–430 |
| VIS | G | 430–650 |
| VIS | R | 650–980 |
| NIR | YJ | 960–1,340 |
| NIR | H | 1,470–1,830 |
| NIR | K | 1,990–2,450 |

The three VIS focal planes use **2,048×4,096 qCCDs**; the three NIR focal planes use
**2,048×2,048 LmAPDs**, all with 15 µm pixels. The NIR optics downstream of the entrance doublet
operate near 100 K, with a rotating cold Lyot stop matched to the Keck pupil.

The current performance model gives median resolving powers of approximately **18,000 with a 0.70″
slit** and **38,000 with a 0.33″ slit**. The detector scale is approximately 0.157″/pixel; the
narrow
slit spans about 2.1 pixels. Resolution varies across each order through anamorphic magnification.

See [ZSpec](zspec_optical.md) for the integrated optical layout, prescription, and throughput, and
[Performance](performance.md) for resolution maps and updated sensitivity calculations.

## ZImager summary

The September optical design uses a **CaF₂ field lens**, a common ADC, two dichroics, and three
**f/1.7 cameras**. Each camera feeds an ORCA-Quest 2 qCMOS detector with 4.6 µm pixels at
approximately
0.05″/pixel. The detector heads rotate independently for field derotation; focus and the ADC are
common to all three channels.

The optical channels span **300–400 nm**, **400–820 nm**, and **820–1,000 nm**. The middle channel
selects 400–550, 550–690, or 690–820 nm filters. These correspond to fixed u- and z-like channels
and
a selectable intermediate band.

The simulator uses 4,096×2,304 pixels per detector, giving an approximately 3.5′×2.0′ footprint.
The illuminated field and common coverage through detector rotation remain optical design checks.
ZImager supports acquisition, spectral flux normalization, and simultaneous multiband time-series
photometry. See [ZImager](zimager_optical.md) for the render, ADC, image quality, and field checks.

(guiding-and-wavefront-sensing)=
## Guiding and seeing enhancement

Facility guiding provides telescope tracking; ZSpec slit viewers interface with MAGIQ for fine
acquisition and provide the reference for independent VIS/NIR slit-relative guiding and nodding.
The guider, imager channels, and slit viewers require calibrated coordinate transforms across the
30″ common field.

With STRATA correction, telescope defocus will match the NIR EE80 to the Nyquist slit width. The
VIS/NIR relative-focus mechanism then adjusts the VIS image, balancing U-band losses against R-band
gains. This focus strategy replaces the flat tip/tilt-error allowance in the older simulations.
The saved sensitivity calculations still use the notebook's broader effective AO PSF; the sharper
STRATA estimates and focus prescription are described under [Seeing
Enhancement](seeing_enhancement.md).

## Calibration and co-alignment

The [calibration and acquisition procedures](procedures/calibration.md) define the measurements
needed to register the optical assemblies and preserve alignment during operation:

- Common point-source references and steering maps for the three imager channels and two slit
  viewers, including slit footprints and selector return repeatability.
- Wavelength and line-spread response versus source position, slit selection, rotator angle, and
  ADC setting.
- Telescope, imager, and relative VIS/NIR focus curves, followed by on-sky scale, orientation, and
  guider registration.
- Extended-source illumination and flat-field maps, with dome/sky comparisons for ZImager.

:::{container} zs-note-to-team zs-internal-only

**Optical interfaces to close**

- **RNAS focus and envelopes:** establish the allowed secondary-focus range and its aberration or
  vignetting penalties, including the focus and clearances needed by neighboring instruments and
  STRATA hardware.
- **ZFront and ZCal:** finalize selector apertures, calibration-field coverage, point-source image
  quality, and lamp brightness ranges against the acquisition and calibration procedures.
- **Requirement/design differences:** resolve the slit inventory and the ZImager fixed i-band
  requirement versus the current z-like red channel. The detailed trades and field checks are on
  the [ZSpec](zspec_optical.md) and [ZImager](zimager_optical.md) pages.

:::

<!-- Source basis: SPIE 2026 manuscript, sections 3–5 and Table 2; ZImager September 30,
2026 optical design; current requirements, calibration procedures, seeing-enhancement strategy,
and saved performance model. Newer subsystem designs and calculations supersede older values. -->

```{toctree}
:hidden:
:maxdepth: 1

zspec_optical
zimager_optical
```
