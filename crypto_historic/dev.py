import os
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import utility
from dotenv import load_dotenv
import crypto_histdata
from datetime import datetime
from dotenv import load_dotenv
import technical
from tqdm import tqdm
import main
import misc

if __name__ == "__main__":
    # print(main.update_technical(symbol="BTCUSDT",interval="1d"))
    # print(misc.fear_greed())
    # main.fear_greed()
    # print(main.onchain_indicators())
    # print(misc.marketwatch_data())
    # print(main.money_index())
    # print(main.crypto_events())
    # print(misc.get_news())
    # main.crypto_historic(symbol="BTCUSDT", interval="1h")
    # main.crypto_update_latest(symbol="BTCUSDT", interval="1h")
    # main.historical_technical(symbol="BTCUSDT", interval="1m")
    crypto_histdata.insert_klines(
        startyear="2020",
        startmonth="01",
        startday="01",
        symbol="BTCUSDT",
        endyear="",
        endmonth="",
        endday="",
        interval="1m",
    )
    pass
