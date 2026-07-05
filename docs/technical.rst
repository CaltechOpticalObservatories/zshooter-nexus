Technical Design
================

Post-conceptual design the ZShooter got simpler on purpose:
    - two spectrometers instead of three, three channels per spectrometer,
    - 6 detectors instead of vs 4 focal planes with 9 detectors and 3 mosaics (2k x 4k VIS and 2k x 2k NIR)
    - less han half then anamorphism, and
    - no detector or grating mosaics.

This significantly reduced operational complexity, maintainability, and lowers cost all while increasing instrument
performance.

This section documents the current architecture/design.


Optical Design
--------------

ZShooter's optics are fed both by K1 M2 and, eventually K1 DM2. The front-end must support
calibration light sources, co-registration of ZImager and ZSpec, seeing-enhancement from future AO, and neighboring
L and R RNAS instruments.  The current design has been updated incorporating conceptual review feedback, with the main
architectural change a move from three to two spectrometers, each split into three science channels.


.. grid:: 1 2 2 5
   :gutter: 2

   .. grid-item-card:: System architecture
      :link: architecture.html
      :link-type: url

      System diagrams: Hardware, software, etc. ...

   .. grid-item-card:: Optical design
      :link: optical_design.html
      :link-type: url

      ZShooter's Optical design and open trades

   .. grid-item-card:: Detector technologies
      :link: detector_technologies.html
      :link-type: url

      Details on the qCCD's, LmAPDs, qCMOS detectors

   .. grid-item-card:: CAD models
      :link: cad.html
      :link-type: url

      Quick access to CAD models and drawings

   .. grid-item-card:: Controls
      :link: software.html
      :link-type: url

      How ZShooter is controlled


.. toctree::
   :hidden:
   :maxdepth: 1

   optical_design
   architecture
   detector_technologies
   seeing_enhancement
   control
   cad
