Instrument Simulator
====================

.. container:: zs-lead

   Explore the instrument forecasts, compare detector choices, or work through a
   science observation. The notebooks include saved calculations and figures and
   can be downloaded to run or adapt.

For the instrument forecast, start with :doc:`ZSpec performance
<_staged/sim/notebooks/zshooter_performance>` or :doc:`ZImager
<_staged/sim/notebooks/06_ZImager>`. For the detector trade, start with
:doc:`the comparison plots and detector settings <simulator/comparisons>`.

.. grid:: 1 1 2 2
   :gutter: 2

   .. grid-item-card:: Performance and imaging
      :link: simulator/performance
      :link-type: doc

      ZSpec sensitivity, ZImager performance and image quality, and the
      SPIE 2026 calculations.

   .. grid-item-card:: Detector and instrument comparisons
      :link: simulator/comparisons
      :link-type: doc

      Detector alternatives, noise budgets and X-shooter comparisons, with plots
      alongside the notebooks that produced them.

   .. grid-item-card:: Science examples
      :link: simulator/science
      :link-type: doc

      Kilonovae, stars, white dwarfs, exomoons and comets.

   .. grid-item-card:: Resolution and optical models
      :link: simulator/models
      :link-type: doc

      Slit illumination, detector sampling, trace geometry and the interpretation
      of simulated spectra.

To run or develop the calculations, see :doc:`Running the simulator
<simulator/running>` for ScopeSim introductions, environment setup and the
development record.

.. toctree::
   :hidden:
   :maxdepth: 1
   :titlesonly:

   Performance & imaging <simulator/performance>
   Detector comparisons <simulator/comparisons>
   Science examples <simulator/science>
   Optical models <simulator/models>
   Running the simulator <simulator/running>
