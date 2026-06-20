# Pitch Movement Traits and Pitch Value Score

- Pitch-level source: `data\processed\2026-data-with-woba-xwoba.parquet`
- Score source: `data\processed\pitch_value_scores.csv`
- Model data output: `data\processed\pitch_value_movement_model_data.csv`
- Regression coefficient output: `data\processed\pitch_value_movement_regression_coefficients.csv`
- Movement correlation output: `data\processed\pitch_value_movement_correlations.csv`
- Groups modeled: 568
- Pitch type normalization: `Fastball` is grouped with `Four-Seam`; `Two-Seam` is grouped with `Sinker`.
- Dependent variable: `pitch_value_20_80`
- Predictors were standardized before fitting; coefficients are Pitch Value Score points per one standard deviation.

## Executive Summary

- Movement traits explain a modest share of Pitch Value Score variation: main-effects R-squared `0.0429`, interaction-model R-squared `0.0536`.
- The clearest positive regression signals are `Spin x Velocity` and `Spin Rate`. In baseball terms, spin appears most valuable when it is paired with enough velocity to make the shape play.
- Velocity is negative after controlling for pitch shape and spin. That should not be read as 'velocity is bad'; it means harder pitches in this league-level, pitch-type-mixed sample did not automatically grade better once movement and spin were included.
- HB is negative in the interaction model, meaning more positive HB is associated with lower Pitch Value Score after controlling for the other movement traits.
- IVB, extension, release height, and release side are weaker signals in this model.

## How To Read The Regression

All movement predictors were standardized before modeling. A coefficient of `+1.00` means that a one-standard-deviation increase in that trait is associated with a one-point increase in Pitch Value Score, holding the other modeled traits constant. A negative coefficient means the trait is associated with a lower Pitch Value Score after controls.

Correlation is different from regression. The correlation tables show raw one-to-one relationships. The regression coefficients show conditional relationships after the other movement traits are included. When those disagree, it usually means pitch traits overlap with pitch type, role, or each other.

## Models Fit

| Model | Predictors | R-squared |
|---|---|---:|
| Main effects | IVB, HB, spin rate, velocity, extension, release height, release side | 0.0429 |
| Main effects + interactions | Main effects plus IVB x velocity, HB x velocity, spin x velocity | 0.0536 |

## Movement Correlations

Raw correlations show how each movement trait relates to Pitch Value Score and xwOBA without controlling for the other traits. Positive correlation with Pitch Value Score is good. Negative correlation with `xwoba_frontier`, average exit velocity, HardHit%, or SweetSpot% is generally good for pitchers.

### Correlation With Pitch Value Score

| Trait | Correlation | P-value |
|---|---:|---:|
| `Spin Rate` | 0.0182 | 0.6645 |
| `Extension` | -0.0354 | 0.4001 |
| `Release Side` | -0.0375 | 0.3726 |
| `Release Height` | -0.0498 | 0.2356 |
| `HB` | -0.1167 | 0.0054 |
| `IVB` | -0.1352 | 0.0012 |
| `Velocity` | -0.1835 | <0.0001 |

### Correlation With xwOBA

| Trait | Correlation | P-value |
|---|---:|---:|
| `Spin Rate` | -0.0497 | 0.2372 |
| `Extension` | -0.0127 | 0.7631 |
| `IVB` | -0.0003 | 0.9942 |
| `Release Side` | 0.0027 | 0.9496 |
| `Release Height` | 0.0050 | 0.9047 |
| `HB` | 0.0707 | 0.0921 |
| `Velocity` | 0.0779 | 0.0637 |

## Main Effects Model

| Variable | Coefficient | P-value |
|---|---:|---:|
| `Intercept` | 49.9757 | <0.0001 |
| `IVB` | 0.3770 | 0.5800 |
| `HB` | -0.9354 | 0.0654 |
| `Spin Rate` | 0.3404 | 0.4378 |
| `Velocity` | -2.0144 | 0.0033 |
| `Extension` | 0.2800 | 0.5250 |
| `Release Height` | -0.3287 | 0.4314 |
| `Release Side` | 0.4214 | 0.3985 |

## Interaction Model

| Variable | Std. Coef | P-value | VIF |
|---|---:|---:|---:|
| `Intercept` | 50.0932 | <0.0001 |  |
| `IVB` | -0.0992 | 0.8934 | 3.29 |
| `HB` | -1.0930 | 0.0404 | 1.70 |
| `Spin Rate` | 1.1181 | 0.0460 | 1.88 |
| `Velocity` | -1.8267 | 0.0083 | 2.86 |
| `Extension` | 0.1680 | 0.7036 | 1.17 |
| `Release Height` | -0.2229 | 0.6081 | 1.14 |
| `Release Side` | 0.5480 | 0.3254 | 1.86 |
| `IVB x Velocity` | -0.1250 | 0.7765 | 1.66 |
| `HB x Velocity` | -0.5734 | 0.2441 | 1.30 |
| `Spin x Velocity` | 1.1972 | 0.0283 | 1.84 |

## Variable Importance

| Rank | Variable | Std. Coef | Direction |
|---:|---|---:|---|
| 1 | `Velocity` | -1.8267 | lower pitch value |
| 2 | `Spin x Velocity` | 1.1972 | higher pitch value |
| 3 | `Spin Rate` | 1.1181 | higher pitch value |
| 4 | `HB` | -1.0930 | lower pitch value |
| 5 | `HB x Velocity` | -0.5734 | lower pitch value |
| 6 | `Release Side` | 0.5480 | higher pitch value |
| 7 | `Release Height` | -0.2229 | lower pitch value |
| 8 | `Extension` | 0.1680 | higher pitch value |
| 9 | `IVB x Velocity` | -0.1250 | lower pitch value |
| 10 | `IVB` | -0.0992 | lower pitch value |

## Traits Most Associated with Higher Pitch Value

- `Spin x Velocity`: coefficient 1.1972, p-value 0.0283.
- `Spin Rate`: coefficient 1.1181, p-value 0.0460.
- `Release Side`: coefficient 0.5480, p-value 0.3254.
- `Extension`: coefficient 0.1680, p-value 0.7036.

## Baseball Summary

The model is descriptive, not a pure pitch-design law. It asks which movement and release traits separate higher-scoring pitcher-pitch types after the Pitch Value Score has already summarized whiff, strike, and contact-quality outcomes.

Positive standardized coefficients point toward traits linked with better pitch value. Negative coefficients point toward traits linked with lower pitch value. The interaction terms test whether movement plays differently at higher velocity, which matters because the same IVB or horizontal break can look very different to hitters when it arrives harder.

Use the partial dependence plots as the cleanest visual read: they hold the rest of the movement profile near typical values and show how predicted pitch value changes as one trait moves.

## Plots

- `plots\pitch_value_movement\effect_ivb.png`
- `plots\pitch_value_movement\effect_hb.png`
- `plots\pitch_value_movement\effect_spin_rate.png`
- `plots\pitch_value_movement\effect_velocity.png`
- `plots\pitch_value_movement\effect_extension.png`
- `plots\pitch_value_movement\effect_release_height.png`
- `plots\pitch_value_movement\effect_release_side.png`
- `plots\pitch_value_movement\partial_dependence_ivb.png`
- `plots\pitch_value_movement\partial_dependence_hb.png`
- `plots\pitch_value_movement\partial_dependence_spin_rate.png`
- `plots\pitch_value_movement\partial_dependence_velocity.png`
- `plots\pitch_value_movement\partial_dependence_extension.png`
- `plots\pitch_value_movement\partial_dependence_release_height.png`
- `plots\pitch_value_movement\partial_dependence_release_side.png`
- `plots\pitch_value_movement\partial_dependence_ivb_x_velocity.png`
- `plots\pitch_value_movement\partial_dependence_hb_x_velocity.png`
- `plots\pitch_value_movement\partial_dependence_spin_x_velocity.png`
- `plots\pitch_value_movement\movement_correlation_heatmap.png`