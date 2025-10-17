#index calculation
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
    free_float_shares = [2143595013, 115044088, 445825048, 189468652, 553765588, 1401882474, 52609530]
    outstanding_shares = [4144070045, 423609750, 704548023, 367392511, 1353431345, 3256204436, 119567114]
    base_price = [9675, 35338, 2775, 3049, 2034, 12552, 4845]
    current_price = [10055, 33530, 2916, 3104, 2060, 12508, 5445]

    base_market_capitalization = base_market_cap(outstanding_shares, base_price)
    current_market_capitalization = current_market_cap(free_float_shares, current_price)

    print(base_market_capitalization)
    print(current_market_capitalization)

    index = (current_market_capitalization / base_market_capitalization) * 1000
    print(index)

if __name__ == "__main__":
    main()
