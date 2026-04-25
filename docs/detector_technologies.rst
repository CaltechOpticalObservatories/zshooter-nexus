Detector Technologies
=====================


.. container:: zs-lead

   ZShooter is leaning into cutting edge detector advances where detector properties enables new observing models, while
   keeping practical fallback paths. The detector choices are not decorative upgrades: they determine how well ZShooter
   can trade cadence, read noise, and spectral resolution without making the instrument itself the bottleneck.

Detector Baseline
-----------------

The baseline detector architecture follows directly from the instrument concept: visible ZSpec channels are designed
around low-noise qCCDs with spatially varying anti-reflection coatings, the infrared channels are designed around
linear-mode avalanche photodiode arrays, and ZImager uses qCMOS detectors modules for fast, low-noise, simultaneous
tri-band imaging. The fallback strategy is conservative: conventional CCDs and H2RG-family infrared arrays can preserve
the basic instrument function, while only sacrificing some of the full cadence/noise/dark current advantages.

.. list-table:: Detector technology summary
   :header-rows: 1
   :widths: 20 26 24 30

   * - Subsystem
     - Baseline
     - Fallback / alternate
     - Why it matters
   * - ZSpec optical
     - qCCDs with tapered ALD AR coatings
     - Conventional STA or Teledyne-e2v CCDs
     - Sub-electron effective read noise makes short sub-exposures, post-facto binning, sky-line editing, and high native resolving power scientifically useful rather than read-noise dominated.
   * - ZSpec IR
     - Low-noise HgCdTe LmAPDs, one 2k × 2k-class array per YJ/H/K channel
     - H2RG or H4RG-family HgCdTe arrays
     - Much of the IR band is detector-noise limited between OH lines. LmAPD avalanche gain reduces the read-noise penalty before multiplexor/readout noise is added.
   * - ZImager
     - ORCA-Quest 2-class qCMOS cameras, final model TBD
     - N/A, detectors in use and commercially available
     - Near-quantizing performance, an electronic shutter, and high frame-rate subrasters support acquisition, photometric anchoring, occultations, and compact-binary timing.

Spectral Channels
-----------------

The post-concept-review optical prescription update moves ZSpec toward two spectrometers, each split into three
channels and each formatted onto a 2k × 2k active detector area. The active detector format is deliberately technology
agnostic: it can be satisfied by available detector classes and by the likely formats of the qCCDs and LmAPDs ZShooter
intends to field.

.. list-table:: Post-concept-review channel coverage
   :header-rows: 1
   :widths: 18 22 38

   * - Spectrometer
     - Channel
     - Detector implication
   * - Visible
     - Blue
     - Optimized for the atmospheric blue cutoff, qCCD coating and blue QE matter disproportionately.
   * - Visible
     - Green
     - Separates the highest-throughput visible region from the blue and red channels, improving cross-disperser efficiency relative to the older two-visible-channel split.
   * - Visible
     - Red
     - Covers the red optical arm on a 2k × 2k active format and supports red-sensitive bulk qCCD material.
   * - Infrared
     - YJ
     - 2k × 2k LmAPD target format; no detector mosaic required
   * - Infrared
     - H
     - Improves efficiency balance and somewhat isolates high-sky-background regime design trades.
   * - Infrared
     - K
     - Preserves K-band science while making thermal background, detector dark current, and telescope impacts tightly contained in one channel.

qCCDs & Tapered Coatings
------------------------

A qCCD is a CCD operated with a skipper-style nondestructive readout architecture: the same pixel charge packet can be
sampled repeatedly before it is finally cleared. If the samples are sufficiently independent, the effective read noise falls
approximately as the square root of the number of samples. The result is not merely a lower-noise CCD; it is a detector
that can approach direct charge quantization for optical photons while retaining CCD strengths such as high QE,
large-area formats, linearity, and on-chip binning.

The optical spectrograph is intentionally high-resolution for a broad set of science
cases, but many programs want to synthesize lower resolution after the fact. With ordinary CCD read noise, collecting a
spectrum at high native resolution and then rebinning it is not equivalent to observing directly at lower resolution: the
read-noise contribution has already been paid in too many pixels. qCCDs change that trade. They let ZShooter collect
more spectral information at the detector and defer some of the resolution/SNR decision into the reduction, where sky
lines, cosmic rays, and science-specific line windows can be handled more intelligently.

For the current ZShooter concept, the optical detector path has three separate pieces:

* **Differential skipper readout.** Differential sampling of the signal and reference levels reduces the speed-noise
  penalty relative to earlier skipper implementations.
* **Many parallel outputs.** Segmenting the serial register into many outputs keeps the readout time compatible with
  observational use rather than particle-physics-style integrations.
* **Frame-transfer operation.** A frame store hides much of the readout overhead, preserving open-shutter efficiency even
  when the instrument is taking many short sub-exposures.

The STA5500 is an available fallback qCCD and the upcoming STA5900 qCCD is our preferred path. The STA5500 already has
better performance than a conventional CCD, with a 4096 × 2048 image area (w/ matching frame store),
and 1 e⁻ read noise in roughly 13 s. STA5900 is the target faster device, with 1 e⁻ read
noise in roughly 2.8 s, and charge quantization in about 120 s, with both bulk red-sensitive and epitaxial
blue-optimized versions.

Tapered AR Coatings
~~~~~~~~~~~~~~~~~~~

The qCCD coating concept further improves ZShooter's optical grasp. In a fixed-format spectrograph, each detector location
corresponds to a predictable wavelength range. A spatially varying anti-reflection coating can therefore be tuned to the
local incident wavelength rather than forcing one coating stack to serve the entire channel uniformly.

The practical goal is simple: keep reflectance below the percent level across the relevant detector format. Since silicon
charge collection is effectively complete when the photon is absorbed in the active volume, lowering reflectance directly
improves QE. It also suppresses ghosting, fringing, and broad-band scattered-light coupling from wavelengths that do not
belong at a given detector location.

.. list-table:: Visible qCCD coating concept
   :header-rows: 1
   :widths: 20 28 28 24

   * - Channel
     - Coating gradient
     - Coating bandwidth
     - Stray-light suppression note
   * - ZSpec Blue
     - Tapered ALD stack ~3.5 nm/mm with 365 nm midpoint
     - full channel span is 110 nm, instantaneous coating bandwidth :zs-check:`TODO`
     - Early estimates suggest ~ :zs-check:`TBD%` reduction in spectrally broad scattered light
   * - ZSpec Green
     - Tapered ALD stack, ~6.5 nm/mm with 500 nm midpoint
     - full channel span is 200 nm, instantaneous coating bandwidth :zs-check:`TODO`
     - Early estimates suggest ~ :zs-check:`TBD%` reduction in spectrally broad scattered light
   * - ZSpec Red
     - Tapered ALD stack, ~13 nm/mm with 780 nm midpoint
     - full channel span is 400 nm, instantaneous coating bandwidth :zs-check:`TODO`
     - Red performance also depends on bulk silicon thickness, fringing, and dark current

Early explorations use a graded graded Al₂O₃ layer bounded by HfO₂ and fabricated by
atomic layer deposition. The appeal of ALD is process control: thickness can be refined cycle-by-cycle, the approach is
compatible with detector-sized substrates, and the coating can be tuned to the cross-dispersed format. The remaining
engineering issue is calibration and repeatability whenever the material set or process changes.

qCCD Science and Operations Implications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 26 37 37

   * - Capability
     - Detector reason
     - ZShooter observing consequence
   * - Short-exposure coadds
     - Read noise no longer dominates each short exposure.
     - Better cosmic-ray rejection in thick devices; real-time SNR assessment; less penalty for splitting exposures around changing conditions.
   * - High native resolution with later binning
     - Read noise remains small even before digital binning.
     - Observers can preserve line information, then bin around sky features or science windows in the DRP.
   * - Digital sky suppression
     - High native sampling plus low read noise makes contaminated spectral pixels less expensive.
     - OH-affected bins can be down-weighted or removed before rebinning to science resolution.
   * - Self-calibration
     - Charge quantization exposes integer-electron peaks in image histograms.
     - Conversion gain, zero signal, linearity, serial CIC, and some brighter-fatter diagnostics can be inferred from science or calibration images.
   * - AO and image-slicer compatibility
     - Oversampling the PSF does not automatically impose a read-noise catastrophe.
     - Optical architectures that collect light into more pixels become more plausible.

CCD Fallback
~~~~~~~~~~~~

The conventional CCD fallback preserves wavelength coverage and basic spectroscopic function. It does not fully preserve the
same observing model. Internal performance slides summarize the expected loss from conventional CCDs as roughly
0.2–0.4 mag. We believe this is still an acceptable fallback because the instrument remains a broad-band,
high-throughput optical–IR spectrograph that remains at least as performant as existing instruments.

LmAPDs
------

ZShooter's infrared baseline is a set of linear-mode HgCdTe avalanche photodiode arrays. In linear mode, the detector is
used as an integrating array, but photoelectrons are multiplied by avalanche gain before the readout noise of the ROIC is
added. This is the central difference from ordinary HxRG-style operation: the signal is amplified before the dominant read
noise source enters the measurement.

Leonardo describes Saphira-family HgCdTe APDs as variable-gain detectors for 0.8–2.5 µm operation,
with flexible windowing and high-speed readout. The Mike Bottom and the University of Hawaiʻi and UC Berkeley have
partnered with Leonardo on a development program that has pushed the technology toward larger, lower-glow,
lower-dark-current astronomy arrays. Recent work on LmAPDs reports newer devices with that employ a modified pixel
structure to reduce ROIC glow, with measured glow around 0.012 e⁻ pixel⁻¹ frame⁻¹ and very low intrinsic dark current
in the relevant low-background tests.

For ZShooter, the current detector target is a 2k × 2k, 15 µm-pixel LmAPD. The project assumption is that one array
can serve each IR channel: YJ, H, and K, a much cleaner path than the earlier conceptual design mosaic that required
three-side-buttable LmAPDs.

.. list-table:: ZSpec IR detector assumptions
   :header-rows: 1
   :widths: 20 28 24 28

   * - Parameter
     - LmAPD baseline assumption
     - HxRG fallback
     - Design consequence
   * - Format
     - 2k × 2k, 15 µm array
     - H2RG/H4RG-family detector options
     - Updated YJ/H/K split avoids the detector mosaic required by the older HK concept.
   * - Read noise
     - Effective <1 e⁻ RMS in a 60 s sampling-up-the-ramp assumption
     - Several e⁻ for long SUTR; higher for short CDS
     - LmAPD gain matters most between OH lines and for synthesized lower-resolution spectra.
   * - QE
     - Effective QE ~80% across Y/J/H/K after excess-noise-factor penalty
     - Conventional HgCdTe can have ~95% nominal QE and no avalanche excess-noise penalty
     - LmAPDs win when read noise dominates; HxRGs remain competitive when shot noise dominates.
   * - Dark current
     - Project target <3.6 e⁻ pixel⁻¹ h⁻¹, excluding glow
     - Mature HxRG performance is known and around 20 e⁻ pixel⁻¹ h⁻¹
     - K-band and long integrations require careful dark/glow/persistence control.
   * - Known risks
     - 2k × 2k ROIC schedule, glow, persistence, cosmetic uniformity, pixel-to-pixel QE structure
     - Mature procurement and calibration path
     - LmAPDs are the higher-payoff, higher-maturity-risk path; HxRGs are the conservative fallback.

APD Excess Noise and Effective QE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Avalanche gain is not perfectly deterministic. The distribution of multiplication gains contributes an excess noise factor,
which has nearly the same SNR effect as reducing QE. Project material uses an excess noise factor of about 1.2, so an
APD with high physical absorption can behave like a detector with a lower effective QE. This should not be hidden: the
case for LmAPDs is not that every detector property is superior to HxRGs. The case is that the read-noise reduction is
large enough to dominate the SNR trade over much of ZShooter's faint-source IR parameter space.

This is why K band deserves separate treatment. In K, telescope emissivity, sky background, thermal background, and
longer integrations can move observations toward a shot-noise-limited regime, where the LmAPD advantage is reduced
and the QE/excess-noise trade becomes more visible.

HxRG Fallback
~~~~~~~~~~~~~

H2RG/H4RG-family detectors afford a straightforward fallback for the infrared channels. They offer mature packaging, established
calibration behavior and high QE. They also may reduce some risk associated with persistence or pixel-to-pixel avalanche
variations.

The cost is read noise and dark current. Sensitivity estimates performed during the conceptual design phase quantify the
sensitivity loss as roughly 0.4 mag for H2RG-style detectors, but the real operational loss is larger in the exact
regimes ZShooter is trying to open: faint, short, or highly binned observations between OH lines. In those cases,
sky between OH lines may be low enough that a conventional IR array may require very long integrations before shot
noise overtakes read noise.

ZImager qCMOS
-------------

ZImager is a simultaneous tri-band science imager intended to support target
verification, spectrophotometric anchoring, rapid fallback photometry when spectra are too faint, and high-cadence timing
science. That places different demands on its detector than ZSpec: the priority is low read noise at high frame rate, stable
photometry, compact packaging, and manageable data flow.

The current baseline is ORCA-Quest 2-class qCMOS device. Hamamatsu describes the ORCA-Quest 2 as
a photon-number-resolving qCMOS camera with 0.30 e⁻ RMS read noise in ultra-quiet scan mode, a 4096 × 2304 format with
4.6 µm pixels, and improved UV QE relative to the first ORCA-Quest generation.

.. list-table::
   :header-rows: 1
   :widths: 25 38 37

   * - Use case
     - Detector requirement
     - Implication for ZImager
   * - Deep acquisition and field verification
     - Low read noise and high QE in u/variable/z bands
     - Faint ToO fields can be verified without long acquisition overheads.
   * - Spectrophotometric anchoring
     - Stable relative photometry and standard filter support
     - ZImager can anchor ZSpec spectra with pre/post imaging when spectroscopy is not enough.
   * - Millisecond/subsecond timing
     - Fast subrasters with low read noise
     - Compact binaries, occultations, flickering sources, and rapid optical counterparts become real ZImager programs, not just acquisition side-products.
   * - Data handling
     - High frame rates at megapixel scale
     - Requires early DRP/data-volume planning; high-cadence modes must be treated as a first-class data-system requirement.

Performance Implications
------------------------

The detector choices interact with the optical design rather than sitting after it. The current performance story is therefore
best written as a set of detector-dependent consequences, not as a single sensitivity number.

.. list-table::
   :header-rows: 1
   :widths: 23 27 25 25

   * - Choice
     - Primary gain
     - Main fallback penalty
     - Science cases most affected
   * - qCCD vs conventional CCD
     - Sub-electron read noise, charge quantization, short-exposure coadds, high-R then bin
     - Roughly 0.2–0.4 mag loss plus weaker cadence/binning flexibility
     - Young SNe, kilonovae, binaries, primordial D/H, polluted WDs, faint nebular work
   * - LmAPD vs HxRG
     - Effective <1 e⁻ read noise in IR with avalanche gain before readout noise
     - Roughly 0.4 mag loss and stronger read-noise penalty between OH lines
     - Kilonovae, GRBs, high-z SNe, TDEs, H/K diagnostics, low-resolution synthesis
   * - AO + low-noise detectors
     - Smaller sky aperture and higher spectral resolution without equivalent slit-loss penalty
     - AO gains are reduced if detector noise dominates after sky suppression
     - Primordial D/H, lensed systems, faint compact sources, high-R stellar/WD work



Risk Posture
------------

The optical detector risk is low because the qCCD path has a staged fallback. Earlier skipper CCDs already
established the underlying charge-quantization principle; the ZShooter-relevant question is whether the differential,
multi-output, frame-transfer versions arrive at the desired speed/noise point on the project schedule. If STA5900 is
late or underperforms, STA5500-class devices and conventional CCDs both preserve a credible path.

The IR detector risk is more substantive. The desired LmAPD arrays are aligned with active HWO-class detector
development and are exactly the kind of technology ZShooter should exploit if the schedule and procurement path close.
But the 2k × 2k ground-based astronomy implementation is still maturing. Persistence, glow, pixel-to-pixel QE variation,
packaging gaps, and procurement/NRE structure remain live issues. The HxRG fallback protects the instrument from a
single-point detector failure, but not from loss of the most distinctive IR read-noise capability.


Further Reading
---------------

* `Leonardo high-performance shortwave APDs for astronomy`_ — Leonardo overview of LmAPD astronomy development with University of Hawaiʻi and NASA.
* `Leonardo Saphira APD array`_ — public Saphira-family detector specifications and operating concepts.
* `Huber et al. 2024, glow reduction in LmAPDs`_ — recent public LmAPD glow/dark-current and photon-detection testing.
* `NASA ultra-low-noise infrared detector highlight`_ — NASA summary of the University of Hawaiʻi LmAPD development path for HWO-class science.
* `Hamamatsu ORCA-Quest 2 qCMOS`_ — public ORCA-Quest 2 detector/camera description.
* `Skipper CCD single-electron sensitivity`_ — public technical background on nondestructive skipper CCD charge measurement.
* `NSF ATI award (ADS)`_ — public ADS entry for the NSF ATI support referenced in project material.

.. _Leonardo high-performance shortwave APDs for astronomy: https://www.leonardo.us/high-performance-shortwave-apds-for-astronomy
.. _Leonardo Saphira APD array: https://www.leonardo.us/ir-systems-saphira
.. _Huber et al. 2024, glow reduction in LmAPDs: https://arxiv.org/html/2412.09735v1
.. _NASA ultra-low-noise infrared detector highlight: https://science.nasa.gov/science-research/science-enabling-technology/technology-highlights/ultra-low-noise-infrared-detectors-for-exoplanet-imaging/
.. _Hamamatsu ORCA-Quest 2 qCMOS: https://camera.hamamatsu.com/us/en/product/camera/C15550-22UP.html
.. _Skipper CCD single-electron sensitivity: https://arxiv.org/abs/1706.00028
.. _NSF ATI award (ADS): https://ui.adsabs.harvard.edu/abs/2023nsf....2308380S/abstract
