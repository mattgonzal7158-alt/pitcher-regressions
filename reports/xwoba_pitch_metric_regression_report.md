# Pitch Metrics Predicting Frontier xwOBA

- Input file: `data\processed\2026-data-with-woba-xwoba.parquet`
- Aggregate output: `data\processed\pitcher_pitch_type_xwoba_metrics.csv`
- Aggregation level: pitcher + pitch type
- Total pitcher-pitch type groups: 2,443
- Regression groups after filters: 568
- Filters: at least 50 pitches and 10 tracked batted balls
- Pitch type normalization: `Fastball` is grouped with `Four-Seam`; `Two-Seam` is grouped with `Sinker`.
- Dependent variable: average `xwoba_frontier`
- Model R-squared: 0.7982

## Metric Definitions

| Metric | Definition Used |
|---|---|
| Whiff% | `Strike Swinging / swings`; swings are swinging strikes, fouls, and balls in play. |
| CSW% | `(Called Strike + Automatic Strike + Strike Swinging) / total pitches`. |
| PutAway% | `Strikeout / two-strike pitches`. |
| K% | `Strikeout / terminal PA-ending pitches` for that pitch type. |
| Average Exit Velocity | Mean `hit_launch_exit_speed_y` on tracked batted balls. |
| HardHit% | Batted balls with exit velocity at least 95 mph / tracked batted balls. |
| Barrel% | Approximate Statcast barrel zone using EV at least 98 mph with launch-angle window expanding from 26-30 degrees. |
| SweetSpot% | Batted balls with launch angle from 8 to 32 degrees / tracked batted balls. |

## Regression Output

| Variable | Coefficient | P-value | Standardized Coef | VIF |
|---|---:|---:|---:|---:|
| `Intercept` | -0.371140 | <0.0001 |  |  |
| `whiff_pct` | 0.012652 | 0.2676 | 0.0326 | 2.39 |
| `csw_pct` | 0.005128 | 0.7888 | 0.0072 | 1.98 |
| `putaway_pct` | 0.002118 | 0.8803 | 0.0046 | 2.58 |
| `k_pct` | -0.023066 | 0.0809 | -0.0635 | 3.65 |
| `avg_exit_velocity` | 0.006835 | <0.0001 | 0.5687 | 2.07 |
| `hardhit_pct` | 0.125364 | <0.0001 | 0.2495 | 2.19 |
| `barrel_pct` | -0.044729 | 0.1323 | -0.0315 | 1.21 |
| `sweetspot_pct` | 0.146243 | <0.0001 | 0.3220 | 1.08 |

## Variable Importance

| Rank | Variable | Standardized Coef | Direction |
|---:|---|---:|---|
| 1 | `avg_exit_velocity` | 0.5687 | higher xwOBA |
| 2 | `sweetspot_pct` | 0.3220 | higher xwOBA |
| 3 | `hardhit_pct` | 0.2495 | higher xwOBA |
| 4 | `k_pct` | -0.0635 | lower xwOBA |
| 5 | `whiff_pct` | 0.0326 | higher xwOBA |
| 6 | `barrel_pct` | -0.0315 | lower xwOBA |
| 7 | `csw_pct` | 0.0072 | higher xwOBA |
| 8 | `putaway_pct` | 0.0046 | higher xwOBA |

## Most Associated with Lower xwOBA

- `k_pct`: standardized coefficient -0.0635, p-value 0.0809.
- `barrel_pct`: standardized coefficient -0.0315, p-value 0.1323.

## Baseball Interpretation

Negative coefficients indicate traits associated with suppressing expected damage on contact for a pitcher-pitch type. Positive coefficients indicate traits associated with allowing more expected damage.

Miss metrics and contact metrics should be read together. A pitch can lower xwOBA either by missing bats and stealing strikes before contact happens, or by shaping contact into weaker, less optimal launch conditions. VIF values are included because these pitch traits overlap: for example, HardHit%, Barrel%, SweetSpot%, and average exit velocity often move together.

In this model, the strongest lower-xwOBA indicators are the variables with the most negative standardized coefficients. Those are the best all-else-equal signals for pitcher-pitch types that prevent dangerous batted balls. The strongest positive coefficients identify risk traits: when those rise, average xwOBA tends to rise after controlling for the other metrics.

## Visualizations

- `plots\xwoba_pitch_metrics\standardized_coefficients.png`
- `plots\xwoba_pitch_metrics\metric_correlation_heatmap.png`
- `plots\xwoba_pitch_metrics\whiff_pct_vs_xwoba.png`
- `plots\xwoba_pitch_metrics\csw_pct_vs_xwoba.png`
- `plots\xwoba_pitch_metrics\putaway_pct_vs_xwoba.png`
- `plots\xwoba_pitch_metrics\k_pct_vs_xwoba.png`
- `plots\xwoba_pitch_metrics\avg_exit_velocity_vs_xwoba.png`
- `plots\xwoba_pitch_metrics\hardhit_pct_vs_xwoba.png`
- `plots\xwoba_pitch_metrics\barrel_pct_vs_xwoba.png`
- `plots\xwoba_pitch_metrics\sweetspot_pct_vs_xwoba.png`