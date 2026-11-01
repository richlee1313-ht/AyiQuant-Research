# AyiQuant Research

**Quantitative Finance | Algorithmic Trading | Python-Based Research**

AyiQuant Research is the public research portfolio for selected quantitative finance experiments conducted within the AyiQuant project.

The repository documents research methodologies, quantitative experiments, strategy evaluation, backtesting, and risk analysis.

Selected research code and findings are publicly available, while proprietary strategy development and execution infrastructure remain private.

> **Disclaimer:** This repository is for educational and research purposes only. It does not provide investment advice, manage external capital, or represent a registered investment management or financial advisory business. Backtested or simulated performance does not guarantee future results.

## Research Focus

The research focuses on financial market data analysis, quantitative investment strategies, algorithmic trading research, backtesting methodology, risk and performance measurement, and Python-based financial research.

## EA1 — EMA Trend-Following Strategy

**Status: Frozen — Exploratory Backtesting Study**

### Research Question

Why can a simple trend-following strategy generate positive historical returns while exhibiting relatively weak risk-adjusted performance?

### Strategy Overview

EA1 uses a simple moving-average crossover approach:

| Condition | Position |
|---|---|
| EMA20 > EMA50 | Long |
| EMA20 ≤ EMA50 | Flat |

The strategy uses daily price data and shifts positions by one trading day to avoid using the current day's closing signal for the same day's return.

### Research Configuration

| Parameter | Setting |
|---|---|
| Instrument | QQQ ETF |
| Research Period | September 2021 – September 2026 |
| Data Source | Yahoo Finance |
| Price Adjustment | Adjusted |
| Frequency | Daily |
| Indicators | EMA20 / EMA50 |
| Trading Direction | Long / Flat |
| Transaction Costs | Excluded |
| Risk-Free Rate | Assumed zero |

## Historical Performance

### EA1 vs. QQQ Buy-and-Hold

| Metric | EA1 | QQQ |
|---|---:|---:|
| CAGR | 5.57% | 14.39% |
| Annualized Volatility | 15.05% | 23.00% |
| Sharpe Ratio | 0.44 | 0.70 |
| Maximum Drawdown | -24.18% | -35.12% |

EA1 generated positive historical returns while reducing volatility and maximum drawdown relative to QQQ.

However, its lower CAGR and Sharpe ratio indicate that it underperformed passive QQQ investing in both absolute and risk-adjusted returns.

### Trade-Level Findings

| Metric | Result |
|---|---:|
| Completed Trades | 12 |
| Win Rate | 50.00% |
| Average Winning Trade | +10.42% |
| Average Losing Trade | -4.96% |
| Average Return per Completed Trade | +2.73% |
| Market Exposure | Approximately 68.18% |

The three largest winning trades generated a combined +53.43 percentage points when their individual returns were summed. The remaining nine completed trades collectively generated −20.69 percentage points using the same calculation.

These values represent sums of individual trade returns, not compounded portfolio returns.

## Research Findings

The historical results are consistent with three characteristics of trend-following strategies.

**Performance concentration:** A relatively small number of substantial winning trades contributed disproportionately to total trade-level profitability.

**Reduced market exposure:** EA1 remained outside the market for approximately 32% of the observed trading days, which may have helped reduce market risk while limiting upside participation.

**Lagging signals:** EMA crossovers respond to historical prices, potentially delaying entries and exits.

These mechanisms are plausible explanations for the observed performance, but their separate contributions were not quantitatively isolated.

## Research Limitations

- Only 12 completed trades were analyzed.
- The study evaluated a single instrument over one historical period.
- Transaction costs and slippage were excluded.
- Independent out-of-sample validation was not performed.
- Execution assumptions were simplified.
- The results do not establish a statistically validated trading edge.

## Research Methodology

**Theory → Data → Python Implementation → Backtest → Risk Analysis → Interpretation**

The objective is to understand how a strategy behaves and identify its limitations before introducing additional complexity.

The original EMA20/50 strategy parameters were preserved without optimization during the final research phase.

## Research Materials

The EA1 research materials are located in [`Research/EA1`](Research/EA1).

They include the research notebook, selected supporting Python modules, and historical performance outputs.

## Technologies

Python, NumPy, Pandas, Matplotlib, Yahoo Finance, Jupyter Notebook, and Git.

## Research Status

**EA1 v0.1: Completed and Frozen**

EA1 is retained as an exploratory quantitative research study, not a production-ready trading system.

Future AyiQuant research projects will investigate additional strategies, methodologies, and market behaviors independently of this frozen baseline.

---

**AyiQuant Research — Building quantitative investment knowledge through transparent experimentation and evidence-based analysis.**
