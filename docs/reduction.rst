:zs-mode: both

Data Reduction
==============

.. container:: zs-lead

   ZShooter's data reduction pipeline glues together established reduction packages,
   detector/header conventions, the WMKO/KOA archive, and user-specified ToO-specific triage.

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card:: Data Reduction Pipeline documentation
      :link: _staged/drp/index.html
      :link-type: url

      Installation, current architecture, and the evolving reduction workflow.

   .. grid-item-card:: Extraction demo
      :link: _staged/drp/notebooks/extraction_demo.html
      :link-type: url

      A rendered, non-executing view of the canonical DRP example notebook.

.. container:: zs-note

   The DRP documentation and notebooks are authored in the DRP repository and staged here
   from the pinned submodule revision.

.. toctree::
   :hidden:
   :maxdepth: 3

   _staged/drp/index
