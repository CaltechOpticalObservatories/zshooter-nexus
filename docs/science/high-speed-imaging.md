# High-speed qCMOS Imaging

```{container} zs-lead
ZImager uses three qCMOS detectors for simultaneous multiband photometry. Windowed operation provides 1 to 5 ms frame times over a 3 arcmin by 20 arcsec field.
```

Millisecond to second time resolution is needed because orbital, spin, and accretion signals are smeared by longer exposures. Simultaneous colors help separate brightness changes caused by viewing geometry from changes in temperature or emission component.

```{figure} figures/high_speed_burdge2019_fig1a.png
:alt: CHIMERA g-band light curve of an eclipsing double white dwarf
:class: zs-science-figure

CHIMERA g-band light curve of the 6.91 minute eclipsing double white dwarf ZTF J1539+5027. The observations used 3 s exposures and resolve the primary and secondary eclipses.  
Source: Burdge et al. 2019, Nature, 571, 528, Figure 1a; ZShooter SRD Section 2.3.3.2; ZShooter CDR Chapter 3 and Table 3.1; High-Speed Optical Imaging Science Case.
```

## Science Drivers

- Ultracompact white-dwarf binaries have 5 to 20 minute orbital periods. Exposures of 5 s or less resolve eclipses, while multiband light curves constrain temperature ratios and inclinations.
- Accreting black-hole and neutron-star binaries show optical variability on 10 to 100 ms timescales. Simultaneous colors distinguish changes in the emission components.

## Instrument Requirements

- Optical pulsars require windowed frame rates of at least 100 Hz and frame-level absolute timing for comparison with radio and X-ray ephemerides.
- Three simultaneous imaging bands are an L1 requirement. .
- The proposed fast-mode requirements are at least 100 Hz in a window containing the target and a comparison star, at least two simultaneous bands, and absolute timing accuracy of at most 1 ms.

## Observing Requirements

- ZImager and ZSpec support rapid switching between phase-resolved imaging and spectroscopy of the same target.

