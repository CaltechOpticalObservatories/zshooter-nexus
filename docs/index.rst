ZShooter
=========

.. image:: _static/image/zshooter_tagline.png
   :alt: ZShooter tagline banner
   :class: zs-tagline-banner

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item::

      .. image:: _static/image/zshooter.png
         :alt: ZShooter logo
         :class: zs-home-logo

   .. grid-item::

      .. container:: zs-kicker

         Keck I optical-IR spectrograph and imager

      .. container:: zs-lead

         ZShooter is a Keck I workhorse in the making: an always-online optical-IR spectrograph plus a fast tri-band
         imager, built for decisive single-object science when timing, throughput, and wavelength leverage all matter
         at once.

         It is intended to carry out observations that will bottleneck single-object astronomy in the Rubin era:
         fast response, broad wavelength coverage, high throughput, and spectral resolution useful well past
         first-look classification.

      .. container:: zs-lead

         This site, like ZShooter, is actively evolving. It is here to do three jobs: clearly convey the concept,
         give the team a living technical home that keeps science and design stories clearly accessible, and affords
         both the team and future users and maintainers the resources they need to understand how to work with ZShooter.


.. grid:: 1 2 2 4
   :gutter: 2

   .. grid-item-card:: Science
      :link: science.html
      :link-type: url

      Why the instrument exists and what science cases are already shaping its design.

   .. grid-item-card:: Requirements
      :link: requirements.html
      :link-type: url

      A short table of the current design pressures.

   .. grid-item-card:: Technical design
      :link: technical.html
      :link-type: url

      The post-CoDR architecture: where the instrument is, where it's headed, and what is still open.

   .. grid-item-card:: Observing
      :link: observing.html
      :link-type: url

      Simulator, classical and ToO operations, data reduction.

.. grid:: 1 2 2 4
   :gutter: 2

   .. grid-item-card:: Program management
      :link: program_management.html
      :link-type: url

      The useful part of the sausage-making: budgets, interfaces, WBS, and the things we keep forgetting.

   .. grid-item-card:: Documents & tools
      :link: documents_tools.html
      :link-type: url

      Formal docs, repos, boards, notebooks, shared tools, and the links everyone winds up needing.

   .. grid-item-card:: Presentations & publications
      :link: presentations_publications.html
      :link-type: url

      Public-facing material, internal briefings, and references this site can aggregate cleanly for us.

   .. grid-item-card:: Contacts
      :link: contacts.html
      :link-type: url

      Who we are.

.. container:: zs-note

   **Current design in a nutshell**

   - Always-online at **Keck I Right Nasmyth for rapid response**
   - **Two spectrometers (optical & nIR) / six channels (blue, green, red, yj, h, k)**
   - **2k x 2k active detector area** per channel, qCCDs and LmAPDs.
   - **ZSpec + ZImager** are a deliberately paired instrument, not two unrelated appendages
   - AO-enhanced-seeing ready, optimized for natural seeing

.. container:: zs-quote

   **A Zero-latency Spectrograph with High-throughput Optical-nIR Observing for Transient Exploration & Response**

   **...so much more than X we had to skip Y.**

.. container:: zs-note

   Many of these pages are naturally mixed-use: useful to the team, useful to future students, eventually useful to
   observers and WMKO operations.


.. toctree::
   :hidden:
   :maxdepth: 3

   science
   requirements
   technical
   observing
   documents_tools
   program_management
   presentations_publications
   contacts
