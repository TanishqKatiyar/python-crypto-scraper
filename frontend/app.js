document.addEventListener('DOMContentLoaded', () => {
    fetchMarketData();
});

async function fetchMarketData() {
    try {
        const response = await fetch('/api/v1/market');
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('loading').style.display = 'none';
            renderGrid(data.data);
        }
    } catch (error) {
        document.getElementById('loading').innerText = "Failed to synchronize with backend engine.";
        console.error("API Sync Error:", error);
    }
}

function renderGrid(coins) {
    const grid = document.getElementById('crypto-grid');
    grid.innerHTML = '';

    coins.forEach(coin => {
        const isPositive = coin.price_change_24h >= 0;
        const changeClass = isPositive ? 'positive' : 'negative';
        const changeSign = isPositive ? '+' : '';
        const hyperClass = coin.volatility.is_hyper_volatile ? 'hyper-volatile' : '';
        
        // Format Currency
        const formattedPrice = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: coin.current_price < 1 ? 4 : 2
        }).format(coin.current_price);

        const card = document.createElement('div');
        card.className = `coin-card ${hyperClass}`;
        
        card.innerHTML = `
            <div class="coin-header">
                <img src="${coin.image}" class="coin-icon" alt="${coin.name}" loading="lazy"/>
                <div class="coin-info">
                    <h3>${coin.name}</h3>
                    <span class="symbol">${coin.symbol}</span>
                </div>
            </div>
            
            <div class="price-row">
                <div class="current-price">${formattedPrice}</div>
                <div class="change-badge ${changeClass}">
                    ${changeSign}${coin.price_change_24h}%
                </div>
            </div>
            
            <div class="metric-pill">
                ${coin.volatility.indicator} ${coin.volatility.sentiment} (Vol: ${coin.volatility.score})
            </div>
            
            <div class="chart-container">
                <canvas id="chart-${coin.id}"></canvas>
            </div>
        `;
        
        grid.appendChild(card);
        
        // Render Sparkline
        if(coin.sparkline && coin.sparkline.length > 0) {
            renderSparkline(`chart-${coin.id}`, coin.sparkline, isPositive);
        }
    });
}

function renderSparkline(canvasId, dataPoints, isPositive) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    const color = isPositive ? '#22c55e' : '#ef4444';
    const gradient = ctx.createLinearGradient(0, 0, 0, 60);
    gradient.addColorStop(0, isPositive ? 'rgba(34, 197, 94, 0.4)' : 'rgba(239, 68, 68, 0.4)');
    gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: dataPoints.map((_, i) => i),
            datasets: [{
                data: dataPoints,
                borderColor: color,
                borderWidth: 2,
                backgroundColor: gradient,
                fill: true,
                pointRadius: 0,
                pointHoverRadius: 0,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false }, tooltip: { enabled: false } },
            scales: {
                x: { display: false },
                y: { display: false, min: Math.min(...dataPoints) * 0.99, max: Math.max(...dataPoints) * 1.01 }
            },
            interaction: {
                mode: 'index',
                intersect: false,
            },
            animation: {
                duration: 2000,
                easing: 'easeOutQuart'
            }
        }
    });
}
