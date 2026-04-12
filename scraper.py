import requests
import pandas as pd
import json
import time

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 50,
    'page': 1,
    'sparkline': False
}

def fetch_crypto_data():
    print(f"[*] Dispatching highly-concurrent scraper to {API_URL}...")
    try:
        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"[!] HTTP Error during scraping: {err}")
    except Exception as err:
        print(f"[!] Target server rejected connection: {err}")
    return None

def analyze_and_export(data):
    if not data:
        return
    
    print("[*] Compiling pandas DataFrame architecture")
    df = pd.DataFrame(data)
    export_df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume']]
    
    filename = "crypto_market_analysis.csv"
    export_df.to_csv(filename, index=False)
    print(f"[+] Output materialized successfully into {filename}")
    
if __name__ == "__main__":
    market_data = fetch_crypto_data()
    analyze_and_export(market_data)
