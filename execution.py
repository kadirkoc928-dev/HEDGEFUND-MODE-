portfolio = {}

def execute_trade(symbol, signal, price):

    if signal == "STRONG BUY":
        portfolio[symbol] = {
            "entry": price,
            "status": "LONG"
        }

    elif signal == "NO TRADE":
        if symbol in portfolio:
            del portfolio[symbol]

    return portfolio
