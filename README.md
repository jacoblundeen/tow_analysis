# Warhammer: The Old World — Tournament Win Rate Analysis

A statistical analysis of competitive win rates across armies ("factions") in Games Workshop's *Warhammer: The Old World*, using real tournament results.

## Overview

Tabletop wargames like *The Old World* are balanced by adjusting rules based on tournament performance data. This project asks: **are the game's factions actually balanced**, based on real-world tournament results — and if not, which ones are over- or under-performing?

## Data

Match data is sourced from [Woehammer](https://woehammer.com), which compiles results scraped from tournament-tracking platforms such as [Best Coast Pairings](https://bestcoastpairings.com). After cleaning, the working dataset contains **3,190 individual game results** across 16 factions, capturing faction/subfaction matchups, points level, number of rounds, ruleset, and player count.

### Data Processing (`tow_data_processing.py`)
Raw export data is cleaned and reshaped before analysis:
- Column names normalized (lowercase, no whitespace/special characters)
- Faction names shortened for readability in charts
- Subfactions inferred by parsing each player's army list URL
- Mirror matches and incomplete records removed
- Data reshaped from one-row-per-game to one-row-per-player-per-game, so each player's result can be analyzed independently of whether they were "player 1" or "player 2" in the raw export

## Analysis (`tow_analysis_16_june.ipynb`)

- **Faction win rates**: overall win rate per faction, benchmarked against a "balanced" range of 45–55%
- **Logistic regression**: `result ~ player_faction + C(rounds) + ruleset`, to test which factions significantly over- or under-perform
- **Linear regression**: `win_rate ~ player_faction + C(rounds) + ruleset`, plus an ANOVA breakdown of which variables matter
- **Win rate breakdowns** by points level, player count, number of rounds, and ruleset

## Key Findings

- 11 of 16 factions fall within the accepted 45–55% win rate band
- Of the 4 outliers, 3 (Empire, Skaven, Ogre Kingdoms) sit below 45%; Kingdom of Bretonnia is the only faction above 55%
- Points level and player count were not statistically significant in either model; faction, rounds, and ruleset were
- Skaven were significant (under-performing) in both models; Empire was also significant in the logistic model

## Tools

Python, pandas, NumPy, [plotnine](https://plotnine.org/) (ggplot2-style visualization), statsmodels (logistic & linear regression, ANOVA), patsy

## Repo Contents

| File | Description |
|---|---|
| `tow_data_processing.py` | ETL script — cleans the raw export and produces `tow_processed_16_june.csv` |
| `tow_analysis_16_june.ipynb` | Main analysis notebook (current) |
| `tow_16_june.xlsx` | Raw tournament data export |
| `tow_processed_16_june.csv` | Cleaned dataset used in the analysis |
| `tow_analysis_24_april.ipynb`, `tow_analysis.ipynb` | Earlier iterations, kept for history |

*This is an ongoing personal project — the analysis is updated periodically as more tournament data becomes available.*
