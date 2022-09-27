import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg

price_history = yf.Ticker('TSLA').history(period='2y', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1wk', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)
sg.Window(title="Test Prog", layout=[[]], margins=(100, 50)).read()

##https://realpython.com/pysimplegui-python/