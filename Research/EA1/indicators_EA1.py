
from data_loader_EA1 import load_data


def calculate_ema(df, span) : 

    
   
    df["EMA" + str(span)] = df["Close"].ewm(span=span, adjust=False).mean()

    

    return df


if __name__ == "__main__":
    df = load_data("QQQ")
    calculate_ema(df, 20)
    calculate_ema(df, 50)


    print(df[["Close", "EMA20", "EMA50"]].tail(10))