# Lab 2 - Normal: ARIMA on Monthly Drug Sales (a10)

## Overview
Lab 2 (basic level) of the Time Series course. The goal is to make a series
stationary, choose the orders (p, d, q) from ACF/PACF, fit ARIMA/SARIMA models
and evaluate their forecasts.

## Dataset
Dataset 1 - Monthly Retail Sales `a10.csv` (monthly drug sales, Australia),
204 observations, 07/1991 - 06/2008, seasonal period s = 12.
Link: https://raw.githubusercontent.com/selva86/datasets/master/a10.csv

## Analysis
- Exploratory data analysis (EDA): trend, seasonality, rolling mean
- ADF stationarity test on the original series
- Differencing (d = 1) and log transform, ADF re-test
- ACF and PACF analysis to suggest (p, d, q)
- ARIMA(1,1,1) vs ARIMA(2,1,1) selected by AIC/BIC
- Residual diagnostics (Ljung-Box) and forecast on the test set (MAE, RMSE, MAPE)
- Extension: SARIMA(p,d,q)(P,D,Q)12 and comparison with ARIMA

## Project Structure
- data/raw - Original dataset (a10.csv)
- src/ - Code, one notebook per exercise:
  - Lab2_Normal.ipynb - Exercises 1-4 (first draft)
  - Bai2_Lab2.ipynb - Exercise 2: ADF test
  - Bai3.ipynb - Exercise 3: differencing and ADF re-test
  - Bai4.ipynb - Exercise 4: ACF/PACF
  - Bai5.ipynb - Exercise 5: ARIMA/SARIMA, diagnostics, forecast
  - proc_data.py - Data processing (empty for now)
- Task/ - Lab description: Lab2_1_descript.md, proess.md

## Installation
pip install -r requirement.txt

## Instructions for use
Open the notebooks in src/ and run all cells, in the order Bai2 -> Bai3 -> Bai4 -> Bai5.
Most notebooks download the data from the link above, so an internet connection is
required; data/raw/a10.csv is the local copy of the same file.
