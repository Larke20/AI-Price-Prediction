#import alpaca_trade_api as alpaca
import os
import sys  # Import sys to get command line arguments
# from sentiment_analysis import *
from get_path import *
import yfinance as yf



user_path = get_path()
DIRECTORY_TO_DATA = f"{user_path}AI-Price-Prediction/data"

if __name__ == '__main__':
    # using alpaca
   
    
    # Assign command line arguments to variables
    ticker = sys.argv[1] if len(sys.argv) > 1 else 'TSLA'
    start = sys.argv[2] if len(sys.argv) > 2 else "2022-01-01"
    end = sys.argv[3] if len(sys.argv) > 3 else "2023-08-18"
    timeframe = '1Day'

    # if using alpaca
    # df = api.get_bars(ticker, timeframe, start, end).df
    # df['date'] = df.index.astype(str).str[:10]
    # df = df.reset_index(drop=True)
    
    # if using yfinance
    
    df = yf.download(ticker, start, end)
    df['date'] = df.index
    df = df.reset_index(drop=True)
    df = df.rename(columns = {'Open':'open', 'High':'high', 'Close':'close', 'Low':'low', 'Volume':'volume'})

    #df['sentiment'] = get_sentiments(df)

    df.to_csv(os.path.join(DIRECTORY_TO_DATA, f'{ticker}.csv'), index=False)
    
