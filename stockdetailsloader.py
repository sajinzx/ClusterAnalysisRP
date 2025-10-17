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
    "MANKIND.NS",
    "JBCHEPHARM.NS",
    "GLENMARK.NS",
    "NATCOPHARM.NS",
    "AJANTPHARM.NS",
    "GRANULES.NS",
    "BIOCON.NS"
]

cluster1 = ["AUROPHARMA.NS", "CIPLA.NS", "DRREDDY.NS", "GLENMARK.NS", "LUPIN.NS", "NATCOPHARM.NS", "ZYDUSLIFE.NS"]
cluster2 = ["ABBOTINDIA.NS", "MANKIND.NS"] 
cluster3 = ["GLAND.NS", "LAURUSLABS.NS"]
cluster4 = ["AJANTPHARM.NS", "GRANULES.NS"]  
cluster5 = ["BIOCON.NS","JBCHEPHARM.NS"]  
cluster6 = ["DIVISLAB.NS", "IPCALAB.NS", "SUNPHARMA.NS", "TORNTPHARM.NS"]
cluster7 = ["ALKEM.NS"]


clusters = {
    "cluster1": cluster1,
    "cluster2": cluster2,
    "cluster3": cluster3,
    "cluster4": cluster4,
    "cluster5": cluster5,
    "cluster6": cluster6,
    "cluster7": cluster7
}

start_date = "2025-08-14"
end_date = "2025-10-15"

data = yf.download(tickers, start=start_date, end=end_date)["Close"]

print(data)

data.to_csv("stockclosingprices.csv")

cluster_sums = pd.DataFrame(index=data.index)
for cname, stocks in clusters.items():
    valid_stocks = [s for s in stocks if s in data.columns]
    cluster_sums[cname] = data[valid_stocks].sum(axis=1)

cluster_sums.to_csv("stockclosingpricesclusterwise.csv")

print(cluster_sums.head())
