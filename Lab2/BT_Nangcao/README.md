# Lab 2 - Advanced: SARIMA on Airline Passengers

## Overview
Lab 2 (advanced level) of the Time Series course. The goal is to handle a
seasonal series: choose d and D, read the seasonal orders (P, Q) from ACF/PACF,
fit a SARIMA model and compare it with ARIMA.

## Dataset
Dataset 2 - Airline Passengers (`airline-passengers.csv`): monthly international
airline passengers (thousands), 144 observations, 01/1949 - 12/1960,
seasonal period s = 12.
Link: https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv

## Analysis
- Time series plot, trend and seasonality identification
- ADF test on the original series (not stationary)
- Log transform, regular differencing (d = 1) and seasonal differencing (D = 1, s = 12)
- ACF and PACF analysis to determine (p, q, P, Q)
- Fit SARIMA candidates from the ACF/PACF step, select by AIC/BIC, residual diagnostics (Ljung-Box)
- Forecast on the test set (1958-1960) and evaluate with MAE, RMSE (and MAPE)
- Comparison with ARIMA (no seasonal part) on the same train/test split

## Project Structure
- data/raw - Original dataset (airline-passengers.csv)
- src/ - Code, one notebook per step:
  - Lab2_Nangcao.ipynb - Step 1: plot and seasonality
  - Lab_2.ipynb - Step 2: ADF test on the original series
  - Buoc3_lab2_NangCao.ipynb - Step 3: regular + seasonal differencing
  - Bai4_Nangcao.ipynb - Step 4: ACF/PACF, determine (p, q, P, Q)
  - Bai5_Nangcao.ipynb - Steps 5-7: SARIMA fit, forecast and evaluation, comparison with ARIMA
  - proc_data.py - Data processing (empty for now)
- Task/ - Lab description: Lab2_2_descript.md, proess.md

## Installation
pip install -r requirement.txt

## Instructions for use
Open the notebooks in src/ and run all cells, in the order of the steps above.
The notebooks download the data from the link above, so an internet connection is
required; data/raw/airline-passengers.csv is the local copy of the same file.
