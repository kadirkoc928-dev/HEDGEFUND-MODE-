import ta

def generate_alpha(df):

    df["EMA20"] = ta.trend.ema_indicator(df["Close"], 20)
    df["EMA50"] = ta.trend.ema_indicator(df["Close"], 50)
    df["RSI"] = ta.momentum.rsi(df["Close"], 14)
    df["VOL"] = df["Volume"].rolling(20).mean()

    last = df.iloc[-1]

    score = 0
    signal = "HOLD"

    # Trend regime
    if last["EMA20"] > last["EMA50"]:
        score += 30

    # Momentum
    if 45 <= last["RSI"] <= 65:
        score += 20

    # Volume expansion
    if df["Volume"].iloc[-1] > last["VOL"] * 1.5:
        score += 25

    # Breakout logic
    if df["Close"].iloc[-1] > df["Close"].max() * 0.98:
        score += 25

    if score >= 80:
        signal = "STRONG BUY"
    elif score >= 60:
        signal = "BUY"
    elif score <= 30:
        signal = "NO TRADE"

    return score, signal
