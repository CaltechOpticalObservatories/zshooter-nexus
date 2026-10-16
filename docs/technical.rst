Design
======

ZShooter has two fixed-format spectrometers, each with three spectral channels:

- **VIS:** B/G/R, each with one 2k × 4k qCCD.
- **NIR:** YJ/H/K, each with one 2k × 2k LmAPD.
- **ZImager:** three additional qCMOS detectors for simultaneous optical imaging.

The spectrometers use six single-detector focal planes, with no detector or grating mosaics.
ZFront, ZImager, ZSpec VIS, and ZSpec NIR are separately supported assemblies for independent
alignment and removal.


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
      :link: control.html
      :link-type: url

      How ZShooter is controlled


.. toctree::
   :hidden:
   :maxdepth: 1

   optical_design
   architecture
   detector_technologies
   control
   cad
