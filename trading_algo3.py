import numpy as np
import pandas as pd
import yfinance as yf
import backtrader as bt
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from datetime import datetime

# ✅ Download Forex Data for Multiple Pairs
def get_data(tickers, start="2023-01-01", end="2024-01-01"):
    data_dict = {}
    for ticker in tickers:
        data = yf.download(ticker, start=start, end=end)
        if data.empty:
            print(f"Warning: No data found for {ticker}. Skipping.")
            continue

        # Compute Moving Averages for Trend Detection
        data["SMA_50"] = data["Close"].rolling(window=50).mean()
        data["SMA_200"] = data["Close"].rolling(window=200).mean()
        data["Trend"] = np.where(data["SMA_50"] > data["SMA_200"], 1, -1)

        # Compute ATR for Dynamic Position Sizing
        data["ATR"] = data["High"] - data["Low"]
        data["ATR"] = data["ATR"].rolling(window=14).mean()

        # Drop NaN values after adding indicators
        data.dropna(inplace=True)

        data_dict[ticker] = data

    return data_dict

# ✅ Train Machine Learning Model
def train_ml_model(data):
    X = data[["SMA_50", "SMA_200", "Trend"]]
    y = np.where(data["Close"].shift(-1) > data["Close"], 1, 0)  # Buy = 1, Sell = 0

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_scaled, y.ravel())

    accuracy = model.score(X_scaled, y) * 100
    print(f"ML Model Accuracy: {accuracy:.2f}%")

    return model, scaler

# ✅ Dynamic Position Sizing Based on ATR
def calculate_dynamic_position_size(account_balance, atr_value, risk_percentage=0.01):
    risk_amount = account_balance * risk_percentage
    if atr_value > 0:
        position_size = risk_amount / atr_value
        return position_size
    return 0  # Avoid division by zero

# ✅ Backtrader Strategy with Performance Metrics
class MLStrategy(bt.Strategy):
    params = (("model", None), ("scaler", None), ("account_balance", 70), ("stop_loss_pct", 0.02),
              ("risk_reward_ratio", 3), ("risk_percentage", 0.01))

    def _init_(self):
        self.model = self.params.model
        self.scaler = self.params.scaler
        self.account_balance = self.params.account_balance
        self.stop_loss_pct = self.params.stop_loss_pct
        self.risk_reward_ratio = self.params.risk_reward_ratio
        self.risk_percentage = self.params.risk_percentage

        # Trade Statistics
        self.total_trades = 0
        self.wins = 0
        self.losses = 0

    def next(self):
        if self.model is None or self.scaler is None:
            return

        for i, data in enumerate(self.datas):
            features = np.array([[data.SMA_50[0], data.SMA_200[0], data.Trend[0]]])
            scaled_features = self.scaler.transform(features)
            prediction = self.model.predict(scaled_features)

            # Ensure ATR Calculation is Updated
            atr_value = data.ATR[0] if hasattr(data, 'ATR') else 0
            position_size = calculate_dynamic_position_size(self.account_balance, atr_value, self.risk_percentage)

            if prediction == 1 and not self.position:  # Buy Signal
                self.total_trades += 1
                stop_loss = data.close[0] * (1 - self.stop_loss_pct)
                take_profit = data.close[0] * (1 + self.risk_reward_ratio * self.stop_loss_pct)
                self.buy(price=data.close[0], exectype=bt.Order.Market, stopprice=stop_loss, limitprice=take_profit, size=position_size)

            elif prediction == 0 and self.position:  # Sell Signal
                self.close()  # Close the existing position

    def notify_trade(self, trade):
        if trade.isclosed:
            if trade.pnl > 0:
                self.wins += 1
            else:
                self.losses += 1

    def stop(self):
        win_rate = (self.wins / self.total_trades) * 100 if self.total_trades > 0 else 0
        print("\n==== Trading Performance ====")
        print(f"Total Trades: {self.total_trades}")
        print(f"Trades Won: {self.wins}")
        print(f"Trades Lost: {self.losses}")
        print(f"Win Rate: {win_rate:.2f}%")
        print("=============================\n")

# ✅ Backtesting Function
def backtest(data_dict, model, scaler):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(MLStrategy, model=model, scaler=scaler, account_balance=70, stop_loss_pct=0.02, risk_reward_ratio=3, risk_percentage=0.01)

    # Convert Data to Backtrader Format
    for ticker, data in data_dict.items():
        if isinstance(data, pd.DataFrame):
            data_feed = bt.feeds.PandasData(dataname=data)
            cerebro.adddata(data_feed, name=ticker)
        else:
            print(f"Skipping {ticker}: Invalid data format (not a DataFrame)")

    cerebro.run()
    cerebro.plot()

# ✅ Execute the Trading Bot
tickers = ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X", "USDCHF=X",
           "USDCAD=X", "NZDUSD=X", "EURGBP=X", "EURJPY=X", "GBPJPY=X"]

data_dict = get_data(tickers)
model, scaler = train_ml_model(data_dict["EURUSD=X"])  # Train using EUR/USD as an example
backtest(data_dict, model, scaler)