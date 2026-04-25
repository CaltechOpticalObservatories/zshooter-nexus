ToO Programs
============

.. container:: zs-lead

   ZShooter's ToO science will require a new kind of Keck ToO operations: rapid, template-driven, alert-fed
   observations where contacting a program astronomer is not in the execution flow and the instrument is not a
   bottleneck.

.. container:: zs-note

   This page should stay split between **instrument capability** and **observatory policy**. The first is ours to
   design. The second needs WMKO evolution and should not be written as settled before it is settled.

Design intent
-------------

ZShooter's ToO concept is intentionally split into two layers. Outside the instrument boundary,
the ToO system needs a template-driven observing system: programs define alert criteria,
requested observations, cadence rules, and instrument configuration(s) needed; the software expands a match
into an executable observation package; and hands the instrument a classic-style target
list with minimal internal overhead. This keeps observatory and program policy governing
governs interruption authority, competing-trigger priority, alert-ingest rules, and time
charging governed by observatory-owned software.

The point of this split is simple: once the beam is on the instrument, ZShooter should not be the
reason a rapid follow-up fails. The instrument is being designed for always-online operation at
K1 RNAS, prompt internal reconfiguration, acquisition support via ZImager, fast calibration
sequences, and live reduction/quick-look feedback so that staff and observers can decide
whether to continue, repeat, or stop.

What ZShooter can do directly
-----------------------------

On the observatory side, the desired workflow is:

* accept pre-filed program definitions that pair alert criteria with required observations,
  cadence ideas, and instrument defaults
* expand a matched alert into a concrete observation package, including SOP-driven defaults
  and implicit calibrations
* check what has already been observed and what reduced products already exist before asking
  for another visit
* hand observatory staff/ZShooter a classic-style target list and configuration payload for execution

On the instrument side:

* ZShooter reduces data quickly enough to support follow-on decisions embedded in programs, bookkeeping, and
  sharing results


That stack is well matched to ZShooter's broader architecture: GUI-driven
operation, a reusable daemon-based ICS, archive-facing data products, and quick-look/DRP
support intended to surface useful feedback during the observation itself.

What still depends on Keck policy and tooling
---------------------------------------------

The observatory-facing side is where the major non-instrument dependencies remain. In
particular, the following are not just software implementation details; they are policy and
operations questions that need explicit WMKO agreement:

* whether rapid ToO programs can be represented as standing program-level trigger definitions,
  rather than only as pre-registered target lists
* which trigger sources may be monitored automatically, and under what approval model
* who is authorized to approve, reject, interrupt, or restore a classical night when a trigger
  arrives
* how multiple matching triggers in a single night are prioritized, queued, or batched
* how time is charged when a program expands into repeated visits, partial execution, or shared
  follow-up logic

This page therefore describes the operating model ZShooter is trying to enable, not a claim
that Keck has already ratified that operating model.

Response classes
----------------

The current operational concept is easiest to understand as a small set of response classes:

Rapid
   Working target for events where the first spectrum is time-critical. The instrument design is
   built around starting science exposure within five minutes of beam delivery, with the
   most aggressive science cases seeking effectively immediate handoff once the telescope is
   ready.

Fast
   Intended for cases where same-hour action still matters, but where a fully interrupt-driven
   response is not always required.

Same-night / same-day
   Intended for follow-up that should happen during the current observing window, but does not
   require a true immediate interruption.

Planned
   Intended for cadence follow-up, predicted windows, or pre-scheduled revisit logic.

These response classes are useful because they let the instrument team talk clearly about
configuration latency, calibration latency, handoff expectations, and sequence design, even
before every Keck-side policy detail is finalized.

Template-driven programs
------------------------

A ZShooter ToO program is best thought of as a standing observing recipe rather than a static
list of named targets. A submission should be able to carry:

* alert or event-match criteria
* required observations and visit limits
* cadence logic, including repeat-visit patterns
* instrument templates, defaults, and calibration bundles
* ownership, allocation, and result-sharing metadata

This model supports both fully specified automated programs and lighter-weight requests that
fall back to standardized templates or human-on-call support. That distinction matters:
WKMO and ZShooter should be able to support both a mature, machine-actionable program and a more
human-mediated one in the Rubin era.

Trigger and cadence concepts
----------------------------

The operational concepts work already identifies several cadence patterns that are worth
exposing explicitly in any future Keck-side ToO tooling:

* single-epoch follow-up
* fixed repeat cadence over a configurable range of days
* adaptive cadence whose spacing grows with time since first trigger
* orbit-phase sampling for short-period systems
* visibility-window sampling for cases constrained by geometry rather than urgency
* visit multiplicity rules such as one visit, multiple visits, or :math:`N` visits per orbit

..
    For ZShooter this is not abstract workflow language. Different science cases genuinely need
    these different patterns: kilonovae and young SNe want rapid first contact plus short-baseline
    revisits; long-period binary programs want repeatability and bookkeeping over long baselines;
    compact binaries need orbit-phase logic; and solar-system follow-up can require a mix of rapid
    response and geometry-limited revisits.

Execution handoff
-----------------

The desired execution chain remains human-mediated at the observatory boundary. In the
current concept, the automation layer does the matching, expansion, schedule evaluation,
bookkeeping, and product-aware stop/continue logic, but the final execution gate remains with
WMKO staff.

A representative handoff looks like this:

#. incoming alerts are ingested through connectors
#. a matching engine compares them against active programs and filters
#. the observation package builder expands the match into the required observations
#. the scheduling layer applies observability, interrupt policy, and remaining allocation
#. the ToO handoff gate presents an executable block and handoff window to the Telescope
   Operator and SA
#. once approved, the observation is delivered to the instrument as a classic-style target list
   and configuration payload
#. the ICS executes, the DRP reduces, and products are published to archive and downstream
   result-sharing logic

That human-gated model is deliberate. It keeps the instrument architecture compatible with
current Keck operating culture while still making room for a much more automated pre-execution
pipeline.

Calibration and data feedback
-----------------------------

Rapid ToO work only functions if calibration behavior is predictable. The current operational
concept assumes that daytime calibration products carry most of the burden, and that any
required contemporaneous setup calibration for a newly selected configuration can be made
short enough to fit inside the slew-plus-acquire window. This is exactly the kind of latency
budget that matters for ZShooter: the science case is often tolerant of modest absolute
precision drift, but it is not tolerant of slow, operator-heavy setup.

The companion requirement is immediate feedback. Quick-look products, extracted spectra,
configuration metadata, and archive handoff are part of the observing loop, not merely
post-facto reduction. For template-driven ToOs, the ability to decide whether an event has
already been adequately observed, whether a sequence should continue, and whether a result
should trigger follow-on notifications depends on that reduction path being operationally real,
not aspirational.

Results and accounting
----------------------

Once an observation has completed, the system still has work to do. The program stack needs to maintain an
observation ledger, connect completed products to the archive, compute time debits against the program database,
and generate the follow-on result or alert notifications that drive later visits.


Architecture views
------------------

Overall architecture
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <figure class="zs-architecture-figure">
     <a href="_static/d2_diagrams/too_architecture.svg" target="_blank" rel="noopener">
       <img src="_static/d2_diagrams/too_architecture.svg" alt="ZShooter ToO architecture diagram">
     </a>
     <figcaption>Overall ToO architecture. Click to open the full SVG in a new tab.</figcaption>
   </figure>

Program submission
~~~~~~~~~~~~~~~~~~

.. raw:: html

   <figure class="zs-architecture-figure">
     <a href="_static/d2_diagrams/program_submission.svg" target="_blank" rel="noopener">
       <img src="_static/d2_diagrams/program_submission.svg" alt="ZShooter ToO program submission diagram">
     </a>
     <figcaption>Program submission flow. Click to open the full SVG in a new tab.</figcaption>
   </figure>

Alert response loop
~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <figure class="zs-architecture-figure">
     <a href="_static/d2_diagrams/alert_response_loop.svg" target="_blank" rel="noopener">
       <img src="_static/d2_diagrams/alert_response_loop.svg" alt="ZShooter alert response loop diagram">
     </a>
     <figcaption>Alert response loop. Click to open the full SVG in a new tab.</figcaption>
   </figure>

Completion and accounting loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <figure class="zs-architecture-figure">
     <a href="_static/d2_diagrams/too_completion_loop.svg" target="_blank" rel="noopener">
       <img src="_static/d2_diagrams/too_completion_loop.svg" alt="ZShooter ToO completion loop diagram">
     </a>
     <figcaption>Completion and accounting loop. Click to open the full SVG in a new tab.</figcaption>
   </figure>