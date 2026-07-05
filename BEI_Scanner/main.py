import pandas as pd
from telegram_sender import send_message
from config import STOCKS
from downloader import download_stock
from indicators import calculate_ma
from scoring import calculate_score
from exporter import export_excel

print("=" * 35)
print("     BEI SMART SCREENER")
print("+" * 35)

results = []

for i, stock in enumerate(STOCKS,start=1):
    try:
        df = download_stock(stock)
        df = calculate_ma(df)
        last = df.iloc[-1]
        score = calculate_score(last)
        if score >= 120:
            signal = "BUY"
        elif score >= 80:
            signal = "WATCH"
        else:
            signal = "WAIT"
        results.append({
            "Stock": stock,
            "Close": last["Close"],
            "Score": score,
            "Signal": signal,
            "RSI": round(last["RSI"], 2),
            "Breakout": last["Close"] > last["HIGH20"]
        })
    except Exception as e:
        print(f"{stock} gagal: {e}")
        continue
results = sorted(results, key=lambda x: x["Score"], reverse=True)
message = "📈 TOP 10 HASIL SCREENING\n\n"

for i, r in enumerate(results[:10], start=1):
    message += (
        f"{i}. {r['Stock']}\n"
        f"Score : {r['Score']}\n"
        f"Close : {r['Close']:.0f}\n"
        f"Signal : {r['Signal']}\n"
        f"RSI : {r['RSI']}\n"
        f"Breakout : {r['Breakout']}\n\n"
    )

send_message(message)
print(f"Jumlah hasil : {len(results)}")
export_excel(results)
print("\n===== RANKING SAHAM =====\n")
for i, r in enumerate(results,start=1):
    print(f"{i:2}. {r['Stock']:10} Close:{r['Close']:8.0f} Score:{r['Score']:3} {r['Signal']} Breakout :{r['Breakout']}")