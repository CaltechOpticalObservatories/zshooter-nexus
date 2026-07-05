Instrument Requirements
=======================

.. container:: zs-lead

   These design pressures drive ZShooter's technical trades. The science team will continue to evaluate exact numbers
   throughout instrument design as technical trades arise. Here we capture design pressures clearly to show what
   capabilities the instrument is trying to protect.

.. container:: zs-note

   **Read this table as design point, rather than a frozen baseline.**

.. container:: zs-tight-table

   .. list-table::
      :header-rows: 1
      :widths: 18 24 28 30

      * - Capability
        - Design point
        - Why
        - Science cases effectively lost without it
      * - Spectral coverage
        - 310-2480 nm in one visit through six science channels
        - One-shot optical-IR leverage is the whole point for a large fraction of the target set.
        - Kilonovae, TDEs, high-z SNe, solar system targets, broad-band transient follow-up
      * - Nominal resolution
        - About R = 18k with a 0.7" slit
        - Keeps RV, abundance, and line-profile work alive without giving up workhorse throughput.
        - Binaries, primordial D/H, polluted white dwarfs, CGM / IGM absorption, detailed stellar work
      * - Higher-resolution path
        - Narrower-slit (penalty-free with AO-enhancement)
        - Much of the instrument's long-term value sits in not painting ourselves into a low-R corner.
        - D/H, lensed systems, future HIRES-replacement use, line-profile science
      * - Lower-resolution path
        - Nominal or wider slit (narrow w/AO-enhanced) with a mix of on-chip and digital binning (5-20x total)
        - Rapid transient classification often needs only broad spectral classification
        - :zs-check:`Faint TOO followup`
      * - Slit length
        - 10 arcsec baseline
        - Gives room for sky subtraction, nodding strategy, and practical real-world acquisition.
        - Nebular SNe, solar system, binaries, faint point-source spectroscopy
      * - Rapid response
        - Always-online on K1 RNAS with a low-overhead observing path; latency budget 5-min
        - Fast temporal-event science does not forgive slow setup.
        - Kilonovae, GRBs, LFBOTs, young SNe, early TDEs
      * - Detector format
        - 2k x 2k active area per science channel
        - Simplifies the instrument, removes mosaics from the baseline, and lowers maintenance pain.
        - Broadly everything; this is mostly about buildability and operational sanity
      * - Imaging support
        - Simultaneous tri-band optical imaging, with final (1-3') field still under active trade
        - Acquisition support, environmental context, fallback photometry, and fast-timing science all want this.
        - Kilonovae, binaries, solar system, very faint transients, context imaging
      * - High-cadence imaging
        - Millisecond / sub-second with ZImager qCMOS
        - Some science cases are fundamentally timing-limited, not exposure-limited.
        - Ultracompacts, occultations, compact binaries, rapid optical variability
      * - Quicklook + calibration support
        - Near-real-time reduction and usable calibration products are part of the operations plan
        - Observers need to decide on the fly whether to keep going, stop, or change tack.
        - ToO triage, faint transients, RV quality control, efficient classical observing


Science & Facility (L1) Requirements
------------------------------------

The optical design is driven by five coupled requirements. ZShooter must
cover the atmospheric near-UV cutoff through K band, preserve enough resolving power for stellar and circumstellar
kinematics, remain sensitive enough for deep spectra after binning to low resolution,
support sky subtraction, and avoid operational configurations that would slow ToO response.

The choice of a high native resolving power only pays off if the detectors keep low enough read
noise that the spectra can be rebinned later without losing the S/N advantage.  Likewise, the
choice to keep ZShooter always-online on K1 RNAS only pays off if ZFront, ZImager, ZSpec, and the guide/WFS interface
do not create a hidden acquisition or calibration bottleneck.


The design is optimized for dynamic range in spectral
information: enough native resolution that stellar, CSM, absorber, and abundance programs are not compromised, and low
enough detector/read-noise penalty that R≈1000 products remain efficient for faint transients. Moreover the use of
 low/zero-noise :doc:`detector technologies <detector_technologies>` is expected to further mitigate the noise penalty
from high binning factors.


Subsystem (L2) Requirements
---------------------------

To Upload


Detailed (L3) Requirements
--------------------------

To Upload

