import numpy as np
from data_loader_EA1 import load_data
from indicators_EA1 import calculate_ema

def generate_trend_signal (df) :

    df["Signal"] = np.where(df["EMA20"] > df["EMA50"], 1,0)

    return df


def generate_trade_events(df) : 

    df["Position"] = df["Signal"].shift(1)
    df["Signal Change"] = df["Signal"].diff()
    df["Event"] = np.select([df["Signal Change"] > 0, df["Signal Change"] <0], ["Entry", "Exit"], default="Holding" )

    return df

if __name__ == "__main__":
    df = load_data("QQQ")
    calculate_ema(df, 20)
    calculate_ema(df, 50)
    generate_trend_signal(df)
    generate_trade_events(df)

    print(df[["Close", "EMA20", "EMA50", "Signal", "Signal Change", "Event"]].tail(30))