import yfinance as yf
def download_stock(stock):
    df = yf.download( stock, period="1mo", progress=False, auto_adjust=False
    )
    df.columns = df.columns.get_level_values(0)
    return df