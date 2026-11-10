<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>RSH Coin - Mini App</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: rgba(30, 41, 59, 0.7);
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.4);
            --gold: #facc15;
            --text-main: #ffffff;
            --text-secondary: #94a3b8;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background: var(--bg-color);
            color: var(--text-main);
            display: flex;
            flex-direction: column;
            height: 100vh;
            overflow: hidden;
            user-select: none;
        }

        /* Шапка профиля */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 20px;
            background: var(--card-bg);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .user-info {
            font-size: 14px;
            color: var(--text-secondary);
        }

        .balance-box {
            text-align: right;
        }

        .balance-value {
            font-size: 20px;
            font-weight: bold;
            color: var(--gold);
        }

        /* Основной контент по вкладкам */
        .content {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            overflow-y: auto;
        }

        .tab-pane {
            display: none;
            width: 100%;
            height: 100%;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .tab-pane.active {
            display: flex;
        }

        /* Кликер */
        .clicker-container {
            text-align: center;
        }

        .coin-target {
            width: 180px;
            height: 180px;
            background: radial-gradient(circle, #fde047 0%, #ca8a04 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            font-weight: bold;
            color: #713f12;
            box-shadow: 0 0 40px rgba(202, 138, 4, 0.5);
            cursor: pointer;
            margin: 20px auto;
            transition: transform 0.08s ease;
            position: relative;
        }

        .coin-target:active {
            transform: scale(0.90);
        }

        .stats-text {
            color: var(--text-secondary);
            font-size: 14px;
            margin-top: 10px;
        }

        /* Магазин и Донаты */
        .shop-list {
            width: 100%;
            max-width: 400px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .shop-card {
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .shop-card-info h4 {
            font-size: 16px;
            margin-bottom: 4px;
        }

        .shop-card-info p {
            font-size: 12px;
            color: var(--text-secondary);
        }

        .btn-buy {
            background: linear-gradient(135deg, #38bdf8, #2563eb);
            color: white;
            border: none;
            padding: 8px 14px;
            border-radius: 10px;
            font-weight: bold;
            cursor: pointer;
            font-size: 13px;
        }

        .btn-donate {
            background: linear-gradient(135deg, #ec4899, #8b5cf6);
        }

        /* Нижняя навигация */
        .nav-bar {
            display: flex;
            background: var(--card-bg);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            height: 60px;
        }

        .nav-item {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
            font-size: 12px;
            cursor: pointer;
            transition: color 0.2s;
            background: none;
            border: none;
        }

        .nav-item.active {
            color: var(--accent);
        }

        .nav-item span {
            font-size: 18px;
            margin-bottom: 2px;
        }
    </style>
</head>
<body>

    <!-- Шапка -->
    <div class="header">
        <div class="user-info" id="username">RSH Player</div>
        <div class="balance-box">
            <div style="font-size: 11px; color: var(--text-secondary);">БАЛАНС</div>
            <div class="balance-value"><span id="score">0</span> RSH</div>
        </div>
    </div>

    <!-- Контент -->
    <div class="content">
        
        <!-- Вкладка 1: Кликер -->
        <div class="tab-pane active" id="tab-clicker">
            <div class="clicker-container">
                <div style="font-size: 13px; color: var(--accent); text-transform: uppercase; letter-spacing: 1px;">Майнинг монет</div>
                <div class="coin-target" id="clickCoin">RSH</div>
                <div class="stats-text">Сила клика: +<span id="clickPower">1</span> RSH</div>
                <div class="stats-text">Авто-доход: +<span id="autoIncome">0</span> RSH/сек</div>
            </div>
        </div>

        <!-- Вкладка 2: Магазин и Донаты (Stars) -->
        <div class="tab-pane" id="tab-shop">
            <div class="shop-list">
                <div class="shop-card">
                    <div class="shop-card-info">
                        <h4>⚡ Улучшение клика</h4>
                        <p>+1 к силе каждого клика</p>
                    </div>
                    <button class="btn-buy" id="buyPowerBtn">50 RSH</button>
                </div>

                <div class="shop-card">
                    <div class="shop-card-info">
                        <h4>🤖 Авто-майнер</h4>
                        <p>Добывает +1 RSH каждую секунду</p>
                    </div>
                    <button class="btn-buy" id="buyAutoBtn">150 RSH</button>
                </div>

                <div class="shop-card">
                    <div class="shop-card-info">
                        <h4>⭐ Звездный буст (Донат)</h4>
                        <p>Мгновенно +5000 RSH за Telegram Stars</p>
                    </div>
                    <button class="btn-buy btn-donate" id="donateStarsBtn">Купить ⭐</button>
                </div>
            </div>
        </div>

        <!-- Вкладка 3: Мини-игры -->
        <div class="tab-pane" id="tab-games">
            <div style="text-align: center; max-width: 320px;">
                <h3 style="margin-bottom: 10px; color: var(--gold);">🎲 Ежедневный бонус</h3>
                <p style="color: var(--text-secondary); font-size: 13px; margin-bottom: 20px;">Испытай удачу и получи случайную награду прямо на баланс!</p>
                <button class="btn-buy" id="dailyBonusBtn" style="padding: 12px 24px; font-size: 15px; width: 100%;">Забрать бонус (+250 RSH)</button>
            </div>
        </div>

    </div>

    <!-- Нижнее меню -->
    <div class="nav-bar">
        <button class="nav-item active" onclick="switchTab('clicker', this)">
            <span>🪙</span>Майнинг
        </button>
        <button class="nav-item" onclick="switchTab('shop', this)">
            <span>⭐</span>Донат / Магазин
        </button>
        <button class="nav-item" onclick="switchTab('games', this)">
            <span>🎮</span>Игры
        </button>
    </div>

    <script>
        let tg = window.Telegram.WebApp;
        tg.expand();

        // Данные игрока
        let score = 0;
        let clickPower = 1;
        let autoIncome = 0;
        let powerCost = 50;
        let autoCost = 150;

        // Элементы интерфейса
        const scoreEl = document.getElementById('score');
        const clickCoin = document.getElementById('clickCoin');
        const clickPowerEl = document.getElementById('clickPower');
        const autoIncomeEl = document.getElementById('autoIncome');
        const buyPowerBtn = document.getElementById('buyPowerBtn');
        const buyAutoBtn = document.getElementById('buyAutoBtn');
        const donateStarsBtn = document.getElementById('donateStarsBtn');
        const dailyBonusBtn = document.getElementById('dailyBonusBtn');
        const usernameEl = document.getElementById('username');

        if (tg.initDataUnsafe && tg.initDataUnsafe.user) {
            usernameEl.innerText = tg.initDataUnsafe.user.first_name || "RSH Player";
        }

        // Переключение вкладок
        function switchTab(tabName, element) {
            document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            
            document.getElementById('tab-' + tabName).classList.add('active');
            element.classList.add('active');
        }

        // Клик по монете
        clickCoin.addEventListener('click', (e) => {
            score += clickPower;
            updateUI();
            createFlyText(e.clientX, e.clientY, `+${clickPower}`);
        });

        // Покупка силы клика
        buyPowerBtn.addEventListener('click', () => {
            if (score >= powerCost) {
                score -= powerCost;
                clickPower += 1;
                powerCost = Math.floor(powerCost * 1.6);
                buyPowerBtn.innerText = `${powerCost} RSH`;
                clickPowerEl.innerText = clickPower;
                updateUI();
            } else {
                alert('Недостаточно RSH монет!');
            }
        });

        // Покупка авто-дохода
        buyAutoBtn.addEventListener('click', () => {
            if (score >= autoCost) {
                score -= autoCost;
                autoIncome += 1;
                autoCost = Math.floor(autoCost * 1.7);
                buyAutoBtn.innerText = `${autoCost} RSH`;
                autoIncomeEl.innerText = autoIncome;
                updateUI();
            } else {
                alert('Недостаточно RSH монет!');
            }
        });

        // Донат через Telegram Stars (или заглушка)
        donateStarsBtn.addEventListener('click', () => {
            if (tg.initDataUnsafe && tg.initDataUnsafe.user) {
                alert('Переход к оплате через Telegram Stars...');
                tg.sendData(JSON.stringify({action: "buy_stars_boost", user_id: tg.initDataUnsafe.user.id}));
            } else {
                score += 5000;
                alert('Тест доната: вам зачислено +5000 RSH!');
                updateUI();
            }
        });

        // Ежедневный бонус
        let lastBonusTime = 0;
        dailyBonusBtn.addEventListener('click', () => {
            let now = Date.now();
            if (now - lastBonusTime < 60000) {
                alert('Бонус можно забирать раз в минуту! Подождите.');
                return;
            }
            lastBonusTime = now;
            score += 250;
            alert('Вы получили ежедневный бонус +250 RSH!');
            updateUI();
        });

        // Авто-майнинг каждую секунду
        setInterval(() => {
            if (autoIncome > 0) {
                score += autoIncome;
                updateUI();
            }
        }, 1000);

        function updateUI() {
            scoreEl.innerText = score;
        }

        function createFlyText(x, y, text) {
            const el = document.createElement('div');
            el.innerText = text;
            el.style.position = 'fixed';
            el.style.left = `${x}px`;
            el.style.top = `${y}px`;
            el.style.color = '#38bdf8';
            el.style.fontWeight = 'bold';
            el.style.fontSize = '18px';
            el.style.pointerEvents = 'none';
            el.style.transition = 'all 0.5s ease-out';
            document.body.appendChild(el);

            setTimeout(() => {
                el.style.transform = 'translateY(-40px)';
                el.style.opacity = '0';
            }, 10);
            setTimeout(() => el.remove(), 500);
        }
    </script>
</body>
</html>

