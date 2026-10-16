# Detector Technologies

ZSpec uses quantizing CCDs (qCCDs) in its three visible channels and linear-mode avalanche
photodiode arrays (LmAPDs) in its three infrared channels. ZImager uses three ORCA-Quest 2 qCMOS
cameras for simultaneous multiband imaging.

## Detector baseline

| Subsystem | Preferred detector | Active format and pixel size | Fallback / status |
| --- | --- | --- | --- |
| ZSpec VIS: B, G, R | STA5900 qCCD with tapered ALD anti-reflection coating | 2,048×4,096; 15 µm | STA5500 qCCD, then conventional STA or Teledyne-e2v CCD |
| ZSpec NIR: YJ, H, K | Leonardo LmAPD; Ike Pono and IBEX are candidates | 2,048×2,048; 15 µm target | H2RG/H4RG-family HgCdTe array |
| ZImager: three optical bands | Hamamatsu ORCA-Quest 2 qCMOS | 4,096×2,304; 4.6 µm | Commercially available; cameras in use |

Each ZSpec channel has one detector; no detector mosaics are required. The VIS qCCD frame store is
additional to the active image area.

## ZSpec VIS: qCCDs

Skipper readout samples the same charge packet nondestructively. For independent samples, read
noise falls approximately as 1/√N, approaching single-electron charge resolution. ZShooter's
preferred architecture combines differential signal/reference sampling, many parallel outputs,
and a frame store that allows readout while the next exposure integrates.

| Device | Role | Readout performance |
| --- | --- | --- |
| STA5500 | Available qCCD fallback; 4,096×2,048 image area and matching frame store | Approximately 1 e⁻ read noise in 13 s |
| STA5900 | Preferred faster device; bulk red-sensitive and epitaxial blue-optimized versions | Target approximately 1 e⁻ in 2.8 s; charge quantization in approximately 120 s |

Low read noise supports short sub-exposures for cosmic-ray rejection and changing conditions,
while retaining high native spectral resolution. OH-contaminated samples can be down-weighted
before binning to the science resolution. Integer-electron peaks provide calibration of gain,
zero signal, linearity, and serial clock-induced charge, with potential brighter-fatter diagnostics.
On-chip binning remains available when the observation can trade native sampling for sensitivity.

### Tapered AR coatings

The fixed echellogram maps a narrow wavelength range to each detector location. A spatially
varying coating can match that local range, targeting **less than 1% reflectance** and reducing
ghosts, fringing, and scattered light.

| VIS channel | Coating passband | Full channel span |
| --- | --- | --- |
| B | 310–430 nm | 120 nm |
| G | 430–650 nm | 220 nm |
| R | 650–980 nm | 330 nm |

The initial coating study uses a graded Al₂O₃ layer bounded by HfO₂, deposited by atomic layer
deposition (ALD). The thickness gradient and local bandwidth must be matched to the current
2k×4k echellograms; process calibration and repeatability remain development work.

<!-- The earlier 3.5/6.5/13 nm/mm gradients and 365/500/780 nm midpoints used older channel
spans. They are not the current coating prescription without verification against the integrated
format. -->

Conventional CCDs preserve wavelength coverage. Their read-noise and QE penalties are included
in the {ref}`fallback comparison <detector-fallback-comparison>` below.

## ZSpec NIR: LmAPDs

HgCdTe LmAPDs multiply photoelectrons before the readout integrated circuit (ROIC) adds noise.
This reduces effective read noise in short integrations and between OH lines. Leonardo's
**Ike Pono and IBEX** are candidate implementations for the three NIR channels.

The current ZShooter model and design targets are:

| Parameter | LmAPD baseline | HxRG comparison |
| --- | --- | --- |
| Format | One 2k×2k, 15 µm array per YJ/H/K channel | H2RG/H4RG-family options |
| Effective read noise | <1 e⁻ RMS in a 60 s sampling-up-the-ramp exposure | H2RG comparison: 6 e⁻ |
| QE | Approximately 80% effective QE, including the avalanche excess-noise penalty | Approximately 95% nominal QE |
| Dark current | Target <3.6 e⁻ pixel⁻¹ h⁻¹, excluding glow | H2RG comparison: 23 e⁻ pixel⁻¹ h⁻¹ |

Avalanche multiplication introduces an excess-noise factor of approximately **1.2** in the project
model. Its S/N penalty is represented by the reduced effective QE. In K, sky and thermal shot
noise reduce the advantage of low read noise; the higher-QE H2RG is slightly deeper in the
one-hour comparison below.

Earlier LmAPD testing reported glow of approximately **0.012 e⁻ pixel⁻¹ frame⁻¹** with a modified
pixel structure ([Huber et al. 2024][huber]). This is a measurement from the development program,
not a specification for either current candidate array.

:::{container} zs-note-to-team zs-internal-only

**Leonardo update — detector team contribution needed.** Leonardo has made significant progress;
both Ike Pono and IBEX may meet ZSpec's needs, and quotation requests are being accepted. Add the
latest device results and compare the two options: available format and ROIC, read noise versus
gain and cadence, QE/excess noise, dark current and glow, persistence, and uniformity. Record
packaging, procurement/NRE terms, and delivery estimates. Update the model assumptions where the
new results support a change.

:::

## ZImager: qCMOS

The **ORCA-Quest 2** provides **4,096×2,304 pixels at 4.6 µm**, with **0.30 e⁻ RMS read noise in
ultra-quiet scan mode** and improved UV QE relative to the original ORCA-Quest. Three cameras
support acquisition, spectral flux normalization, and simultaneous multiband time-series
photometry. Windowed readout supports high-cadence observations; the 0.30 e⁻ figure applies to the
ultra-quiet mode, not every readout rate.

The [ZImager design](zimager_optical.md) gives the optical layout, detector scale, and simulator
parameters. Camera mode, subarray size, cadence, and read noise must be qualified together for
the timing modes, including exposure synchronization, timestamp accuracy, and sustained data
rates.

(detector-fallback-comparison)=
## Detector fallback comparison

The saved dark-time calculation uses **one hour on source**, a **0.70″ slit**, **0.65″ natural
seeing**, **airmass 1.1**, and **R≈1,000**. OH emission is included, with independent S/N
optimization for each detector choice. Values are medians over complete matched spectral bins.

| Channel | Conventional detector | Limiting magnitude relative to the qCCD/LmAPD baseline |
| --- | --- | --- |
| B | CCD | 1.06 mag shallower |
| G | CCD | 0.46 mag shallower |
| R | CCD | 0.34 mag shallower |
| YJ | H2RG | 0.53 mag shallower |
| H | H2RG | 0.25 mag shallower |
| K | H2RG | 0.06 mag deeper |

The calculation includes an equal-duration independent sky reference and the different detector
QE curves. It bins **after readout**; it does not include CCD on-chip binning. The
[Performance page](performance.md) gives the baseline limiting magnitudes and a separate detector
break-even calculation that does include on-chip binning.

<!-- Source: saved zshooter_performance.ipynb, conventional-detector sensitivity-regime table
(cell 79), medians over complete matched bins. Not the multi-scenario order-peak medians from
cell 78 or the all-bin diagnostic from cell 80. -->

:::{container} zs-note-to-team zs-internal-only

**Outstanding detector work**

- **qCCD readout:** verify STA5900 noise versus readout time, clock-induced charge, frame-transfer
  overhead, and availability; retain STA5500 and conventional CCD alternatives.
- **Tapered coatings:** derive thickness gradients and instantaneous bandwidths from the current
  B/G/R echellograms; verify reflectance, calibration, and fabrication repeatability.
- **LmAPDs:** complete the Ike Pono/IBEX comparison above, including detector/controller packaging
  and the operating gain, temperature, and sampling cadence for YJ, H, and K.
- **qCMOS:** qualify readout modes, synchronization, timing, photometric stability, and sustained
  data rates for the selected subarrays.

**Technical references**

- [Skipper CCD single-electron sensitivity][skipper].
- [Leonardo astronomy APD development][leonardo] and [Saphira detector family][saphira].
- [Huber et al. 2024: LmAPD glow and dark-current measurements][huber].
- [NASA ultra-low-noise infrared detector development][nasa].
- [Hamamatsu ORCA-Quest 2 specifications][quest].
- [NSF ATI award][ati].

:::

[huber]: https://arxiv.org/html/2412.09735v1
[skipper]: https://arxiv.org/abs/1706.00028
[leonardo]: https://www.leonardo.us/high-performance-shortwave-apds-for-astronomy
[saphira]: https://www.leonardo.us/ir-systems-saphira
[nasa]: https://science.nasa.gov/science-research/science-enabling-technology/technology-highlights/ultra-low-noise-infrared-detectors-for-exoplanet-imaging/
[quest]: https://camera.hamamatsu.com/us/en/product/camera/C15550-22UP.html
[ati]: https://ui.adsabs.harvard.edu/abs/2023nsf....2308380S/abstract
