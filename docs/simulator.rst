Instrument Simulator
====================

.. container:: zs-lead

   Explore ZShooter performance, detector alternatives and the X-shooter comparison.
   The notebooks show their saved calculations and figures. Each page offers the
   notebook for download; the simulator repository provides the environment to run it.

Comparisons
-----------

Start with the flat-AB notebook and its :doc:`results report
<_staged/sim/docs/xshooter-comparison-results>`. The :doc:`detector operating points
<_staged/sim/docs/detector-operating-points>` document the detector packages,
exposures and reduction checks used in these comparisons.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Flat-AB instrument comparison <_staged/sim/notebooks/02_Flat_AB_Comparison>
   Kilonovae — ZShooter <_staged/sim/notebooks/01_Kilonovae>
   Kilonovae — alternative detectors <_staged/sim/notebooks/01_Kilonovae_ALTDET>
   Kilonovae — X-shooter <_staged/sim/notebooks/01_Kilonovae_XSHOOTER>
   Resolution and detector sampling <_staged/sim/notebooks/03_Resolution_and_Sampling>
   Slit illumination and calibration lamps <_staged/sim/notebooks/03_Slit_Illumination_Lamps>

Performance and imaging
-----------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   ZSpec performance <_staged/sim/notebooks/zshooter_performance>
   ZImager simulation <_staged/sim/notebooks/06_ZImager>
   ZImager image quality <_staged/sim/notebooks/zshooter_zimager_diq>
   SPIE 2026 <_staged/sim/notebooks/zshooter_spie2026>

Science examples and ScopeSim
-----------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Stellar spectra <_staged/sim/notebooks/02_Stellar>
   White dwarf spectra <_staged/sim/notebooks/03_White_dwarf>
   Exomoons <_staged/sim/notebooks/04_Exomoons>
   Comet spectra <_staged/sim/notebooks/05_Comets>
   ScopeSim overview <_staged/sim/notebooks/i_ScopeSim_Overview>
   ScopeSim sources <_staged/sim/notebooks/ii_ScopeSim_Sources>

Reports, validation and setup
-----------------------------

The reports explain the assumptions and limitations behind the results. Validation
notebooks preserve the measurements used to check the simulator and reductions.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Simulator reports and environment <_staged/sim/docs/index>
   Validation notebooks and reference data <simulator-validation>

See also the `ScopeSim documentation <https://scopesim.readthedocs.io/en/latest/>`_
and `ScopeSim repository <https://github.com/AstarVienna/ScopeSim>`_.
