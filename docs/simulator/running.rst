Running the Simulator
======================

Each notebook page has a download link. Use the installation guide to set up the
simulator and its dependencies; the ScopeSim introductions explain how to build
sources and observations.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   Installation </_staged/sim/docs/install>
   ScopeSim overview </_staged/sim/notebooks/i_ScopeSim_Overview>
   ScopeSim sources </_staged/sim/notebooks/ii_ScopeSim_Sources>
   Reproducing an environment </_staged/sim/docs/reproducibility>
   Troubleshooting </_staged/sim/docs/troubleshooting>

Development record
------------------

The detector trades and X-shooter comparison were developed by Jeb Bailey with
Codex assistance. That work also produced diagnostic notebooks, saved regression
data and reports used to investigate numerical behavior, repair reductions and
prepare the simulator PR series. The scientific plots and reasoning are linked
from the relevant topics on this site. The development records stay in the
repository:

* `Validation notebooks and supporting data <https://github.com/CaltechOpticalObservatories/zs-scopesim/tree/main/validation>`_
  preserve the experiments and debugging runs.
* `Development reports <https://github.com/CaltechOpticalObservatories/zs-scopesim/tree/main/docs>`_
  include runtime repairs, upstream checks and integration history.
* `PR review series <https://github.com/CaltechOpticalObservatories/zs-scopesim/blob/main/docs/review-series.md>`_
  and `follow-up work <https://github.com/CaltechOpticalObservatories/zs-scopesim/blob/main/docs/h4rg-development.md>`_
  record how the work was split for review; their branch and merge instructions
  describe that stage of development.

For the current code and environment, use the
`simulator repository <https://github.com/CaltechOpticalObservatories/zs-scopesim>`_.
