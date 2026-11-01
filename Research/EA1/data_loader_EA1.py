import yfinance as yf 

def load_data(ticker, start="2021-09-13", end="2026-09-14") : 

    data = yf.download(ticker, start= start, end=end , auto_adjust=True)

    

    # Check if data exists
    if data.empty :
        raise ValueError(f"No data found for{ticker}")  


    # Remove rows containing missing va
    data =data.dropna()

    return data





if __name__ == "__main__" : 
    data =load_data("QQQ")
    print(data.head())
    print(data.tail())