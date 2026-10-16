---
zs-mode: internal
myst:
  heading_anchors: 3
---

# Operations

Draft device functions, commands, status, and recovery behavior for ZShooter. Each page links to its
physical interfaces and identifies the controller assignments or operating details still needed.

| Area | Scope |
| --- | --- |
| [ZFront and ZCal](zfront-zcal.md) | Beam selection, calibration insertion, illumination, and source control |
| [ZSpec](zspec.md) | VIS/NIR motion, focus, shutters, slit viewers, and science readout |
| [ZImager](zimager.md) | ADC, filter selection, detector rotation, focus, and acquisition |
| [Digital functions](digital-functions.md) | Fine guiding, nodding, signal assessment, astrometry, and sequencing |
| [Environmental services](environmental-services.md) | Glycol, air, temperature, vacuum, and cryogenics |
| [Networking](networking.md) | Connections, discovery, status, and recovery |
| [Power control](power-control.md) | Distribution, UPS, switching, isolation, and recovery |
| [Computer management](computer-management.md) | Hosts, services, storage, and standalone operation |

[Harnesses](../harnesses/index.md) contains the harness and connection records.
[Calibration procedures](../../procedures/calibration.md) covers the associated measurements and
observing flows.

```{toctree}
:hidden:
:maxdepth: 1

ZFront and ZCal <zfront-zcal>
ZSpec <zspec>
ZImager <zimager>
Digital functions <digital-functions>
Environmental services <environmental-services>
Networking <networking>
Power control <power-control>
Computer management <computer-management>
```
