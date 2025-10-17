import yfinance as yf
import pandas as pd

tickers=[
    "SUNPHARMA.NS",
    "CIPLA.NS",
    "DRREDDY.NS",
    "DIVISLAB.NS",
    "LAURUSLABS.NS",
    "LUPIN.NS",
    "ALKEM.NS",
    "TORNTPHARM.NS",
    "AUROPHARMA.NS",
    "IPCALAB.NS",
    "GLAND.NS",
    "ABBOTINDIA.NS",
    "ZYDUSLIFE.NS",
    "PFIZER.NS",
    "GLAXO.NS",
    "GLENMARK.NS",
    "NATCOPHARM.NS",
    "SANOFI.NS",
    "GRANULES.NS",
    "BIOCON.NS"
]

start_date = "2025-08-14"
end_date = "2025-10-15"

data = yf.download(tickers, start=start_date, end=end_date)["Close"]

print(data)

data.to_csv("stockclosingprices.csv")