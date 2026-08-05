<div align="center">

# 📈 Python Crypto Scraper

**Real-time cryptocurrency price scraper with automated alerts and data pipelines.**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-43B02A?style=for-the-badge)](https://pypi.org/project/beautifulsoup4/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

</div>

---

## Overview

A lightweight yet powerful cryptocurrency price scraper that monitors live market data, detects significant price movements, and triggers configurable alerts. Built with async Python for high-throughput data collection.

## Features

- **Real-Time Monitoring** — Track prices across multiple exchanges simultaneously
- **Price Alerts** — Configurable thresholds for percentage-based and absolute price changes
- **Data Export** — CSV and JSON export with timestamped snapshots
- **Async Pipeline** — Non-blocking I/O for monitoring 50+ coins concurrently
- **Rate Limiting** — Respectful scraping with configurable request intervals
- **Historical Data** — Store and query historical price data for trend analysis

## Tech Stack

| Component | Technology |
|:----------|:-----------|
| Language | Python 3.11 |
| Scraping | BeautifulSoup4, Requests |
| Async | asyncio, aiohttp |
| Data | Pandas, CSV |
| Scheduling | APScheduler |

## Quick Start

```bash
# Clone
git clone https://github.com/TanishqKatiyar/python-crypto-scraper.git
cd python-crypto-scraper

# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env

# Run
python main.py
```

## Configuration

Edit `.env` to customize:

```env
SCRAPE_INTERVAL=60          # Seconds between scrapes
ALERT_THRESHOLD=5.0         # % change to trigger alert
COINS=BTC,ETH,SOL,DOGE      # Coins to monitor
OUTPUT_FORMAT=csv            # csv or json
```

## Project Structure

```
python-crypto-scraper/
├── main.py              # Entry point
├── scraper/
│   ├── collector.py     # Price data collection
│   ├── parser.py        # HTML parsing logic
│   └── alerts.py        # Alert system
├── data/
│   └── exports/         # Exported price data
├── requirements.txt
└── .env.example
```

## License

[MIT](./LICENSE)
