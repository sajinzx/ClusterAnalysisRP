#index calculation
import csv
import pandas as pd
def base_market_cap(outstanding_shares, base_price):
    val = 0
    for i in range(7):
        val += outstanding_shares[i] * base_price[i]
    return val

def current_market_cap(free_float_shares, current_price):
    val = 0
    for i in range(7):
        val += free_float_shares[i] * current_price[i]
    return val

def main():
    allindex=[]
    alldates=[]
    free_float_shares = [2143595013, 115044088, 445825048, 189468652, 553765588, 1401882474, 52609530]
    outstanding_shares = [4144070045, 423609750, 704548023, 367392511, 1353431345, 3256204436, 119567114]
    with open("stockclosingpricesclusterwise.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        base_price = None
        for i, row in enumerate(reader):
            if i >= 41:
                break
            date=row[0]
            daily_prices = [float(price) for price in row[1:]]
            if base_price is None:
                base_price = daily_prices
                continue
            base_market_capitalization = base_market_cap(outstanding_shares, base_price)
            current_market_capitalization = current_market_cap(free_float_shares, daily_prices)
            index = (current_market_capitalization / base_market_capitalization) * 1000
            allindex.append(index)
            alldates.append(date)  

            print(f"Day {i}: Index = {index:.2f}")

    with open("calculated_index.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Index"])
        for date, idx in zip(alldates, allindex):
            writer.writerow([date, idx])

if __name__ == "__main__":
    main()
