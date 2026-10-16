# High-speed qCMOS Imaging

```{container} zs-lead
ZImager uses three qCMOS detectors for simultaneous multiband photometry. Its fastest cadence uses
detector subarrays.
```

Millisecond to second time resolution is needed because orbital, spin, and accretion signals are
smeared by longer exposures. Simultaneous colors help separate brightness changes caused by viewing
geometry from changes in temperature or emission component.

```{figure} figures/high_speed_burdge2019_fig1a.png
:alt: CHIMERA g-band light curve of an eclipsing double white dwarf
:class: zs-science-figure

CHIMERA g-band light curve of the 6.91 minute eclipsing double white dwarf ZTF J1539+5027. The
observations used 3 s exposures and resolve the primary and secondary eclipses.\
Source: Burdge et al. 2019, Nature, 571, 528, Figure 1a; ZShooter SRD Section 2.3.3.2; ZShooter CDR
Chapter 3 and Table 3.1; High-Speed Optical Imaging Science Case.
```

## Science Drivers

- Ultracompact white-dwarf binaries have 5 to 20 minute orbital periods. Exposures of 5 s or less
  resolve eclipses, while multiband light curves constrain temperature ratios and inclinations.
- Accreting black-hole and neutron-star binaries show optical variability on 10 to 100 ms
  timescales. Simultaneous colors distinguish changes in the emission components.

## Instrument Requirements

- The [L1 requirements](../requirements/l1.md) specify three simultaneous imaging bands.
- Fast-mode imaging requires at least 100 Hz, with a goal of at least 1 kHz, in a subfield
  containing the target and at least one comparison star in at least two bands simultaneously.
- GPS-synchronized per-frame absolute timing must be accurate to at most 1 ms, with a goal of
  50 µs, for comparison with radio and X-ray ephemerides.

## Observing Requirements

- ZImager and ZSpec support rapid switching between phase-resolved imaging and spectroscopy of the
  same target.

