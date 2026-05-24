import yfinance as yf

def get_realtime(symbol):
    df = yf.Ticker(symbol).history(period="1d", interval="1m")
    return df
