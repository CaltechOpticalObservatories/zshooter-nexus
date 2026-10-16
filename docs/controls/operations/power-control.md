---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter power control operations

Scope: supply/UPS status and control of instrument power. Circuits, outlets, and loads are in the
[power harness](../harnesses/power.md).

## Power distribution

| Area | Equipment | Details still needed |
| --- | --- | --- |
| Server room | Managed UPS, with NUT planned for monitoring | Management connection, backed loads, shutdown thresholds |
| ZFront | 120 VAC from facility UPS; AC distribution to ZImager and ZSpec; local DC supply | Switched outputs and load allocation |
| ZImager | Local DC distribution; local battery provision under review | Retained loads and need for local battery |
| ZSpec VIS | Local DC distribution and UPS provision | Retained loads and UPS arrangement |
| ZSpec NIR | Local DC distribution, presently supplied through VIS | Standalone power connection |

## Controls and status

The available controls depend on the selected supplies and distribution hardware.

| Function | Inputs | Status and feedback |
| --- | --- | --- |
| Read supply/UPS state | Supply or UPS | Input/output state, battery state where available, faults |
| Switch an output | Output and on/off | Output state and affected loads |
| Power-cycle a load | Load | Off/on progress and resulting equipment state |
| Shut down a computer | Host or group | Shutdown progress and outcome; see [computer management](computer-management.md) |

## Interruption and recovery

An interruption plan needs the actual UPS coverage and the loads required to maintain cooling,
vacuum support, and monitoring. Shutdown thresholds and restart behavior remain to be set for that
hardware.

Module isolation must leave the retained modules and central glycol monitoring available. The
isolation points are part of the power harness design.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Facility UPS is the working direction for the RNAS feed. The remaining local
battery/UPS entries need review in that context. NIR also needs a practical power arrangement for
standalone AIT and maintenance. There is not enough information yet to write a switching sequence.

:::
