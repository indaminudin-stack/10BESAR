def calculate_ma(df):
    #Moving Average
    df["MA5"] = df["Close"].rolling(5).mean()
    df["MA20"] = df["Close"].rolling(20).mean()
    # Volume rata-rata 20 hari
    df["VOL20"] = df["Volume"].rolling(20).mean()
    delta = df["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))

    # Harga tertinggi 20 hari sebelumnya
    df["HIGH20"] = df["High"].rolling(20).max().shift(1)

    # MACD
    df["EMA12"] = df["Close"].ewm(span=12,adjust=False).mean()
    df["EMA26"] = df["Close"].ewm(span=23,adjust=False).mean()

    df["MACD"] = df["EMA12"] - df["EMA26"]
    df["SIGNAL"] = df["MACD"].ewm(span=9,adjust=False).mean()
    
    return df