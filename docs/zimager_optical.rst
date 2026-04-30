ZImager
=======

ZImager is the imaging half of ZShooter and should be treated as a science instrument, not merely as an acquisition
camera.  It provides simultaneous multi-band context for targets being sent to ZSpec, fast photometric observations
when spectra are secondary or impossible, and millisecond-class time-domain capability for compact binaries,
occultations, pulsations, accretion flickering, and other rapid optical phenomena.  Its project value is high
because it adds these capabilities with comparatively modest incremental optical complexity once ZShooter already
has the RNAS location, software infrastructure, calibration strategy, and detector/readout support.

The ZImager concept is less mature than ZSpec because it was added later in the conceptual phase and because it can
draw directly on two near-term pathfinders: proto-Lightspeed/Lightspeed at Magellan and Cerberus at Palomar.  That is a
design advantage, not an excuse for deferral.  The preliminary-design task is to turn the present concept into a clean
optical prescription with a frozen field, filter set, data-rate envelope, WCS model, and ZSpec cross-calibration strategy.

.. container:: zs-placeholder zs-internal-only

   **Figure placeholders**

   - ZImager optical layout from Zemax.
   - Spot and EE maps for the u, selectable, and z channels.
   - Distortion/WCS map over the selected field.
   - Dichroic/filter bandpass plot with nominal science filters.
   - Mechanical concept for three independently rotating detector heads.

Design Requirements
-------------------

ZImager has four principal roles:

- provide tri-band imaging for target identification, field verification, host association, and local environment characterization;
- provide contemporaneous or near-contemporaneous photometric anchoring for ZSpec spectra;
- provide a fallback science product when a transient is too faint for a useful spectrum; and
- provide high-cadence, low-noise imaging for compact and rapidly variable sources.

These roles drive the optical design differently.  Acquisition and context prefer field of view.  Spectrophotometric
anchoring prefers stable standard filters, controllable color terms, and accurate WCS.  High-cadence science prefers
high frame rate, windowed readout, low noise, and manageable data volume.  AO/seeing-enhanced use prefers fine enough
sampling that the improved delivered image quality is not squandered at the detector.

The present requirement-level intent is simultaneous imaging in at least three bands over enough field to support
relative photometry across most of the observable sky.  The CDR concept uses a ∼3 arcmin field.  Current notes leave
the final field as a 1–3 arcmin trade; the optical design should keep the CDR value as the science-preferred target
until the data-rate and packaging trades force a smaller first-light field.

.. container:: zs-note-to-team zs-internal-only

   Freeze the ZImager field requirement explicitly.  The current text contains both “∼3 arcmin” and “1–3 arcmin”
   language.  The optical team needs one baseline field and one descoped field for sensitivity/data-rate/packaging analysis.

Current Optical Concept
-----------------------

The baseline concept uses a refractive collimator that accepts the ZImager field from ZFront.  A dichroic tree
separates the collimated beam into three channels.  The first split is expected to isolate the u-band channel, the
second split separates the red/z-like channel from the selectable middle channel, and the longest-wavelength optical
channel can be folded as needed for packaging.  Each channel then uses a fast camera to focus the image onto an O
RCA-Quest-class qCMOS detector.

The current CDR design point is an f/1.2 camera delivering 17.2 arcsec/mm, corresponding to about 0.079 arcsec/pixel
for a 4.6 µm ORCA-Quest pixel.  This pixel scale oversamples normal seeing and is also credible for future
seeing-enhanced operation.  The price is data rate.  ZImager should therefore be specified with multiple readout modes
rather than a single “full field at high cadence” mode.

.. list-table:: ZImager optical concept
   :header-rows: 1
   :widths: 24 76

   * - Item
     - Current design intent
   * - Optical form
     - Refractive collimator followed by dichroic splits and one fast camera per channel.
   * - Field of view
     - Science-preferred target ∼3 arcmin; current trade range 1–3 arcmin.
   * - Channels
     - Three simultaneous bands: u, selectable middle band, and z-like red channel.
   * - Detector class
     - Hamamatsu ORCA-Quest 2-class qCMOS modules, one per channel.
   * - Pixel scale
     - CDR value ≈0.079 arcsec/pixel for 4.6 µm pixels at 17.2 arcsec/mm.
   * - Camera speed
     - CDR value f/1.2; faster options are tied to future detector formats and data-rate trades.
   * - Field derotation
     - Current concept rotates the individual detector heads on compact rotation stages.
   * - Filter strategy
     - Fixed u and z-like channels; selectable middle channel with standard broadband and possibly narrow-band filters.

Filter and Channel Strategy
---------------------------

The nominal channel concept is u / variable / z.  The u channel is valuable because many ZShooter science cases are
blue at early times or have diagnostic leverage near the atmospheric cutoff.  The z-like channel is valuable for
reddening transients, field calibration, and high-cadence color leverage.  The middle channel should carry the most
frequently useful standard broadband option, likely g or r depending on final science prioritization, plus a small
number of filter slots for special programs.

Narrow-band filters near 1 nm bandwidth have been discussed for targeted science cases.  They should remain possible,
but the baseline optical design should not be optimized around them unless a science case establishes enough demand.
Narrow filters impose stronger requirements on filter tilt, wavelength shift across the field, pupil telecentricity, and calibration.

.. container:: zs-note-to-team zs-internal-only

   Define the middle-channel baseline filter set before PDR.  At minimum decide whether g, r, or a multi-slot broadband s
   et is the required first-light configuration, and whether 1 nm filters are a requirement, an accommodation, or a future option.`

Image Quality and Sampling
--------------------------

The imager should sample the delivered image under both natural and seeing-enhanced conditions.  A reasonable working
target is that the optical design not degrade a 0.25 arcsec delivered PSF over the science field by more than the
adopted DIQ budget.  At the current 0.079 arcsec/pixel sampling, a 0.25 arcsec FWHM image spans about three pixels,
which is appropriate for PSF-fitting, difference imaging, and WCS/astrometry without imposing extreme undersampling.

The optical design should track at least four image-quality products during preliminary design:

- spot and encircled-energy maps over field and wavelength for each channel;
- distortion and differential distortion maps for WCS and co-registration;
- chromatic PSF and focus behavior across each filter bandpass; and
- pupil/ghost behavior from dichroics, filters, detector windows, and fast-camera surfaces.

ZImager does not need diffraction-limited optics, but it does need predictable optics.  Its value as a calibration and
acquisition tool depends on reliable coordinate transformations, stable PSFs, and well-characterized color terms.

Detector and Readout Basis
--------------------------

The baseline detector module is ORCA-Quest 2-class qCMOS.  This class of detector has sub-electron read noise and
photon-number-resolving modes, making it well suited to fast, low-light astronomical imaging.  The CDR detector table
lists a 2k × 4k, 4.6 µm format, approximately 0.25 e− read noise, 21.6 e−/hour dark current, 7 ke− well depth,
∼85% QE, and 8 ms readout time.

Operationally, the detector choice should be translated into a small number of modes:

.. list-table:: Suggested readout-mode framing
   :header-rows: 1
   :widths: 24 36 40

   * - Mode
     - Use
     - Optical/readout implication
   * - Full-field imaging
     - Acquisition support, context, photometric anchoring, faint fallback imaging.
     - Prioritize calibrated field, low distortion, stable filters, and manageable exposure/readout cadence.
   * - Windowed high cadence
     - Compact binaries, eclipses, occultations, pulsars, rapid flares.
     - Use subrasters to reach millisecond-to-second cadence without full-field data rates.
   * - Calibration/WCS mode
     - Field registration, cross-calibration, focus checks.
     - Use standard exposure sequences and repeatable detector orientation metadata.
   * - Engineering mode
     - Detector characterization, non-linearity checks, persistence/offset behavior, timing validation.
     - Allow non-science frame formats and diagnostic metadata.

.. container:: zs-note-to-team zs-internal-only

   A likely ORCA-Quest 3 or larger-format successor would change the ZImager trade space by allowing a slower camera
   for a given field size while increasing an already significant data rate.

Field Derotation
----------------

The current concept derotates the field by rotating the three compact detector heads independently.  This is attractive
because it avoids a large upstream optical derotator in the imager path and takes advantage of the small detector
packages.  The consequence is that each channel has its own detector angle, cable wrap, and WCS state.  That is
acceptable if the software model is explicit and the rotation stages are repeatable.

The alternative is to derotate the full imager field optically before the dichroics.  That could simplify WCS but
would add optical/mechanical complexity and might compete with the ZFront/ZSpec path.  At this stage, independent
detector rotation remains the sensible baseline, but it must be evaluated against cable routing, flexure, calibration
repeatability, and high-cadence operations.

Cross-calibration with ZSpec
----------------------------

ZImager should help ZSpec in three ways.  First, it provides photometric anchoring close in time to the spectrum,
reducing the burden on cross-arm spectrophotometric calibration.  Second, it helps establish target location and local
field context before the target is placed on the slit.  Third, it supports ZSpec/ZImager co-alignment checks through
shared calibration and on-sky fields.

ZFront enables a common central calibration field, nominally 20–30 arcsec, that can be sent through the ZImager and
ZSpec paths.  A uniform-field mode is useful for flat-field and response checks; a pinhole/point-source mode would be
useful for centroid, distortion, and co-alignment checks.  On sky, spectrophotometric standards and field stars
complete the calibration chain.

The optical and software teams should jointly define a calibration product that states, for every science exposure or visit:

- the ZImager WCS and distortion solution;
- the transformation from ZImager field coordinates to the ZSpec slit coordinate system;
- the filter and color-term calibration used for synthetic photometry;
- the time offset between image and spectrum;
- the ZFront selector state and any calibration-path identifiers.

Open Design Trades
------------------

.. container:: zs-note-to-team zs-internal-only

   **Trades requiring disposition before a stable PDR baseline**

   - ZImager field of view: freeze the field requirement after Science Team input on topics such as photometric calibration star
     density and acquisition/environmental value and engineering team considerations such as readout/data rate and optical difficulty.


   - Field of view: choose the baseline and descoped values, with data volume, photometric-star density, optical envelope, and acquisition value explicitly compared.
   - Camera speed and pixel scale: confirm f/1.2 and 0.079 arcsec/pixel, or revise them in response to the final detector model and AO/DIQ assumptions.
   - Detector derotation: confirm independent rotating detector heads versus an upstream field derotator; include cable-wrap, WCS, flexure, and failure-mode implications.
   - Filter list: select first-light middle-channel filters and decide whether narrow-band filters are required or merely accommodated.
   - Dichroic transitions: set channel boundaries so that u and z science are protected while the selectable channel remains useful for common photometric anchoring.
   - Data-rate envelope: specify sustained and peak rates for full-field and subraster operation; this must feed directly into detector-server, compression, storage, and DRP design.
   - Co-alignment calibration: decide whether a pinhole/point-source calibration mode is required in ZFront for ZImager/ZSpec alignment validation.



External Technical Context
--------------------------

The current detector-facing concept is informed by Hamamatsu ORCA-Quest qCMOS performance documentation and by the
proto-Lightspeed pathfinder on the Magellan Clay telescope.  The proto-Lightspeed paper is particularly relevant
because it demonstrates a low-read-noise, high-speed astronomical imager built around the ORCA-Quest 2 detector class
and motivates the same class of fast compact-binary, occultation, and accretion-variability science that ZImager is
intended to support.  ZImager differs in being integrated with a simultaneous broad-band spectrograph and in using
three co-aligned channels as part of a facility-style Keck instrument.

Useful starting references:

- `Hamamatsu ORCA-Quest qCMOS technical note <https://camera.hamamatsu.com/content/dam/hamamatsu-photonics/sites/documents/99_SALES_LIBRARY/sys/SCAS0154E_C15550-20UP_tec.pdf>`__.
- `proto-Lightspeed: a high-speed, ultra-low read noise imager on the Magellan Clay Telescope <https://arxiv.org/abs/2601.16268>`__.
