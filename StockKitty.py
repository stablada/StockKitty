import yfinance as yf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import streamlit as st

st.write("""
# Stock Kitty
Price analysis of the stock of your choice!
""")

tksym = 'AAPL'
tk = yf.Ticker(tksym)
hist = tk.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(hist.Close)
st.line_chart(hist.Volume)