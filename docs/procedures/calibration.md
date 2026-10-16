---
zs-mode: both
---

# ZShooter Calibration and Acquisition Procedures

This document describes measurements used to establish ZShooter's internal registration,
illumination, focus, and acquisition model, and the observing flows that use those measurements.

ZShooter has two spectrographs, VIS and NIR, each with a slit viewer and independent steering,
rotation, and ADC, a relative focus adjustment, and per-focal-plane focus adjustment. It has three
ZImager channels that share a common ADC and focus mechanism with the detectors themselves rotating
to attain a field angle. The calibration unit is upstream of the ZImager/ZSpec+ZImager selector and
provides extended-source and point-source illumination. Procedures involving a spectrograph or
imager channel apply to each arm/channel unless a distinction is made.

Astrophysical photometric, radial-velocity, and telluric calibrations, and wavelength/RV drift
monitoring through the night, are outside this document's scope. Laboratory detector
characterization and the relationship between detector focus and encoder position are assumed well
determined during AIT and baked in when the instrument is ready for these procedures. The on-sky
focus procedure establishes the telescope and inter-arm focus reference after installation.

:::{container} zs-note-to-team zs-internal-only

**Note to the ZShooter team (JIB 10/8/26):** At this time I'm seeking feedback on completeness of
the measurements, things I may have missed, redundancies, and anything that is ambiguous or unclear.

:::

## Basis and Coordinate Model

Supporting references are still in progress and include
[ZFront/ZCal](../controls/operations/zfront-zcal.md), [ZSpec](../controls/operations/zspec.md),
[ZImager](../controls/operations/zimager.md), and
[coordinated operations](../controls/operations/digital-functions.md) notes, along with ZShooter's
optical design and SRD/OCDD.

The coordinate reference is an in-progress whitepaper *Coordinate Transforms from Working Sky
Coordinates to the Guide Detector and Science Slit.* That whitepaper and its Wolfram companions are
unfinished drafts JIB is working on. Its named reference points, guider runout model, steering
response, and guide-reference construction provide a useful framework for organizing the
measurements below.

The procedures supply measured reference positions and response functions to that model:

| Measurement                                                       | Use in the coordinate model                                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Common point-source positions                                     | Tie the three imager planes and two slit-view planes to a reproducible internal reference             |
| Steering command versus measured displacement                     | Establish each arm's local steering response and its useful range                                     |
| Slit footprint, selector position, and slit-view focus dependence | Locate the selected aperture in the measured field and preserve registration as configuration changes |
| Internal and on-sky rotator/ADC series                            | Describe angular and chromatic changes in image position and orientation                              |
| Known sky offsets and guider/slit-view comparisons                | Establish scale, orientation, parity, and the connection to the facility guider                       |
| Guider-angle series                                               | Measure repeatable angle-dependent residual motion for the guider model                               |
| Acquisition residuals                                             | Apply a field-specific refinement to the predicted placement                                          |

Slit-view pixels are the proposed reference for each arm's steering. A steering position therefore
carries its slit-view coordinate and relevant optical configuration. The slit footprint is
registered in that frame. A slit-relative offset is computed from the registered footprint when
needed. This preserves the measured steering map through slit selection and allows slit-position
changes to be examined independently.

A common point observed once in several cameras establishes corresponding reference positions.
Scale, orientation, distortion, and their configuration dependence require the additional
displaced-source and on-sky measurements described below. The internal launch point, telescope
pointing reference, telescope optical axis, and rotation centers all have separate identities even
when they are aligned.

## Execution modes and dependencies

**Establish** means obtaining the measurements needed to construct a calibration for the first time
or after a relevant change. **Verify** means comparing selected measurements with an existing
calibration. **Routine acquisition** uses accepted calibration products to place and follow a
source. Engineering/commissioning procedures are expected to become occasional verification
procedures once instrument stability is measured.

C01 and C02 include routine flat or arc acquisition as well as the fuller engineering measurements
that establish their use. C03–C09 establish internal calibration and support later verification.
C10–C12 establish the on-sky focus and registration and can be repeated as installation or
performance checks. C13 is an optional independent cross-check. C14 is an idea for engineering
STRATA guider-runout measurement; C15 is an alternative whose usefulness will be assessed from its
transfer errors.

The procedure numbers identify measurement objectives. Several objectives share a configuration or
exposure series. During initial calibration, C03–C07 are iterative: preliminary reference positions
and steering measurements support focus and slit setup; the adopted focus and slit positions then
define the final registration. Existing laboratory results can supply the starting values. Where
focus-dependent distortions are small, iterations may be omitted.

| ID                                                                  | Procedure                                                | Main dependencies and shared measurements                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| {ref}`C01 <c01>`                                                    | Full-field ZImager flats                                 | Detector corrections; supplies illumination context for {ref}`C02 <c02>`                                                  |
| {ref}`C02 <c02>`                                                    | Internal extended illumination and field coverage        | Detector corrections; feeds {ref}`C05 <c05>` and the spectral-flat context for {ref}`C08 <c08>`                           |
| {ref}`C03 <c03>`                                                    | Common point-source reference                            | Usable focus and detector corrections                                                                                     |
| {ref}`C04 <c04>`                                                    | Steering map                                             | {ref}`C03 <c03>` reference; final focus state from {ref}`C06 <c06>`                                                       |
| {ref}`C05 <c05>`                                                    | Slit footprint                                           | {ref}`C02 <c02>` extended illumination; final focus state from {ref}`C06 <c06>`                                           |
| {ref}`C06 <c06>`                                                    | Slit-view focus and coordinate stability                 | Point source; provisional {ref}`C03 <c03>`/{ref}`C04 <c04>`; feeds final {ref}`C03 <c03>`–{ref}`C05 <c05>`                |
| {ref}`C07 <c07>`                                                    | Slit-selector reference and optimal position             | {ref}`C04 <c04>`–{ref}`C06 <c06>`; spectral measurements can be shared with {ref}`C08 <c08>`                              |
| {ref}`C08 <c08>`                                                    | Wavelength and PSF response to source placement          | {ref}`C02 <c02>`–{ref}`C07 <c07>`; supplies guidance for offsets and nods                                                 |
| {ref}`C02 <c02>`/{ref}`C03 <c03>`/{ref}`C05 <c05>`/{ref}`C07 <c07>` | ZI/ZS and slit-selector return repeatability             | Embedded in other procedures                                                                                              |
| {ref}`C09 <c09>`                                                    | Internal rotator and ADC image motion                    | {ref}`C03 <c03>`/{ref}`C04 <c04>`/{ref}`C06 <c06>`; supplies the internal reference for {ref}`C11 <c11>`/{ref}`C12 <c12>` |
| {ref}`C10 <c10>`                                                    | Telescope and relative instrument focus                  | Laboratory focus/encoder calibration; usable slit-view focus from {ref}`C06 <c06>`                                        |
| {ref}`C11 <c11>`                                                    | On-sky reference registration                            | {ref}`C03 <c03>`–{ref}`C07 <c07>`, {ref}`C09 <c09>`/{ref}`C10 <c10>`; existing facility guider calibration                |
| {ref}`C12 <c12>`                                                    | Off-axis rotator and on-sky ADC verification             | {ref}`C09 <c09>`–{ref}`C11 <c11>`; uses telescope offsets and field stars                                                 |
| {ref}`C13 <c13>`                                                    | Guider/slit-view astrometry and scale cross-check        | {ref}`C11 <c11>`/{ref}`C12 <c12>`; known relative stellar astrometry                                                      |
| {ref}`C14 <c14>`                                                    | Guider runout with a two-star field                      | {ref}`C11 <c11>`–{ref}`C13 <c13>`; suitable simultaneous guider/slit-view stars                                           |
| {ref}`C15 <c15>`                                                    | Guider runout by repeated source transfer                | {ref}`C11 <c11>`–{ref}`C13 <c13>`; alternative field strategy to {ref}`C14 <c14>`                                         |
| {ref}`A01 <a01>`–{ref}`A04 <a04>`                                   | Acquisition, guiding refinement, nods, and blind offsets | Applicable accepted products from the calibration procedures                                                              |

## Measurement records

Keep raw images, measurements (values and formal errors), fits, and residuals together as a
first-class, user-friendly object. Metadata captured in the headers will already include source;
optical route; calibration state; filter; intended slit name and selector position; motor positions
(ADC, rotator, focus); steering coordinates and any offsets/zeros in play; detector settings; and
temperatures. The dome-light state is desirable. On-sky sequences also record target/reference
astrometry, telescope pointing and offsets, airmass, and the full guider positioning state (e.g.
guide-reference pixel settings and the states of guiding, the rotator, and their control loops).

A calibration product states the configuration and sampled range over which it was measured. The
software record should include reference frames, units, axis directions, and angle conventions used
in its construction. Field-specific acquisition corrections retain their own identity alongside the
underlying instrument calibration. A shortened procedure must record the calibration settings it
reused and the steps it performed.

Adopted settings are programmed into the ICS/DRP through an interface that supports manual entry of
the output settings/offsets from each calibration. The interface details are outside this document’s
scope.

## Calibration procedures

(c01)=
### C01. Full-field ZImager flats

**Purpose.** Support full-field imaging calibration and registration of the ZSpec sub-field within
ZImager.

**Starting configuration.** Telescope illumination reaches ZImager, ZCal is retracted, and ZFront is
in the full-field imager configuration. Use the detector corrections, filters, and readout settings
appropriate to the intended measurements.

**Operation flow.**

1. Obtain a dome-flat series spanning selected signal levels, from low signal to saturation.
   - Acquire all imager channels concurrently with one filter selected.
   - Obtain one mid-scale image in each remaining filter to anchor the filter-to-filter response.
2. During one exposure with the ZImager+ZSpec fold inserted, run all imager rotators through a full
   rotation to locate their centers relative to the ZSpec aperture.
3. Obtain a sky flat and record the sky position and conditions.
   - One image at a mid-to-upper signal level should be sufficient.
4. Derive the flat-field products and compare their small-scale structure, large-scale illumination
   pattern, and signal-level dependence.
5. For the fold comparison, select the ZImager+ZSpec routing and take a mid-scale image using dome
   or sky illumination. Identify the field passed to ZSpec and the region still illuminated on
   ZImager.
6. Compare the two routing configurations over their common illuminated area.
7. Retain results.

**Determines/checks.**

- Pixel-to-pixel response uniformity and QE/linearity over the sampled signal levels.
- Relative dome/sky illumination structure and changes associated with the path selector.
- ZSpec sub-field center on each ZImager detector and its offset from the rotation center.

Attributing mid- or large-scale patterns to the detector, optics, or source requires expert study
and additional measurements.

**Results.**

- Flat-field images for each channel/filter and the tested signal levels.
- Normalized dome/sky and fold-comparison maps, with illuminated-field masks.
- Detector-coordinate locations of the ZSpec aperture and rotation center, with their relative
  offset.

**Repeat use.** Routine flats can be made with a single high S/N image. The fold comparison,
rotation sweep, and signal-level series establish the calibration and can be omitted.

(c02)=
### C02. Internal extended illumination and spectrograph field coverage

**Purpose.** Provide repeatable spectral flats and arcs throughout the field used for steering and
nodding.

**Starting configuration.** Insert ZCal with its point-source mask removed. Select the imager route
first. The internal beam illuminates the central calibration field on ZImager; C01 supplies the
full-field imaging flats.

**Operation flow.**

1. Acquire quartz-illuminated images in the participating ZImager channels.
2. Repeat with individual broadband LEDs and any combined LED/quartz mixtures.
3. For engineering characterization, repeat with each arc source and compare the illuminated area
   and count rate (exposure-time anchoring and lamp-aging checks) with the continuum-source images.
4. Select the ZImager+ZSpec route and acquire continuum/trace flats and extended-source arcs.
5. **Establish field coverage:** move each arm to the extreme steering corners, acquiring exposures
   at each position. Optionally interleave central measurements to estimate source variation.
6. Compare normalized trace illumination and arc flux and line position across the sequence. Inspect
   for changes.
7. During establishment, repeat ZCal insertion and use ZImager to verify the stability of the
   launch-field location.

**Determines/checks.**

- Useful quartz/LED mixtures and spatial uniformity of the continuum and arc sources.
- Whether the extended beam overfills the intended dither field without clipping.
- Variation in trace illumination and lamp flux with steering position, accounting for source
  variation during the sequence.

**Results.**

- Source settings and exposure recipes, with source-specific illumination maps.
- Reference trace flats and extended-source arcs.
- Coverage mask and normalized illumination/flux residuals across the tested steering grid.

**Repeat use.** Routine flats and arcs use a source recipe and centered steering.

(c03)=
### C03. Internal common point-source reference in the imager and slit viewers

**Purpose.** Give subsequent calibrations and acquisitions a common internal reference across the
ZImager and slit-view planes.

**Starting configuration.** Insert the ZCal point-source mask and select mid-range broadband
illumination. Set the rotators, ADCs, steering, and focus to reference positions.

**Operation flow.**

1. Select the imager route and measure the point-source centroid in each channel/filter.
   - Optionally repeat filter selections to check middle-band stability.
2. Select the spectrograph route. Place each slit selector at the intermediate, fully reflective
   position so that the source reaches the slit viewer.
3. Calibrate/home steering actuators.
4. Measure the source in both slit viewers.
   - This anchors the point source in the two frames relative to tilt variations between the two
     selectors. Characterize those variations with an on-sky source and guider offsets.
5. If desired, switch in a slit to determine corresponding trace center.
6. Compare the positions through the instrument coordinate model.
7. If testing selector repeatability, repeat across ZImager/ZImager+ZSpec selector moves.
8. If testing point-source repeatability, repeat point-source mask insertion and measure the source
   with ZImager.

**Determines/checks.**

- Point-source centroid in each frame at the reference optical state.
- Agreement of those positions with the current instrument coordinate model.
- ZImager registration scatter and slit-view field stability after selector returns.

**Results.**

- Cross-camera reference-position table with centroid uncertainties and source PSF measurements.
- Registration residuals relative to the existing scale and orientation model.
- Return-offset distributions.

**Repeat use.** Repeat on reinstallation of ZSpec or ZImager. Refresh the affected reference
positions after C06/C07 changes focus or an adopted slit position.

(c04)=
### C04. ZSpec steering to slit-view coordinate map

**Purpose.** Convert slit-plane displacements into steering commands for ZSpec acquisition and
guiding refinement, nodding, and spectral calibration.

**Starting configuration.** Start from C03 with the point source and fully reflective slit-selector
position. Hold focus, rotator, and ADC settings fixed for a given grid. Carry out the measurement
independently for VIS and NIR.

**Operation flow.**

1. Optionally calibrate/home the steering actuators. Any zero-point update requires repeating C03.
2. Measure the source at the reference steering command.
3. Command a nine-position, 3 × 3 grid covering the intended range and measure the source centroid
   at each point.
4. Return to the reference and measure closure. Include the reversed pattern when establishing
   direction dependence.
5. Fit the command-to-image mapping, including cross-axis terms supported by the data. Use the
   residuals to identify regions needing denser sampling.
6. Verify predicted positions, including those used for along-slit and across-slit sampling.

**Determines/checks.**

- Steering direction, scale, and cross-axis coupling.
- Nonlinearity across the sampled range and any dependence on approach direction.
- Return error and accuracy at independently checked positions.

**Results.**

- Command-to-slit-view mapping and local steering Jacobian, tied to the applicable focus and optical
  state.
- Fit and verification residuals defining the usable steering range.

**Repeat use.** Should not be necessary beyond periodic engineering verification. Use the full grid
when constructing or revising the map, and C05/C07 to convert its coordinates to slit-relative
commands.

(c05)=
### C05. Slit footprint in the slit-view plane

**Purpose.** Verify slit positions and movement in the slit-view detector plane to place a source on
any selected slit.

**Starting configuration.** Use ZSpec+ZImager routing with ZCal broadband extended-source
illumination and steering at home. This shares C02’s configuration for establishing the active
region on the slit-view camera.

**Operation flow.**

1. Select the slit to be characterized.
2. Image the reflective slit surface and measure the dark opening against its surroundings.
3. Fit the aperture boundary, centerline, and endpoints, identifying poorly constrained edges.
4. Repeat for each slit. Repeated visits independently check slit-selector repeatability.
5. Register the footprints against the common point-source and steering coordinates from C03/C04.

:::{container} zs-note-to-team zs-internal-only

**Review — C05.** After C07 changes an adopted selector position, either remeasure the footprint or
use these measurements to anchor the selector’s absolute encoder scale to the slit-view plane. The
team should settle which approach to use.

:::

**Determines/checks.**

- Slit centerline, width, endpoints, and orientation in slit-view coordinates.
- Placement of each aperture relative to the common point-source and steering reference.

**Results.**

- Registered aperture model for each slit, with edge uncertainties and its selector/focus state.

**Repeat use.** Generally unnecessary. Remeasure as needed for engineering health.

(c06)=
### C06. Slit-view focus and coordinate stability

:::{container} zs-note-to-team zs-internal-only

**Review — C06.** Possibly VIS only. This procedure may be avoidable if the slit-view cameras do not
need their own focus adjustment.

:::

**Purpose.** Quantify the impact of slit-view focus on centroid and slit location measurements.

**Starting configuration.** Use the calibration point source and fully reflective slit-selector
position. Hold the other optical mechanisms fixed. Begin with nominal focus.

**Operation flow.**

1. Run through focus (slit-view camera, VIS/NIR relative) around the optimum.
   - C10 establishes telescope focus.
   - The VIS/NIR relative-focus adjustment affects the point-source position; slit-view camera focus
     sets the mapping of the physical slits onto the detector.
2. Measure source shape and centroid through the series.
3. Repeat at steering position corners to sample the field.
4. Compare the measured coordinate changes with the optical model. Retain the mapping if it is
   stable, or fit a focus-dependent correction.
   - If both slit viewers have variable focus and the operating focus differs from nominal, update
     C03–C05 using correction factors or repeated measurements.

**Determines/checks.**

- Best slit-view focus and image-quality sensitivity around that setting.
- Centroid, plate-scale, and distortion changes with focus over the sampled field.
- Whether the existing coordinate model describes those changes adequately.

**Results.**

- Adopted focus setpoint and supporting focus curves for each viewer.
- Focus-dependent coordinate correction, where required, with residuals by field position.

**Repeat use.** Initially useful at different temperatures to determine or confirm temperature
drift. Repeat as desired for engineering verification.

(c07)=
### C07. Slit-selector reference offsets and optimal slit position

**Purpose.** Make each named slit selection return to its adopted optical operating position.

**Starting configuration.** Use the focused slit viewer and steering map from C04–C06, with steering
at home. Insert the point source and select suitable continuum or arc illumination for the
image-quality measurement.

**Operation flow.**

1. Calibrate the slit selector and position a slit at the nominal slit position.
2. Acquire the transmitted point-source image using the lamp-line images. Measure reflected light
   from the point-source overfill on the slit-view camera. Use extended illumination for any
   required aperture measurements, then restore the point source.
3. Determine an offset to the operating position to maximize flux through the slit.
4. Repeat for all slits.
5. Return to that setting from other selector positions to check repeatability, repeating in
   different orders as desired.
6. Update the slit registration and consider repeating impacted C08 samples.

**Determines/checks.**

- Mechanism set-point for each slit position.
- Transmission and image-quality dependence on selector adjustment.
- Placement repeatability on return from other selector positions.
- Dependence on move history or approach direction.

**Results.**

- Slit-position scatter.
- Return-offset distributions by move, including associated spectral residuals.
- Slit-selector setpoints and reference-offset table.
- Merit curves supporting each selected setting and the corresponding return residuals.

**Repeat use.** Repeat if input PSF symmetry materially changes or the relationship between the slit
and slit-view camera changes. Repeat as desired to monitor instrument stability.

(c08)=
### C08. Wavelength, PSF, and ZSpec vignetting response to point-source placement

**Purpose.** Support spectral extraction and observer decisions about recalibration after nodding or
switching between nearby sources.

**Starting configuration.** Insert the point-source mask, select the slit of interest, and use the
adopted focus and geometry from C03–C07. The calibration source is intended to provide a spot
suitable for the narrowest slit with a PSF representative of excellent seeing or seeing enhancement.
Image it slightly offset from the slit with the slit-view camera as the reference for this test.

**Operation flow.**

1. Acquire point-source arc spectra at the slit-center position.
2. Sample top and bottom positions along the slit and at transverse positions across the slit for
   slits where width/PSF EE80 (or thereabouts) is >1. Acquire the selected arcs at each position.
3. Fit line locations and two-dimensional detector profiles across the available wavelengths and
   sampled slit positions. Use the data to inform 2D PSF models, wavelength-calibration offsets, and
   guiding/ADC calibration effects.
4. With the point-source mask inserted, obtain continuum exposures at the sampled along-slit
   positions.
5. Revisit the initial position to check reproducibility. Be mindful of the repeatability of the
   slit positions from C05.

**Determines/checks.**

- Line location and detector PSF as functions of wavelength, along-slit position, and transverse
  source placement.
- Reproducibility of wavelength/profile changes with point source location or selector return.
- Continuum trace and illumination behavior at the two slit ends.

**Results.**

- Wavelength and PSF model over the three-dimensional sampling domain, with fit residuals.
   - Wavelength model: Legendre-polynomial correction terms relative to the slit-center
     Legendre-polynomial wavelength solution.
   - PSF model: eigenimages with coefficients modeled as functions of position and subpixel phase.
     Eigenimage construction must account for individual images’ subpixel phase in 2D.
- Accuracy guidance for source offsets and the circumstances in which an additional point-source arc
  is useful.

:::{container} zs-note-to-team zs-internal-only

**Review — C08.** Flesh out the vignetting measurements and EE80 sampling criterion with the team.
Assess whether continuum exposures at every along-slit position are excessive.

:::

**Repeat use.** Engineering maintenance only.

(c09)=
### C09. Internal point-source motion with rotator and ADC

**Purpose.** Preserve internal registration as rotator and ADC settings change, and provide
diagnostics for alignment.

**Starting configuration.** Insert calibration point source. Use the imager route for each ZImager
channel and the fully reflective slit-view configuration for each spectrograph. Fix steering to
reference home and use nominal focus settings.

**Operation flow.**

1. Measure the source with ADC and rotator mechanisms after a fresh actuator calibration and home.
   Use this as the reference state.
2. Capture an image series while rotating the ADCs through their full range of motion: at least 30
   images, roughly 12° apart.
3. Repeat with the rotators.
4. Fit centroids, check width stability, then fit the loop trajectory (sinusoidal epicycles, polar
   coordinates, etc.). Measure closure on return to the reference.
5. Collect combined rotator/ADC samples if the data indicate coupling or second-order effects.

**Determines/checks.**

- Apparent offset between the internal CAL launch point and each rotation center.
- Image displacement with rotator and ADC state, including any measurable coupling.
- Closure and image-quality changes over the cycle.

The trajectory combines the calibration point-source position and mechanism motion. C11/C12 and the
optical model provide the additional information needed to assign those contributions.

**Results.**

- Per-path trajectory fits and state-dependent registration corrections, with residuals.

**Repeat use.** Establishment during AIT. Repeats considered after mechanism servicing.

(c10)=
### C10. Telescope focus and relative instrument focus on sky

**Purpose.** Bring ZSpec and ZImager onto a common telescope-focus reference after installation.

**Starting configuration.** Laboratory measurements provide the detector-focus encoder relationships
and initial setpoints. The slit viewers have usable, characterized focus from C06. Acquire a
suitable star and complete the facility's normal telescope-focus procedure.

**Operation flow.**

1. Set the NIR slit viewer to its established internal focus and place the star on a visible
   reflective part of the slit plane.
2. Run a telescope-focus series around the initial setting, using the NIR slit-camera stellar image
   as the merit measurement. Hold the viewer focus fixed.
3. Record the NIR best focus. Under seeing enhancement, select the telescope defocus that matches
   the NIR EE80 to the Nyquist slit width; retain both the best-focus reference and adopted offset.
4. Retain that telescope reference and sweep the nominal ZImager focus to verify the nominal
   position in all three channels (one mechanism, three band optima, one broadband optimum).
5. Hold the adopted telescope setting and sweep the VIS/NIR relative focus. Select the VIS setting
   for slit coupling, balancing U-band losses against R-band gains; record the wavelength-dependent
   focus curves.
6. Obtain additional series at naturally occurring temperatures. Use them as needed and compare with
   available design predictions.

**Determines/checks.**

- NIR best focus and the telescope defocus needed to match EE80 to the Nyquist slit width.
- Nominal ZImager focus and VIS/NIR relative-focus setting at that telescope reference.
- Agreement with the predicted temperature dependence as focus series accumulate.

**Results.**

- Telescope, imager, and relative-focus settings.
- Focus curves indexed by temperature and observing/enhancement conditions, usable for broadband or
  wavelength-specific focus optimization.
- Performance gain available with chromatic focus optimization, principally ZSpec U vs R and ZImager
  U vs ZImager others.

**Repeat use.** Initially repeat after reinstallation of ZSpec NIR or ZSpec, and repeat the relevant
part after ZImager reinstallation. Once stability is established, use an as-needed engineering check
or repeat when anomalous image quality appears. Build temperature coverage as conditions change.

(c11)=
### C11. On-sky registration of the internal reference and facility guider

**Purpose.** Make the facility guide reference deliver a sky target to internal instrument
coordinates. Off-axis scale, orientation, and angular dependence are measured in C12/C13.

**Starting configuration.** Use a star with good Gaia astrometry at low airmass; a suitable
spectrophotometric standard is also useful for other calibrations. Apply system focus and internal
calibrations/zeros (slit, steering, rotator, and ADC). Record the facility guider's existing
calibration and reference state.

**Operation flow.**

1. Acquire a guide star and place the star on the nominal RNAS port axis (boresight/nominal
   instrument axis) and measure it in the imager channels.
2. Switch to the spectrograph route and measure the star in both slit viewers, using a fully
   reflective position if necessary.
3. Compute the telescope offset necessary to place the star at the calibration point-source
   reference, accounting for the current rotator, ADC, focus, and steering states.
4. Shift the guide target to guide the telescope until the star reaches the internal-source
   reference.
5. Determine the change from the existing facility guide reference and apply it through the agreed
   reference convention as ZShooter's internal reference location.
   - This establishes a common zero point, which may be off-axis. The science guide position is
     selected for the observation.
6. Reacquire the guide and verify the predicted positions on ZImager or the ZSpec VIS slit viewer.
7. Use this central measurement as the reference for C12 and the independent comparison in C13.

**Determines/checks.**

- Registration of the sky source to the internal-source reference in each ZImager and each slit-view
  camera.
- Guide-reference adjustment required for the chosen instrument placement.
- Closure of the predicted positions when switching between ZImager/ZSpec.

**Results.**

- Central sky-to-instrument registration and K1 guide-reference offset.
- Per-camera verification residuals forming the reference for C12/C13.

**Repeat use.** Repeat each time ZShooter or any component is reinstalled. Repeat as needed when
guider is calibrated.

(c12)=
### C12. Off-axis rotator behavior and on-sky ADC verification

**Purpose.** Support accurate acquisition across the useful field and airmass range of observing.

**Starting configuration.** Begin with the low-airmass reference from C11. Use the established
rotator and ADC models and record the state of telescope guiding throughout the sequence.

**Operation flow.**

1. Offset the telescope to place the source at the four corners of a box spanning the intended
   spectrograph steering field. Measure its actual camera positions. (i.e. (+7, -3), (-7, +3), ...
   if the final field were 14 × 6 arcsec).
2. At each position, run the VIS and NIR field rotators through their full range. Follow the source
   with the fully reflective slit-view configuration.
3. Stop field-rotation tracking and hold the instrument rotators fixed while telescope sidereal
   tracking continues. Let the target trace an arc to find the field-rotation center; a target
   nearer the zenith is useful. Resume field-rotation tracking afterward.
4. Compare the paths with the model predictions.
5. Revisit the central reference during the sequence to measure closure and accumulated changes.
6. For ZImager, place the source near the largest circle within the usable rotating detector field.
   Run the rotator through its full range, measure each channel’s path and compare it with the
   camera model.
7. **Commissioning ADC check:** Run each ADC through its travel to measure image motion and identify
   field-position- or airmass-dependent offsets. Gather data for ZImager, ZSpec VIS, and ZSpec NIR.
8. Repeat the ADC measurements at higher airmasses.
9. Fit the on-sky residuals and compare them with C09 to identify additional field-dependent terms.

**Determines/checks.**

- Off-axis scale and orientation, rotator image-angle law and zero point, and residual field
  distortion.
- Image translation and chromatic image-quality changes with ADC state and airmass.
- Additional field-dependent terms needed beyond the internal-source model from C09.

**Results.**

- Field/rotation registration solution with residual maps over the sampled positions and angles.
- ADC performance curves or correction tables over the measured wavelength and airmass range.

**Repeat use.** Establish the behavior with the full field and high-airmass sequences. Repeat only
as needed for engineering monitoring.

(c13)=
### C13. Independent guider/slit-view astrometry and plate-scale comparison

**Purpose.** Provide an independent astrometric test of acquisition and telescope-offset
predictions.

**Starting configuration.** Select a pair of astrometric standards with one star near the instrument
axis and the other in the usable guider field at the chosen guider orientation. Ideal fields would
offer several visible stars (>4, to support astrometry.net) with Gaia astrometry in both fields and
with the primary guider star at least 15" from the guider-field edge. Remember your epoch!

**Operation flow.**

1. Slew to the field and place the guide star such that the companion should be on-axis.
2. Predict the central star’s slit-view position from the guider measurement, the pair’s relative
   astrometry, and the coordinate model. Measure the companion’s offset.
3. Move the telescope via the guider to place the field at each of the four corners of the steerable
   field.
4. Measure field positions in the guider and slit viewers. In a rich field, also measure the
   surrounding field shift on ZImager. Compare prediction and measurement in both slit-view cameras.

**Determines/checks.**

- Agreement between the measured slit-view position and the position predicted from guider/slit view
  measurements and stellar relative astrometry in both directions.
- Scale, direction, and cross-axis response of telescope offsets expressed in slit-view coordinates.

**Results.**

- Prediction-versus-measurement comparison with an uncertainty budget from the stellar astrometry
  and camera measurements.
- Measured telescope-offset response in both coordinate systems.

**Repeat use.** Rarely, when guider or instrument changes invalidate the plate scales or
axis-translation model. Reinstallation is intended to update the model’s zero points.

(c14)=
### C14. Guider runout with simultaneous guider and slit-view stars

**Purpose.** Calibrate guider-angle errors that could move the target away from its requested slit
position. Continues from C13. C15 provides an alternative field strategy.

**Starting configuration.** Use a suitable two-star field from C13. Place one star at the slit
reference or a nearby visible slit-view position and the other on the guider. Select a sequence of
guider positions/angles that keeps the guide star measurable. Hold or explicitly model the
instrument rotator, ADC, and steering states.

**Operation flow.**

1. Acquire simultaneous guider and slit-view reference measurements.
2. Move the guider to the next position/angle while guiding continues, if MAGIQ supports this.
   Otherwise, move the guider and then guide the telescope back into position, using measurements
   after guiding is restored. Record any guide-offset/correction changes.
3. Compare the guide star with its predicted position, using the slit-view star as an independent
   cross-check to search for uncorrected telescope motion.
4. Repeat over the accessible arc and return to a reference angle.
5. Use additional fields or placements to cover the required guider angles.
6. Fit the angle-dependent residual, beginning with the whitepaper’s constant plus sine/cosine
   terms. Examine residuals on independent arcs before extending the fit.

**Determines/checks.**

- Repeatable angle-dependent registration error after accounting for telescope motion with the
  simultaneous slit-view reference.
- Return consistency and prediction accuracy on independent arcs.

**Results.**

- Effective guider-angle correction and its fit/validation residuals.
- Time-aligned guider/slit-view trajectories where available, or settled-position measurement sets.

:::{container} zs-note-to-team zs-internal-only

**Review — C14.** Develop the sequence with Keck and the team around MAGIQ’s supported behavior.
Assigning the fitted error to bearing runout, axis decenter, or optical distortion requires
additional constraints.

:::

**Repeat use.** After guider rotator or camera track surgery.

(c15)=
### C15. Guider runout by repeated transfer of one source

**Purpose.** Provide guider-angle calibration evidence from fields that lack the simultaneous star
pair required by C14. Adoption as a substitute for C14 depends on separating time-dependent tracking
error from angle-dependent guider motion.

**Starting configuration.** Select a source near enough to the zenith to provide useful angular
evolution within a short duration. Use transfer geometry from C11–C13. Hold the instrument image
rotator at a recorded fixed angle for the proposed sequence and account for the resulting field
rotation.

**Operation flow.**

1. Measure the source at its initial guider placement.
2. Offset the telescope to the slit-view field and measure the source against the calibrated
   reference.
3. Offset back to the guider and measure closure. Preserve timing and commanded offsets for both
   transfer legs.
4. Repeat the transfer cycle at successive guider angles.
5. Use a second slit-view star, when present, to check telescope motion and field evolution.
6. Analyze the transfer residuals with the telescope offset/tracking uncertainty. Compare their
   angle dependence with C14 or the current guider model.

**Determines/checks.**

- Transfer residual as a function of guider angle.
- Round-trip repeatability and the contribution of telescope offset/tracking errors.
- Whether the transfer uncertainty permits a useful guider-angle correction.

**Results.**

- Angle-indexed transfer residuals, closure measurements, and uncertainties.
- Comparison with C14 or the existing guider model where available.

**Repeat use.** Same as C14.

## Acquisition and observing flows

(a01)=
### A01. ZSpec acquisition and slit-view guiding refinement

**Purpose.** Place a target at the requested slit position and maintain that placement during
observing.

**Starting configuration.** Select the slit and position angle, and send the field center,
orientation, calibrations, and target/guide-star astrometry to the instrument. Focus, ADC state,
pupil rotator, and steering use their automatic defaults.

Ongoing slit-view refinement requires an independent source with good relative astrometry to the
target. A single source centroid supplies two constraints. Allocating its motion among X/Y steering
and rotation requires additional spatial/temporal information or a defined control constraint.

**Operation flow.**

1. Use MAGIQ/facility planning to select a guider orientation and guide star, then slew to the
   target.
2. Set the guide reference to place the target on the instrument axis, including any guider-modeled
   evolution during tracking.
3. Measure target overfill or suitable field sources in each slit viewer and determine any placement
   error.
4. Apply the appropriate acquisition case:
   - Within the calibrated internal correction range, apply the steering correction. Alert the
     operator to a guiding error if the correction is large.
   - For an off-scale correction, report an error and alert the operator to fix guiding.
   - With no visible reference, accept the guider-predicted placement.
5. Begin observing.
6. Where an independent slit-view reference is available, measure it periodically during the
   exposure. Use residuals and the coordinate model to derive slow X/Y steering and constrained
   ZSpec rotator corrections.
7. Track the accumulated correction. Request a guider correction when the coordinate model indicates
   it is merited, and alert the operator if the correction signal leaves the established operating
   region.
8. After a facility correction, unwind the accumulated internal correction.

**Determines/checks.**

- Acquisition position and correction applied in each arm.
- Residual slit-plane translation and any independently constrained rotation error.
- Growth of steering/rotator correction (wind-up) and remaining calibrated range.

**Archived telemetry.**

- Field acquisition solution: guide reference, applied telescope/steering offsets, final placement
  residuals, and full mechanism-calibration parameter values.
- Time series of source-position residuals and applied steering/rotator corrections.

(a02)=
### A02. Classical sky/source nods

**Purpose.** Move between requested nod positions or nearby sources during an observing sequence.

**Starting configuration.** Begin from an acquired field with the slit, steering map, and C08
response model identified. Express the requested offsets either relative to target or between
positions in the slit-view camera frame.

**Operation flow.**

1. Convert the requested offsets into steering positions using the pointing and coordinate model or
   the pair of pointings.
2. Check that each position lies within the calibrated range and evaluate its spectral consequences
   with C08. The observer decides whether the spectral dependence merits additional arcs.
3. Where slit-view guiding is active, set its target to the new nod position. Command the steering
   move.
4. Verify placement with available slit-view sources, then execute the associated exposure or dwell.
5. Continue the pattern.

**Determines/checks.**

- Achieved displacement or position error.
- Applicability of the C08 wavelength/PSF model at the requested positions.

**Archived telemetry.**

- Exposure-associated nod record containing applied positions and measured placement errors.

(a03)=
### A03. Blind acquisition using a guide star transferred to the slit viewer

**Purpose.** Acquire an invisible target when the science field contains no measurable slit-view
reference.

**Starting configuration.** Select the desired slit. Use known relative astrometry between the
target and guide star and the calibrated telescope/guider-to-slit-view mapping. Establish the
nominal field with facility guiding.

**Operation flow.**

1. Acquire with the guider so that the target should be on the slit.
2. Pause guiding or switch guide stars as needed, then offset the telescope to place the guide star
   beside the slit.
3. Use the reference-star measurement and coordinate model to determine and apply the internal
   fine-steering correction.
4. Undo the temporary telescope offset and restore the science guide configuration, retaining the
   internal steering correction.
5. Observe.

**Determines/checks.**

- Acquisition-specific internal steering correction inferred from the transferred reference star.

**Archived telemetry.**

- Reference-star transfer measurements and the applied internal steering correction.
- Inferred target position and uncertainty at the final science configuration.

(a04)=
### A04. Blind acquisition with a reference source in the slit-view field

**Purpose.** Acquire an invisible target using a measurable reference source in the same slit-view
field.

**Starting configuration.** Select the science slit and supply the target/reference relative
astrometry and the reference-source astrometry. Acquire the field with the facility guider so that
the reference is beside the slit, roughly one PSF width to either side.

**Operation flow.**

1. Identify and measure the reference source.
2. Use the coordinate model to compute an internal steering correction or request a
   telescope/guide-reference correction.
3. Remeasure the reference for confirmation.
4. Begin observing and use the reference for subsequent refinement.

**Determines/checks.**

- Remaining placement error and uncertainty after the correction.

**Archived telemetry.**

- Acquisition solution linking the reference-star centroid, relative astrometry, applied
  corrections, and inferred target position.

:::{container} zs-internal-only

## Questions

| Topic                                       | Questions                                                                                                                                                                                                |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Illumination and flats, C01/C02             | What measurements separate the large-scale illumination pattern from detector response, and what precision is needed for the intended use? Which source combinations and signal levels are sufficient?   |
| Initial registration, C03–C07               | Which laboratory products provide the starting scale, orientation, focus, and slit positions? After the final focus/selector settings are chosen, which measurements need repeating or refitting?        |
| Steering coverage, C04/C08                  | Is a nine-point grid enough? Which additional positions distinguish nonlinearity, direction dependence, and return error?                                                                                |
| Focus hierarchy, C06/C10                    | Which internal settings remain fixed during the telescope-focus series? How will the image-quality merit be evaluated across the VIS channels?                                                           |
| Slit setting, C05/C07                       | Which geometric or spectral measure defines the adopted optimum position?                                                                                                                                |
| Source sampling and vignetting, C08         | Does the source image adequately sample the narrowest slit and detector PSF? Settle the along-/across-slit sampling, EE80 criterion, vignetting measurement, and useful continuum exposures.             |
| Registration stability, C02/C03/C07/C08/C09 | Which return cycles and angular states are sensitive enough for a short verification? Which configuration changes require a new calibration or a targeted check?                                         |
| On-sky geometry, C11/C12                    | Which measurements distinguish internal launch decenter, telescope/instrument registration, rotator motion, and field distortion? What independent field information is needed to fit the chosen model?  |
| ADC verification, C09/C12                   | Which wavelength-resolved or multi-band measurements distinguish chromatic residuals from image translation, and what airmass/ADC sampling covers the intended observations?                             |
| Guider runout, C13–C15                      | Can the available field/angle coverage distinguish mechanical runout, axis decenter, and guider distortion? What tracking and offset uncertainty can the single-source transfer tolerate?                |
| Guiding refinement, A01                     | What measured residual and remaining steering range trigger a facility correction? Which data constrain a rotator correction, and how, if at all, are the facility and internal corrections coordinated? |
| Blind placement, A03/A04                    | How does the uncertainty from catalog offsets, differential refraction, field mapping, and transfer closure compare with the required placement accuracy?                                                |
| Additional operating cases                  | Do non-sidereal acquisitions, extended sources, or special slit placements require extra steps beyond these flows?                                                                                       |

The final verification recipes should specify the retained subset, its expected residuals, and the
action taken when a check disagrees with the existing calibration. That decision can then be traced
to a measured change and to the observing capability it affects.

:::
