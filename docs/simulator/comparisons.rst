:zs-mode: internal

Detector and Instrument Comparisons
====================================

Start with **Detector packages and sensitivity** for the detector settings and
the revised H2RG YJ comparison. **Instrument comparison plots** collects the
X-shooter comparison, detector trades and noise budgets from the earlier run.
Each report identifies the settings used for its figures.

.. figure:: /_staged/sim/validation/xshooter/data/detector_packages/alternate_yj_h2rg_performance_r1000.png
   :alt: ZShooter performance comparison with H2RG detectors in all three alternative NIR channels.
   :target: ../_staged/sim/docs/detector-operating-points.html#explicit-exposure-settings

   One-hour, 0.70 arcsec natural-seeing comparison at approximately R=1000.
   Select the plot for the detector settings and exposure cadences.

Plots and interpretation
-------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Detector packages and sensitivity </_staged/sim/docs/detector-operating-points>
   Instrument comparison plots </_staged/sim/docs/xshooter-comparison-results>

Notebooks
---------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Flat-AB instrument comparison </_staged/sim/notebooks/02_Flat_AB_Comparison>
   Kilonovae — alternative detectors </_staged/sim/notebooks/01_Kilonovae_ALTDET>
   Kilonovae — X-shooter </_staged/sim/notebooks/01_Kilonovae_XSHOOTER>

The :doc:`X-shooter model </_staged/sim/docs/xshooter>` describes its inputs and
approximations. The :doc:`ZShooter kilonova example
</_staged/sim/notebooks/01_Kilonovae>` supplies the baseline science case.
