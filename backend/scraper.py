import requests
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 50,
    'page': 1,
    'sparkline': True,
    'price_change_percentage': '24h'
}

def analyze_volatility(coin):
    """
    Algorithmic volatility scanner triggering alerts for highly traded assets.
    """
    price_change_24h = coin.get('price_change_percentage_24h', 0)
    if price_change_24h is None:
        price_change_24h = 0
        
    volatility_score = abs(price_change_24h)
    
    # Label "Extreme" if swing is past 10% in 24 hours
    is_hyper = volatility_score > 10.0
    sentiment = "Bullish Focus" if price_change_24h > 0 else "Bearish Drop"
    
    return {
        "score": round(volatility_score, 2),
        "is_hyper_volatile": is_hyper,
        "sentiment": sentiment,
        "indicator": "🚀" if is_hyper and price_change_24h > 0 else "⚠️" if is_hyper else "📊"
    }

def fetch_crypto_markets():
    """
    Core engine wrapper fetching payload and running volatility framing logic.
    """
    try:
        logger.info(f"Dispatching query vector to {API_URL}")
        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()
        
        raw_data = response.json()
        processed_data = []
        
        for coin in raw_data:
            volatility_metrics = analyze_volatility(coin)
            
            # Map robust dataset
            processed_data.append({
                "id": coin.get("id"),
                "symbol": str(coin.get("symbol")).upper(),
                "name": coin.get("name"),
                "image": coin.get("image"),
                "current_price": coin.get("current_price"),
                "market_cap": coin.get("market_cap"),
                "price_change_24h": round(coin.get("price_change_percentage_24h", 0) or 0, 2),
                "sparkline": coin.get("sparkline_in_7d", {}).get("price", []),
                "volatility": volatility_metrics
            })
            
        return processed_data
    except Exception as e:
        logger.error(f"Upstream pipeline sync failed: {e}")
        return []

if __name__ == "__main__":
    data = fetch_crypto_markets()
    print(f"Scraped {len(data)} nodes.")
