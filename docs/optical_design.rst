Optical Design
==============

.. container:: zs-note-to-team zs-internal-only

   The source material for these pages is the CDR optical chapter, the February 2026 post-CoDR optical update, and my notes/memory
   The post-CoDR update controls the design intent for the ZSpec channel split and detector format. -Jeb

   A key todo is to revise the requirement/design language for compatibility with this agreed upon updated R.

   `Early PD Optical Design Update <https://caltech.sharepoint.com/:p:/r/sites/coo/zshooter/Shared%20Documents/ZS%20-%20Papers%20and%20Presentations/Caltech%20Faculty%20Presentations/ZShooter%20-%20Optical%20Update%20Post%20CoDR%20v2.pptx?d=w9e1f293ac5c74428935e55972f6eaf18&csf=1&web=1&e=xCGlKi>`_.


.. container:: zs-placeholder zs-internal-only

   **Figure placeholders for this page**

   - One clean optical block diagram showing RNAS → ZFront → ZSpec/ZImager (& R/L inst)
   - One common-coordinate sketch showing guide field, ZImager field, ZSpec slit center, and calibration field.


The present optical concept is composed of into four key parts:

.. list-table:: Optical assemblies
   :header-rows: 1
   :widths: 18 27 55

   * - Assembly
     - Function
     - Current design intent
   * - RNAS interface
     - Receive the Keck I beam and preserve future AO/guide compatibility.
     - ZShooter sits on-axis at K1 RNAS, where the deployable tertiary can feed it quickly.  The mechanical/optical
       interface must leave volume for the facility guide and future AO wavefront-sensing hardware.
   * - ZFront
     - Select science/calibration paths and send light to ZSpec, ZImager, or neighboring RNAS instruments.
     - Two-stage light-path selection, with a calibration launch upstream of the selection.
   * - ZSpec
     - Six science channels of fixed-format echelle spectroscopy.
     - Two spectrometers: one visible and one infrared.  Each spectrometer is split into three detector channels formatted on 2k × 2k active areas.
   * - ZImager
     - Simultaneous tri-band imaging for photometric anchoring, high-cadence work, imaging-only fallback science, and acquisition support.
     - Refractive collimator, dichroic split into u / selectable / z-like channels, and one fast qCMOS detector module per channel.



RNAS Focus
----------

ZShooter is allocated to the Keck I Right Nasmyth platform.  The native Nasmyth focus is
described as approximately 1.5 m above the platform floor and approximately 0.39 m outside the elevation bearing.  This
motivates the use of front-end relay and selection optics: the focus is too close to the bearing to let the
full spectrograph architecture simply grow around the native focal plane without imposing significant packaging constraints.

The optical design assumes that ZShooter is a natural-seeing instrument capable of utilizing exceptional seeing.
The future K1 AO STRATA system is treated as a performance enhancer increasing the number of "exceptional seeing" nights
rather than as an enabling condition.  ZShooter will be ready to exploit narrower delivered PSFs for reduced sky
background and higher spectral resolution without concomitant slit losses when AO becomes available.

.. container:: zs-placeholder zs-internal-only

   **Figure placeholder:** K1 RNAS nominal focus geometry from ``cad/drawings/k1rnas.pdf`` or the equivalent
   released CAD/ICD view.  This should show the K1 elevation bearing, nominal telescope focus, the ZImager fold path,
   and the straight-through ZSpec path.

.. container:: zs-note-to-team zs-internal-only

   Confirm the allowable secondary-z focus adjustment range, subject to some nominal induced
   aberration/vignetting penalty, and then what additional shift STRATA/K1AOF can practically deliver for L/R instruments
   without (or with quantified, minimal, i.e. fold mirror sizes) changes to the ZFront relay assumptions.

ZFront
------

ZFront is the telescope-facing beam switchyard and calibration assembly.  It selects where the
telescope beam or calibration beam goes.

The current concept is a two-stage light-path selector.  The first selector chooses whether the incoming field goes
directly to ZImager, to ZImager with the central field passed on to ZSpec, or to the
second selector.  The second selector chooses the ZSpec dichroic/pre-optics path or a feed to an instrument to the
left or right of ZShooter on the RNAS platform. This implementation naturally allows the central science field to
be passed to neighboring instruments as well while imaging the surrounding with ZImager, but maintaining
such capability is not a ZShooter science requirement.

The calibration launch is planned upstream of the first selector so that a common calibration reference
can be delivered to both systems.  The baseline concept is a fiber-fed integrating sphere that illuminates a
roughly 20–30 arcsec central field, with lamp sources for wavelength calibration and continuum/flat-field work.
Hollow-cathode lamps such as ThAr, ThArNe, ThNe, or UNe, together with LED and quartz sources: the specific sources
remain under evaluation. A point-source mask is also attractive because it would let the same calibration path probe
ZSpec/ZImager co-alignment and PSF behavior rather than only flat-field response.


.. container:: zs-note-to-team zs-internal-only

   **Current optical review queue**

   - ZFront calibration path: define whether the point-source/pinhole mode is a requirement or an AIT convenience.


ZSpec Summary
-------------

For details, see :doc:`zspec_optical`.

ZSpec is best described as a six-channel, two-spectrometer, fixed-format echelle.  The visible spectrometer
is split into Blue, Green, and Red channels; the infrared spectrometer is split into YJ, H, and K channels.  This
preserves the broad 310–2450 nm science grasp while reducing the number of slits and the echelle gratings,
avoiding detector and echelle mosaics, and reducing the previous large anamorphic excursions of the conceptual design
while delivering improved optical efficiency.

.. list-table::
   :header-rows: 1
   :widths: 18 20 24 38

   * - Spectrometer
     - Channel
     - Approximate passband
     - Design rationale
   * - Visible
     - Blue
     - 308–420 nm
     - Highest leverage for atmospheric-cutoff science, hot stars, D/H, and flash-ionization diagnostics and partially isolates the region with the most difficult coatings, glass transmission, and detector QE.
   * - Visible
     - Green
     - 400–600 nm
     - Places the highest-throughput optical region in its own channel rather than on the roll-off of a broader blue/red cross-disperser design.
   * - Visible
     - Red
     - 580–980 nm
     - Carries the red optical diagnostics and bridges toward the YJ channel without forcing one detector/coating solution across the full visible range. Covers Hα through Ca triplet and red continuum/absorption diagnostics.
   * - Infrared
     - YJ
     - 950–1350 nm
     - Avoids an IR detector mosaic and isolates the lowest-background NIR range.
   * - Infrared
     - H
     - 1457–1848 nm
     - Improves the efficiency balance relative to the conceptual studies YJ/HK split.
   * - Infrared
     - K
     - 1972–2482 nm
     - Contains the thermal-background-sensitive portion of the design in one channel.

.. container:: zs-note-to-team zs-internal-only

   Jason, I'm inclined to axe the rationale above or qualify it here. To my mind this is driven by detector area
   demands and blaze efficiencies given R and m needs with pupil size.

ZImager Summary
---------------

ZImager is a co-aligned tri-band imager. It supports four roles: pre/post-imaging around ZSpec observations,
photometric anchoring of spectra, imaging-only fallback for targets beyond spectroscopic reach, and
millisecond-to-second cadence observations of compact and rapidly variable sources.  It is also useful operationally
because it can help identify faint transients, moving targets, host-galaxy context, and slit-placement ambiguities
before committing ZSpec exposure time.

It's optical layout uses a refractive collimator over a 1–3 arcmin field, two dichroics and a fold mirror
to create three channels with fast cameras feeding one ORCA-Quest qCMOS detector per band.  The nominal filters
are u, one selectable middle band, and z.  The middle channel is expected to include both standard broadband options
and may carry narrow filters where science demand and throughput justify them.

For details, see :doc:`zimager_optical`.

Guiding and Wavefront Sensing
-----------------------------

Routine telescope guiding is expected to be handled by a facility guide system developed for K1 RNAS, with ZShooter as
the initial client.  The same facility work is expected to preserve the volume and optical interfaces
needed for natural-guide-star and sodium-laser wavefront sensing associated with the Keck I AO facility.  This keeps
ZShooter from carrying a one-off guider solution that would later fight the AO architecture or
be replicated by neighboring instruments.

The key ZShooter optical implications are straightforward.  First, the slit, ZImager field, guide field, and future WFS
references must be tied to a stable and well-documented coordinate model.  Second, acquisition support must work
before AO is available.  Third, once seeing enhancement is available, the optical design should turn a smaller
delivered PSF into better S/N at higher spectral resolution without requiring a redesign of ZSpec.

A detailed white-paper on the relevant coordinate transforms is available here `zs_cood_math`_.


Calibration and Co-alignment
----------------------------

The optical calibration strategy is meant to be repeatable and low overhead.  ZFront provides common internal
calibration delivery for a central common field; ZImager supplies field photometry and WCS context; ZSpec supplies
fixed-format spectra whose stability can be tracked against arcs, flats, standards, and sky features.  The system
should therefore be aligned and documented as an integrated optical instrument, not as a spectrograph
plus an unrelated camera.

At minimum, the optical design and AIT plan will verify:

- ZSpec/ZImager common-field registration and its repeatability across light-path selector moves
- Slit-center, ZImager channel WCS, and guide-system reference consistency, including reregistration procedures.
- Wavelength calibration stability versus slit-selector repeatability, rotator angle, thermal state, and time.
- ZImager photometric flatness and color terms for the selected broadband filters.
- Calibration-beam uniformity and its ability to support both flat-fielding and co-alignment checks.



.. toctree::
   :hidden:
   :maxdepth: 1

   zspec_optical
   zimager_optical
