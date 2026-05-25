# Two-Factor Arbitrage Pricing Theory Model

This project implements a two-factor Arbitrage Pricing Theory (APT) model in Excel. The workbook estimates how two groups of stocks, gold mining firms and technology firms, are exposed to two systematic risk factors: the stock market and gold-price-related movements.

The project combines factor-model estimation with the APT pricing relation. First, stock-level factor loadings are estimated using ordinary least squares (OLS). Then the estimated loadings are averaged by sector and used to compute expected monthly excess returns.

## Project Files

| File | Description |
|---|---|
| `Two-Factor Arbitrage Pricing Theory Model.xlsx` | Excel workbook containing the return data, excess-return calculations, OLS factor-loading estimates, sector averages, and expected excess return forecasts. |
| `Two-Factor Arbitrage Pricing Theory Model.pdf` | Companion explanation document describing the mathematical background, model specification, estimation method, and interpretation of results. |
| `README.md` | Project overview and guide. |

## Model Overview

The workbook uses a two-factor APT framework. For stock $i$ in month $t$, define the stock excess return as

$$
R_{i,t} = r_{i,t} - r_{f,t},
$$

where $r_{i,t}$ is the stock return and $r_{f,t}$ is the risk-free rate. The two factor excess returns are

$$
M_t = r_{\mathrm{MKT},t} - r_{f,t},
$$

and

$$
G_t = r_{\mathrm{GLD},t} - r_{f,t}.
$$

Here, $M_t$ represents the market excess return and $G_t$ represents the excess return on the GLD ETF, used as a factor-mimicking portfolio for gold-price exposure.

For each stock, the empirical regression model is

$$
R_{i,t}
=
\alpha_i
+
\beta_{i,\mathrm{MKT}} M_t
+
\beta_{i,\mathrm{GLD}} G_t
+
\epsilon_{i,t}.
$$

The estimated coefficients have the following interpretation:

- $\alpha_i$ is the intercept, often interpreted as the average excess return not explained by the two factors.
- $\beta_{i,\mathrm{MKT}}$ measures exposure to broad stock market movements.
- $\beta_{i,\mathrm{GLD}}$ measures exposure to gold-price-related movements.
- $\epsilon_{i,t}$ is the residual component of returns not explained by the model.

## Methodology

The project follows these steps:

1. Compute excess returns for each stock, the market factor, and the GLD factor.
2. Estimate stock-level factor loadings using OLS regression.
3. Group the stocks into two sectors: Gold Mining and Technology.
4. Compute sector-average factor loadings.
5. Apply the two-factor APT pricing relation to estimate expected monthly excess returns.

For a sector $s$, the sector-average factor loadings are

$$
\bar{\beta}_{s,k}
=
\frac{1}{n_s}
\sum_{i \in s} \hat{\beta}_{i,k},
$$

where $n_s$ is the number of stocks in sector $s$.

The expected excess return forecast is then computed using

$$
E[R_s]
=
\lambda_{\mathrm{MKT}} \bar{\beta}_{s,\mathrm{MKT}}
+
\lambda_{\mathrm{GLD}} \bar{\beta}_{s,\mathrm{GLD}}.
$$

The factor risk premia used in the workbook are

$$
\lambda_{\mathrm{MKT}} = 0.75\%,
\qquad
\lambda_{\mathrm{GLD}} = 0.15\%.
$$

## Main Results

| Sector | $\bar{\beta}_{\mathrm{GLD}}$ | $\bar{\beta}_{\mathrm{MKT}}$ | $\bar{\alpha}$ | Expected Monthly Excess Return |
|---|---:|---:|---:|---:|
| Gold Mining Stocks | 1.751 | 0.189 | -0.8% | 0.40% |
| Technology Stocks | -0.168 | 0.982 | 1.0% | 0.71% |

The results show a clear difference between the two sectors. Gold mining stocks have strong positive exposure to the GLD factor and relatively weak exposure to the market factor. Technology stocks have market betas close to one and slightly negative exposure to the GLD factor.

## Economic Interpretation

The gold mining sector is mainly driven by gold-price-related systematic risk. Its large positive GLD beta means that its expected excess return is strongly affected by the expected premium on the gold factor.

The technology sector is mainly driven by broad market risk. Its market beta is close to one, so the market factor contributes most of its expected excess return. Its slightly negative GLD beta reduces its forecasted expected excess return by a small amount because the GLD factor premium is positive.

The forecast decomposition is:

| Sector | Market Contribution | GLD Contribution | Total |
|---|---:|---:|---:|
| Gold Mining Stocks | 0.14% | 0.26% | 0.40% |
| Technology Stocks | 0.74% | -0.03% | 0.71% |

## Workbook Structure

The Excel workbook contains three main sheets:

| Sheet | Purpose |
|---|---|
| `Header` | Project title and overview. |
| `Return Data` | Return data, excess-return calculations, and stock-level regression estimates. |
| `Forecasting Expected Returns` | Sector-average factor loadings and expected monthly excess return forecasts. |

## Skills Demonstrated

- Arbitrage Pricing Theory (APT)
- Factor models and systematic risk exposure
- Ordinary least squares regression
- Excel-based financial modeling
- Sector-level risk analysis
- Expected excess return forecasting
- Interpretation of factor loadings and factor risk premia

## Summary

This project shows how APT can be implemented empirically using a two-factor model. The workbook estimates stock-level market and gold factor exposures, aggregates them by sector, and uses the APT pricing relation to compute expected monthly excess returns. The final results highlight the different systematic risk profiles of gold mining and technology stocks.
