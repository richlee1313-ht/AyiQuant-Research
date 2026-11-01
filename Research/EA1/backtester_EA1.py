import numpy as np 
from data_loader_EA1 import load_data
from indicators_EA1 import calculate_ema
from signals_EA1 import generate_trend_signal, generate_trade_events
import matplotlib.pyplot as plt

def calculate_returns(df) :
    
    df["Market Returns"] = df["Close"].pct_change()

    df["Strategy Returns"] = df["Position"] * df["Market Returns"]

    df["Cumulative Return"] = (1 + df["Strategy Returns"]).cumprod()

    df["Benchmark Return"] = (1 + df["Market Returns"]).cumprod()

    df["Strategy Total Return"] = df["Cumulative Return"] - 1
    
    df["Benchmark Total Return"] = df["Benchmark Return"] - 1

    return df 


def calculate_cagr(df) :
    
    years = (df.index[-1] - df.index[0]).days / 365.25

    cagr = (df["Cumulative Return"].iloc[-1] / 1)**(1/years) - 1

    

    return cagr


def calculate_volatility(df) : 

    daily_volatility = df["Strategy Returns"].std()

    annualized_volatility = (daily_volatility*np.sqrt(252))

    return annualized_volatility


def calculate_max_drawdown(df):

   df["Peak"] = df["Cumulative Return"].cummax()

   df["Drawdown"] = (df["Cumulative Return"] - df["Peak"]) / df["Peak"]

   max_drawdown = df["Drawdown"].min()

   return max_drawdown


def calculate_sharpe(df):


    sharpe_ratio = (df["Strategy Returns"].mean() / df["Strategy Returns"].std())*np.sqrt(252)


    

    print("Mean daily return:", df["Strategy Returns"].mean())
    print("Daily volatility:", df["Strategy Returns"].std())
    print("Annualized Sharpe:", sharpe_ratio)
    return sharpe_ratio 


def identify_trade_events(df):

    df["Position Change"] = df["Position"].diff()
    
    df["Trade Event"] = np.select([df["Position Change"] > 0, df["Position Change"] <0], ["Entry", "Exit"], default="Holding" )

    return df


    
def calculate_trade_returns(df):
    # your code here

    trade_groups = df.groupby("Trade ID")

    trade_returns = trade_groups["Strategy Returns"].apply(lambda x: (1 + x).prod() - 1)

    return trade_returns


def trade_counter(df, cagr, max_drawdown): 

    df["Counter"] = np.where(df["Trade Event"] == "Entry", 1, 0).cumsum()

    df["Trade ID"] = df["Counter"].where((df["Position"] == 1) | (df["Trade Event"] == "Exit"))

    
    trade_returns = calculate_trade_returns(df)

    entry_dates = df[df["Position Change"] == 1]

    
    closed_trades = df[df["Trade Event"] == "Exit"]
    number_closed_trades = len(closed_trades)
    closed_trades_returns = trade_returns[trade_returns.index.isin(closed_trades["Trade ID"])]

    trade_durations = closed_trades.index - entry_dates.index[:len(closed_trades)]

    average_trade_duration =trade_durations.mean().days

    median_trade_duration = trade_durations.median().days

    winning_trades = closed_trades_returns[closed_trades_returns > 0]
    losing_trades = closed_trades_returns[closed_trades_returns < 0]

    win_rate = (len(winning_trades) / len(closed_trades_returns)  if len(closed_trades_returns) > 0 else 0)

    average_win = winning_trades.mean() if len(winning_trades) > 0 else 0
    average_loss = losing_trades.mean() if len(losing_trades) > 0 else 0

    expectancy = (win_rate *average_win +(1-win_rate) *average_loss)

    gross_profit = winning_trades.sum()
    gross_loss = abs(losing_trades.sum())
    profit_factor = (gross_profit /gross_loss) if gross_loss > 0 else np.inf

    downside_returns = df["Strategy Returns"][df["Strategy Returns"] < 0]
    downside_volatility = downside_returns.std()

    annualized_mean_return = df["Strategy Returns"].mean() * 252
    annualized_downside_volatility = downside_volatility*np.sqrt(252)

    sortino_ratio = (annualized_mean_return / annualized_downside_volatility if annualized_downside_volatility > 0 else np.inf)

    calmar_ratio = cagr / abs(max_drawdown)

    

    print(trade_durations)
    print("Average Trade Duration :", average_trade_duration, "days.")
    print("Median Trade Duration :", median_trade_duration, "days.")
    print()

    print(downside_returns)
    print("Downside volatility:", downside_volatility)
    print("Annualized Downside volatility:", annualized_downside_volatility)
    print("Sortino Ratio :", sortino_ratio)
    print("Calmar Ratio :", round(calmar_ratio, 2))
    print()
    print("Number of Closed Trades:", number_closed_trades)
    print(closed_trades[["Trade Event", "Trade ID"]])
    print()
    print(winning_trades)
    print("\n_______________")
    print(losing_trades)
    print()
    print(closed_trades_returns)
    print("Win Rate :", round(win_rate*100,2), "%")
    print()
    print("Average Win:", round(average_win * 100, 2), "%")
    print("Average Loss:", round(average_loss * 100, 2), "%")
    print("Expectancy:", round(expectancy*100,2),"%")
    print()
    print("Gross Profit:", round(gross_profit*100,2),"%")
    print("Gross Loss:", round(gross_loss*100,2),"%")
    print("Profit Factor:", round(profit_factor,2))




    

    # print(entry_dates[["Position", "Position Change", "Trade Event", "Trade ID"]])

    # print(trade_returns)

    return df


if __name__ == "__main__":
    df = load_data("QQQ")

    calculate_ema(df, 20)
    calculate_ema(df, 50)

    generate_trend_signal(df)
    generate_trade_events(df)
    identify_trade_events(df)
    calculate_returns(df)

    cagr = calculate_cagr(df)
    annualized_volatility = calculate_volatility(df)
    max_drawdown = calculate_max_drawdown(df)
    sharpe_ratio = calculate_sharpe(df)

    df =trade_counter(df,cagr, max_drawdown)

    #print(df[df["Position"] == 0][["Close", "Signal", "Position", "Market Returns", "Strategy Returns", "Cumulative Return", "Benchmark Return"]].tail(10))
    #print(df[["Strategy Total Return", "Benchmark Total Return"]].tail(1))
    print(df[["Position", "Position Change", "Trade Event", "Trade ID", "Counter"]].tail(30))


    print()
    print("CAGR:", round(cagr*100,2),"%")
    print("Annualized Volatility:", round(annualized_volatility*100,2),"%")

    print()
    print("Max Drawdown :", round(max_drawdown*100,2),"%")
    print("Sharpe Ratio :", round(sharpe_ratio,2))






    plt.figure(figsize=(10,5))

    plt.plot(df.index, df["Cumulative Return"], label = "EMA Strategy")
    plt.plot(df.index, df["Benchmark Return"], label = "Benchmark")

    plt.title("AyiQuant Backtester EA1 v.01")

    plt.xlabel("Date")

    plt.ylabel("Growth of $1")


    plt.grid()

    plt.legend()


    #plt.show()

    