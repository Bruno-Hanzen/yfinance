#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 20:26:39 2020

@author: bruno
"""

import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max", rounding = False, auto_adjust=False
                    )

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits