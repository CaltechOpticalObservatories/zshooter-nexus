---
zs-mode: internal
myst:
  heading_anchors: 3
---

# Reading the architecture diagrams

Start with the <a href="../../_static/archwrap.html?selected=hardware_overview.svg">instrument overview</a>. Click a linked object to open its documentation. The <a href="../../_static/archwrap.html?selected=hardware_systems_full.svg">complete panel map</a> is a wiring reference: use **Focus** to select a module, EBox, vessel or individual panel, then zoom to follow a connection. Drag to pan; Ctrl/⌘ + wheel, the zoom buttons and keyboard controls also work. Choose **Legend** in the same list to read the key. **Full window** opens the viewer outside the page frame; **Open SVG** gives the standalone drawing.

Connection views use containers for physical boundaries; concept views group related paths. Panel tables follow the interfaces enumerated in the harness notes; their rows identify functional connections. Connector part numbers and contact assignments belong in the assembly drawings. A glycol line represents a supply/return pair. Unarrowed lines are physical connections; arrows show optical paths, triggers or information flow.

Blue linked cards are navigation points. Amber marks a baseline component or implementation selection. A dashed outline marks an optional component. These styles carry the qualification without lengthening every label.

## Baseline choices

This revision uses the item ledger and connection notes, with Jeb's 13 November 2026 corrections:

| Topic | Depiction |
|---|---|
| Motion control | One Beckhoff master each for ZImager, VIS and NIR. Module computers remain separate. |
| ZFront | Pneumatic ZImager/ZSpec selection, calibration insertion and point/diffuse selection. Ethernet connects the lamp, valve/service and neighbor-selector controllers. This baseline needs no ZFront EtherCAT master. |
| Spectrograph readout | One Archon per detector: B/G/R and YJ/H/K. The ledger's DC supply entries supersede the earlier AC labels in the harness notes. |
| Focus and slit viewing | VIS relative focus acts on the first pre-optic, ahead of the field rotator and ADC. VIS slit-viewer focus uses the optional style. CRED2 is outside vacuum, looking through a baffled port with a cold shortpass filter. |
| NIR services | VIS supplies the normal NIR DC feed and network. The separate <a href="../../_static/archwrap.html?selected=nir_support_cabinet.svg">support-cabinet view</a> shows the off-instrument arrangement. The cabinet appears only there. |
| Network | A combined 10G ZFront-to-VIS link carries control and Archon traffic. The NIR network branches from VIS. This gives a specific baseline for the network and panel drawings. |
| Imager readout | Independent CXP optical transport for U/V/Z, outside the ZFront EBox, ending at three PCI cards. The transport equipment is a baseline selection. |
| Thermal wiring | General NIR sensors/heaters use the support VIB. Detector thermal circuits stay with their channels at the detector VIB. This drawing assigns that boundary so the thermal harness can be reviewed as a whole. |
| Local interfaces | USB serves the 1-Wire hubs, VIS slit viewer and gauge interfaces. CRED2 is drawn on Ethernet. These are concrete interface choices for review; the ledger still carries some USB/Ethernet/EtherCAT alternatives. |

The NIR supply row has conflicting voltage/source fields; the diagram follows its named upstream VIS DC bus. No supply voltage or connector rating is inferred from that row. The standalone cabinet supplies the same functional service interfaces.

## Useful paths

<a href="../../_static/archwrap.html?selected=optical_train_full.svg">Optical routing</a> ·
<a href="../../_static/archwrap.html?selected=imager_readout.svg">Imager readout</a> ·
<a href="../../_static/archwrap.html?selected=nir_feedthroughs.svg">NIR feedthroughs</a> ·
<a href="../../_static/archwrap.html?selected=shutter_triggers.svg">Shutter triggers</a> ·
<a href="../../_static/archwrap.html?selected=vacuum_protection.svg">Vacuum protection</a> ·
<a href="../../_static/archwrap.html?selected=module_isolation.svg">Module removal</a> ·
<a href="../../_static/archwrap.html?selected=software_runtime_full.svg">Software roles</a>

The software view describes host roles and information paths. Detailed APIs and process definitions live with the [ICS documentation](../../_staged/ics/index.rst).
