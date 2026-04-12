from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from .scraper import fetch_crypto_markets

app = FastAPI(title="Python Crypto Scanner Pro", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/market")
def get_market_data():
    """
    Returns the aggressively scraped market data payload,
    bundled with the volatility engine's insights.
    """
    data = fetch_crypto_markets()
    return {"success": True, "count": len(data), "data": data}

# Mount the static frontend
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

@app.get("/")
def serve_index():
    return FileResponse(os.path.join(frontend_dir, "index.html"))
