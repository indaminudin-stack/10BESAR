def calculate_score(last):
    score = 0
    # Trend
    if last["Close"] > last["MA20"]:
        score += 30
    # Momentum
    if last["MA5"] > last["MA20"]:
        score += 30
    # Volume meningkat
    if last["Volume"] > last["VOL20"]:
         score += 20    
    # Harga di atas MA5
    if last["Close"] > last["MA5"]:
           score += 20
    if 50 <= last["RSI"] <= 70:
         score += 20     
    # Breakout
    if last["Close"] > last["HIGH20"]:
         score += 30
    # MACD diatas Signal
    if last["MACD"] > last["SIGNAL"]:
         score += 20
    return score