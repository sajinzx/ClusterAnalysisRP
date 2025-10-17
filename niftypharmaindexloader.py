import yfinance as yf
import pandas as pd


ticker = "^CNXPHARMA"


start_date = "2025-08-14"
end_date = "2025-10-14"


data = yf.download(ticker, start=start_date, end=end_date)

closing_index=data[['Close']]

print(closing_index)


closing_index.to_csv("nifty_pharma_2025.csv",index_label="Date")
