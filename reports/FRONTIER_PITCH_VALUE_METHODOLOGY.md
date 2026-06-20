# Frontier League Pitch Value Methodology

## Quick Read

Pitch Value Score is a pitch-level quality grade.

Higher is better.

It grades one pitch type for one pitcher, not the entire pitcher. A pitcher can have an elite slider and still have an ordinary overall profile if the rest of the arsenal, command, usage, or durability is weaker.

Current qualification:

- At least 50 pitches
- At least 10 tracked batted balls

The main score files are:

- `data/processed/pitch_value_scores_with_type_rank.csv`
- `reports/pitch_value_score_leaderboards.md`

## What Goes Into The Score

The score is built from pitcher + pitch type aggregates. Each row is one pitch type thrown by one pitcher.

Pitch type labels are normalized before aggregation:

- `Fastball` and `Four-Seam` are treated as `Four-Seam`
- `Two-Seam` and `Sinker` are treated as `Sinker`

The inputs are split into two groups.

### Miss And Strike Metrics

| Metric | Definition | Why It Matters |
|---|---|---|
| Whiff% | Swinging strikes / swings | Measures bat-missing ability. |
| CSW% | Called strikes + swinging strikes / pitches | Captures called-strike and whiff value. |
| PutAway% | Strikeouts / two-strike pitches | Measures ability to finish counts. |
| K% | Strikeouts / terminal PA-ending pitches for that pitch type | Measures finishing value when the pitch ends plate appearances. |

### Contact Metrics

| Metric | Definition | Why It Matters |
|---|---|---|
| Average Exit Velocity | Mean EV on tracked batted balls | Lower EV generally means weaker contact. |
| HardHit% | Batted balls at least 95 mph / tracked batted balls | Lower is better for pitchers. |
| Barrel% | Approximate barrel-zone batted balls / tracked batted balls | Lower is usually better, but this coefficient is conditional on the other contact metrics. |
| SweetSpot% | Batted balls from 8 to 32 degrees / tracked batted balls | Lower is better for pitchers because this is a productive launch window. |

## xwOBA Frontier

Before creating Pitch Value Score, I built `xwoba_frontier` for tracked batted balls.

The selected xwOBA model used:

- Exit Velocity
- Launch Angle
- Launch Angle squared
- Batted Ball Type

That model was selected because it had the best holdout RMSE and R-squared among the tested xwOBA models.

## Regression Behind Pitch Value Score

Pitch Value Score comes from this regression:

`xwoba_frontier ~ miss metrics + contact metrics`

The goal was to learn which pitch-level outcomes are most predictive of lower expected damage.

The regression found that contact quality carried most of the predictive weight:

- Average Exit Velocity
- SweetSpot%
- HardHit%

Miss metrics still matter in baseball evaluation, but in this model they added less extra xwOBA explanation after contact quality was already included.

## How The Score Is Calculated

Each input metric is standardized across qualified pitcher-pitch type rows.

Then the standardized regression coefficients are applied:

`xwOBA_pressure = sum(standardized_coefficient * metric_z)`

Because lower xwOBA is better for pitchers, the sign is reversed:

`pitch_value_raw = -xwOBA_pressure`

So:

- Higher `pitch_value_raw` is better.
- Higher `pitch_value_20_80` is better.
- Higher `pitch_value_0_100` is better.

## Score Columns

| Column | Meaning |
|---|---|
| `pitch_value_raw` | Unscaled regression-weighted score. Higher is better. |
| `pitch_value_20_80` | Scouting-style scale. 50 is average, 60 is plus, 70 is double-plus, 80 is the cap. |
| `pitch_value_0_100` | Percentile rank among qualified pitcher-pitch types. |
| `overall_rank` | Rank among all qualified pitcher-pitch types. |
| `pitch_type_rank` | Rank within the normalized pitch type label. |

## How To Interpret Scores

| Score | Interpretation |
|---:|---|
| 80 | Top-end pitch in this dataset. |
| 70 | Elite / double-plus result profile. |
| 60 | Clearly above average. |
| 50 | League average among qualified pitcher-pitch types. |
| 40 | Below average. |
| 30 or lower | Poor result profile. |

Always read the score with:

- Pitch count
- Batted-ball count
- Pitch type
- xwOBA
- Component metrics

Small batted-ball samples can make contact metrics noisy.

## Movement Regression

After Pitch Value Score was created, I tested which movement and release traits were associated with higher scores.

Movement predictors:

- IVB
- HB
- Spin Rate
- Velocity
- Extension
- Release Height
- Release Side

Interaction terms tested:

- IVB x Velocity
- HB x Velocity
- Spin x Velocity

The movement model answers a different question than the Pitch Value Score model.

Pitch Value Score asks:

> Which pitches have the best miss, strike, and contact-management outcomes?

Movement regression asks:

> Which movement traits are associated with those better pitch scores?

## How To Read Movement Regression Tables

All movement predictors are standardized before modeling.

A coefficient of `+1.00` means:

> A one-standard-deviation increase in that trait is associated with a one-point increase in Pitch Value Score, holding the other movement traits constant.

A negative coefficient means the trait is associated with lower Pitch Value Score after controls.

Important distinction:

- Correlation is the raw one-to-one relationship.
- Regression is the conditional relationship after accounting for other variables.

If correlation and regression disagree, the trait probably overlaps with pitch type, velocity band, role, or another movement trait.

Current movement-model takeaway:

- Movement traits explain only a modest share of Pitch Value Score.
- Spin Rate and Spin x Velocity are the clearest positive movement signals.
- Velocity by itself is negative after controls, which should be read as a pitch-mix/context finding, not as "velocity is bad."
- IVB is weak after controls in this league-wide model.

## Movement Archetypes

Movement archetypes were clustered with:

- IVB
- HB
- Spin Rate
- Velocity
- Extension

The current clustering selected 4 archetypes:

| Archetype | General Meaning |
|---|---|
| Tight High-Spin Breakers | Slider/curve/cutter shapes with lower IVB and higher spin. |
| Soft-Speed Separation | Changeup/splitter-style shapes with separation and arm-side action. |
| Riding Shape / Lower Velo | Fastball/sinker shapes with ride but less velocity. |
| Riding Power Fastballs | Firmer fastball/sinker shapes with ride and run. |

Average Pitch Value Score by archetype shows which movement families performed best in the current dataset.

## Undervalued Pitches

Undervalued pitches are pitches with strong movement traits but average-or-worse current results.

Current definition:

- Movement quality percentile at least 75
- Pitch Value Score at or below league average

These are scouting targets. They may need better command, usage, sequencing, or pairing to unlock the movement quality.

## Key Files

| File | Purpose |
|---|---|
| `reports/pitch_value_score_leaderboards.md` | Main score explanation and leaderboards. |
| `data/processed/pitch_value_scores_with_type_rank.csv` | Current normalized Pitch Value Score table with pitch-type ranks. |
| `data/processed/pitch_value_scores.csv` | Canonical filename; may be stale if the CSV is open/locked during regeneration. |
| `reports/pitch_value_movement_report.md` | Movement regression, impact tables, correlations, and plots. |
| `data/processed/pitch_value_movement_correlations.csv` | Raw correlations between movement traits and outcomes. |
| `data/processed/pitch_value_movement_regression_coefficients.csv` | Regression coefficients for the interaction movement model. |
| `reports/pitch_movement_archetype_report.md` | Movement clusters, top archetypes, undervalued pitches, scouting notes. |

## Limitations

- The score is descriptive, not a projection system.
- It is not park-adjusted, opponent-adjusted, handedness-adjusted, or count-adjusted.
- It does not directly grade command.
- It does not know whether a pitch was used optimally.
- It does not include scouting looks, injury risk, or role context.
- It should support scouting judgment, not replace it.
