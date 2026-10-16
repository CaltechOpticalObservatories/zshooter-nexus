:zs-mode: both

Controls
========

.. container:: zs-lead

   ZShooter's control system follows a straightforward pattern:
    - observer-first control,
    - modular daemons,
    - a simple, useful quicklook,
    - engineering tooling used from AIT through maintenance.

.. Draft navigation: to hide both branches from navigation, replace the next
   ".. container:: zs-internal-only" line with "..". Its indented contents
   become an RST comment. Restore that line to show them in Internal mode.
   The draft pages still compile for local review; their content is unchanged.

.. container:: zs-internal-only

   **Operations and harnesses — working drafts**

   - :doc:`Operations <controls/operations/index>`: device functions, commands, status, and recovery.
   - :doc:`Harnesses <controls/harnesses/index>`: module boundaries, harnesses, and shared services.

   .. toctree::
      :hidden:
      :maxdepth: 3

      Operations <controls/operations/index>
      Harnesses <controls/harnesses/index>

.. grid:: 1
   :gutter: 2

   .. grid-item-card:: Software
      :link: _staged/ics/index.html
      :link-type: url

      Architecture, daemon and driver inventories, interfaces, operations,
      testing, AIT, and design decisions maintained with the ICS source.

.. container:: zs-note

   The ICS documentation is authored in the ICS repository and staged here
   from the pinned submodule revision.

.. toctree::
   :hidden:
   :maxdepth: 3

   Software <_staged/ics/index>
