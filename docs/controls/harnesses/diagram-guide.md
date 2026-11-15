---
zs-mode: internal
myst:
  heading_anchors: 3
---

# Reading the architecture diagrams

The <a href="../../_static/archwrap.html?selected=zshooter_overview.svg">instrument overview</a>
follows light through ZFront to the instrument channels and data through readout, storage and
reduction. Its arrows summarize those relationships at assembly level. Click an item for its
documentation or a linked data path for the detailed drawing. Container links are on their
labels and link icons; the background stays available for panning and any tooltip. Hover over
a device, container or information icon for its tooltip. The **Diagram** menu also includes
<a href="../../_static/archwrap.html?selected=zshooter_power.svg">Instrument Power</a>, which
follows AC/DC supplies and distribution through the modeled power recipients and panels.

The <a href="../../_static/archwrap.html?selected=zshooter_connections.svg">complete connection map</a>
is a zoomable wiring reference. **Focus** selects RNAS, ZShooter, an assembly, EBox, vessel or panel.
Drag to pan. Ctrl/⌘ + wheel and the zoom buttons change scale. **Legend** is also in the Focus list; its heading links to this guide.
**Full window** opens the viewer outside the page frame; **Open SVG** opens the drawing itself.

Containers identify physical assemblies. A vessel assembly includes its vacuum gauge and automatic gate valve,
both mounted outside vacuum. Invisible layout groups keep adjacent panels together. Panel rows name
functional connections; connector part numbers and contact assignments belong in the assembly
drawings. A glycol line represents its supply/return pair. Helium has a separate colour.

The USB, Ethernet, power, glycol, vacuum, shutter and readout views select connections from the same
instrument model. Changing a device or cable in that model updates the views that contain it.
The optical view uses light-path arrows and the same equipment identities. The NIR feedthrough
view contains cables and warm services; the baffled optical port appears in the optical view.

A dashed outline identifies an optional component. Amber is reserved for an explicitly provisional
choice and is unused in this revision. Archons and CRED2 use the ordinary equipment styles.

In the software view, blue boxes are physical computers, purple queue-shaped nodes are collections
of daemons, and white rounded boxes are applications or services. Requests go to the daemons;
published state and events return to clients and telemetry. Data paths use magenta arrows.
A collection does not imply one process or a shared busy state.

The [architecture package README](https://github.com/baileyji/zshooter_d2#readme)
explains source locations, tooltips and rendering. Detailed APIs belong with the
[ICS documentation](../../_staged/ics/index.rst).
