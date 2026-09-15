# AyiQuant Research

**Quantitative finance and algorithmic trading research using Python.**

AyiQuant Research is the public research portfolio for selected quantitative finance experiments conducted within the AyiQuant project.

The repository documents research methodology, quantitative experiments, strategy evaluation, and selected results while keeping proprietary implementation details private.

> **Disclaimer:** This repository is for educational and research purposes only. It does not provide investment advice, manage external capital, or represent a registered investment management or financial advisory business. Backtested or simulated performance does not guarantee future results.

## Research Focus

The research focuses on:

* Financial market data analysis
* Quantitative investment strategies
* Algorithmic trading research
* Backtesting methodology
* Risk and performance analysis
* Python-based financial research

## Current Research

### EA1 — Trend-Following Strategy

The first research project investigates a simple trend-following strategy based on exponential moving averages (EMA).

**Core signal:**

* EMA20 > EMA50 → Long position
* EMA20 ≤ EMA50 → No position

The research evaluates whether a simple trend-following approach can generate positive returns and how its performance compares with the underlying market.

### Research Question

> Why can a simple trend-following strategy generate positive returns while still producing relatively weak risk-adjusted performance?

The research focuses on:

* Return generation
* Trade performance
* Volatility
* Drawdowns
* Risk-adjusted performance
* Benchmark comparison
* Strategy robustness

## Baseline Results

**Asset:** QQQ
**Research period:** September 2021 – September 2026

| Metric                |     EA1 |
| --------------------- | ------: |
| Total Return          |  31.23% |
| CAGR                  |   5.57% |
| Annualized Volatility |  15.05% |
| Sharpe Ratio          |    0.44 |
| Maximum Drawdown      | -24.18% |
| Closed Trades         |      12 |

These results represent an initial research baseline and should not be interpreted as evidence of future performance.

## Research Workflow

AyiQuant follows a research-driven workflow:

**Theory → Data → Python Implementation → Backtest → Risk Analysis → Interpretation**

The objective is to understand the behavior and limitations of a strategy before introducing additional complexity.

## Technologies

* Python
* NumPy
* Pandas
* Matplotlib
* Yahoo Finance
* Git

## Repository Structure

```text
AyiQuant-Research/
│
├── Research/
│   └── EA1/
│
├── Charts/
│
└── README.md
```

Only selected research materials are published in this repository. Core strategy implementation and proprietary development code are kept private.

## Status

**Current Phase:** EA1 — Trend-Following Research

The research portfolio is under active development.
