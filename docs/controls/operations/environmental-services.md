---
zs-mode: internal
myst:
  heading_anchors: 3
---

# Environmental service operations and commands

Scope: glycol, air, ambient/enclosure temperature monitoring, vacuum, and cryogenic control.

## Glycol

The exposed ZFront manifold distributes cooling to ZImager, ZSpec, and the ZFront EBox. It includes
temperature, flow, leak monitoring, and automatic shutoff. Leak monitoring must remain available
with modules disconnected.

| Function | Inputs | Status and feedback | Details still needed |
| --- | --- | --- | --- |
| Monitor cooling | Circuit | Supply/return temperature, flow, leak state | Sensor locations and branch coverage |
| Shut off cooling on a leak | Local leak indication | Shutoff and leak state | Which branch or supply closes; reset behavior |
| Enable/isolate a branch, if remotely controlled | Branch and requested state | Valve state | Valve selection and remote interface |

Connections: [glycol harness](../harnesses/glycol.md).

## Air

Air supplies enclosure positive pressure and any pneumatic actuators selected for ZFront. The
manifold includes pressure sensing. Valve controls and behavior on loss of air depend on the
actuator choices.

| Function | Status and feedback | Details still needed |
| --- | --- | --- |
| Monitor supply | Pressure and sensor status | Sensor location, units, operating range |

Connections: [air harness](../harnesses/air.md). Mechanism commands are in
[ZFront/ZCal](zfront-zcal.md).

## Ambient and enclosure temperatures

ZImager and VIS use 1-Wire hubs and temperature sensors. NIR may use the cryogenic temperature
controller for enclosure monitoring as well.

| Reading | Associated information |
| --- | --- |
| Temperature | Sensor name/location, value, units, sample time, missing/fault indication |

Sensor locations and any use in focus maintenance will be added with the thermal and optical design.

## Vacuum

Each B/G/R detector vessel and the NIR cryostat has a gauge and automatic gate valve, with a shared
pump. Gate-valve operation is independent of host software.

| Function | Status or control | Details still needed |
| --- | --- | --- |
| Read vacuum | Vessel pressure, units, gauge status | Gauge/controller interface |
| Observe automatic isolation | Valve position and local fault, where available | Local logic and status connections |
| Pump down or isolate a vessel | Local controls; remote controls if fitted | Valve arrangement and operating procedure |

Connections: [vacuum harness](../harnesses/vacuum.md).

## Cryogenic and thermal control

| Assembly | Controls and readings | Details still needed |
| --- | --- | --- |
| VIS B/G/R detector assemblies | Individual cryocooler controls, temperatures, faults | Interfaces, operating temperatures, and cooling dependencies |
| NIR cryostat | Temperature-controller setpoints, sensors/heaters, coldhead and compressor status | Sensor/heater assignments, temperature limits, cooldown/warm-up behavior |
| Mechanical room | Compressor and cryo-monitor status | Available controls and fault indications |

Connections: [ZSpec VIS](../harnesses/zspec-vis.md), [ZSpec NIR](../harnesses/zspec-nir.md), and
[glycol](../harnesses/glycol.md).

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Selected hardware will determine the temperature/pressure limits and the response to
cooling, vacuum, or power loss. Local protection, retained monitoring, and recovery need to work
with modules absent or on the bench. These are still design tasks; numerical limits and operating
sequences are not yet assigned.

:::
