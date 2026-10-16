---
zs-mode: internal
myst:
  heading_anchors: 3
---

# ZShooter Vacuum Harnesses & Connections

Scope: four vessel branches, gauges, automatic gate valves, and the shared pump. Related operations:
[environmental services](../operations/environmental-services.md#vacuum).

Diagrams:
[VIS detector assemblies](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/subsystems.d2)
and
[NIR assembly](https://github.com/baileyji/zshooter_d2/blob/d0c5ec581d60008d01dc86c04f0d72a4871852c4/entities/zspec.d2).

## Assembly boundaries

- B/G/R detector vessels
- NIR cryostat
- Four gauge and automatic gate-valve branches
- Shared roughing/turbo pump and manifold

## Vacuum connections

| Vessel | Gauge | Isolation | Pump connection |
| --- | --- | --- | --- |
| VIS B | B vacuum gauge | B automatic gate valve | Shared pump; branch layout open |
| VIS G | G vacuum gauge | G automatic gate valve | Shared pump; branch layout open |
| VIS R | R vacuum gauge | R automatic gate valve | Shared pump; branch layout open |
| NIR | NIR vacuum gauge | NIR automatic gate valve | Shared pump; removable-NIR connection capped |

Gauge placement, valve/manifold arrangement, fittings, and service connections remain open. Pump
cooling is included in the [glycol harness](glycol.md).

## Electrical connections

| Equipment | Connection | Detail |
| --- | --- | --- |
| Vessel gauges | Power and readout | Local host/controller connections open |
| Automatic gate valves | Local sensing, actuation, and position indication | Closes on power-loss |
| Shared pump | Power, local controls, status | Equipment selection and remote interface open |

Automatic valve operation is independent of host software. The local protection connections and any
host status interface will be shown in the assembly drawings.

## Service connections

Each vessel needs an isolation arrangement for servicing or removal while the retained vessels
remain in use. Disconnects, caps/blanks, and pump-down connections will be assigned with the
manifold layout.

:::{container} zs-note-to-team zs-internal-only

**Team notes:** Automatic-valve logic, pressure thresholds, and the response to pump or valve-power
loss remain open. The selected equipment and manifold arrangement will establish the pump-down and
recovery procedures.

:::
