def position_size(account_balance, risk_pct, atr, price):

    risk_amount = account_balance * risk_pct

    if atr == 0:
        return 0

    size = risk_amount / atr

    max_shares = account_balance / price

    return min(size, max_shares)


def max_daily_loss(account_balance):
    return account_balance * 0.02  # 2% max loss per day
