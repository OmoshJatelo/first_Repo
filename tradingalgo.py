import numericPython as np
import pandas as pd
import yfinance as yf
import backtrader as bt
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from datetime import datetime

# Function to Download Forex Data
def get_data(ticker, start="2023-01-01", end="2024-01-01"):
    data = yf.download(ticker, start=start, end=end)

    if data.empty:
        raise ValueError("Downloaded data is empty. Check ticker or date range.")
    
    # Ensure the index is a datetime index
    data.index = pd.to_datetime(data.index)
    
    # Compute Moving Averages for Trend Detection
    data["SMA_50"] = data["Close"].rolling(window=50).mean()
    data["SMA_200"] = data["Close"].rolling(window=200).mean()
    data["Trend"] = np.where(data["SMA_50"] > data["SMA_200"], 1, -1)
    
    # Drop NaN values after adding indicators
    data.dropna(inplace=True)
    
    return data

#  Train Machine Learning Model
def train_ml_model(data):
    X = data[["SMA_50", "SMA_200", "Trend"]]
    y = np.where(data["Close"].shift(-1) > data["Close"], 1, 0)  # Buy = 1, Sell = 0

    # Train-test split to evaluate model performance
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train.ravel())  # Fix: Flatten 'y' to 1D

    # Evaluate model on test data
    accuracy = model.score(X_test_scaled, y_test) * 100
    print(f"ML Model Test Accuracy: {accuracy:.2f}%")

    return model, scaler

#  Backtrader Strategy
class MLStrategy(bt.Strategy):
    params = (
        ("model", None),  # Add model as a parameter
        ("scaler", None),  # Add scaler as a parameter
    )

    def _init_(self):
        # Initialize model and scaler from params
        self.model = self.p.model
        self.scaler = self.p.scaler
        self.trade_results = []  # Track trade results

    def next(self):
        if self.model is None or self.scaler is None:
            return

        # Get the latest data for prediction
        features = np.array([[self.datas[0].SMA_50[0], self.datas[0].SMA_200[0], self.datas[0].Trend[0]]])
        scaled_features = self.scaler.transform(features)
        prediction = self.model.predict(scaled_features)

        # Trading logic
        if prediction == 1 and not self.position:
            self.buy()
        elif prediction == 0 and self.position:
            self.sell()

    def notify_trade(self, trade):
        # Log trade results
        if trade.isclosed:
            self.trade_results.append(trade.pnl)

#  Backtesting Function (Error-Free)
def backtest(data, model, scaler):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(MLStrategy, model=model, scaler=scaler)  # Pass model and scaler to the strategy

    # Set initial cash and commission
    cerebro.broker.set_cash(10000)  # $10,000 initial cash
    cerebro.broker.setcommission(commission=0.001)  # 0.1% commission

    # Debug: Print column names and check DataFrame structure
    print("DataFrame Columns:", data.columns)
    print("DataFrame Index:", data.index)
    print("DataFrame Head:\n", data.head())

    # Ensure the index is a datetime index
    if not isinstance(data.index, pd.DatetimeIndex):
        raise ValueError("DataFrame index must be a DatetimeIndex.")

    # Flatten MultiIndex columns (if present)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = ['_'.join(col).strip() for col in data.columns.values]

    # Convert DataFrame to Backtrader Feed
    data_feed = bt.feeds.PandasData(
        dataname=data,
        datetime=None,  # Use the index as datetime
        open="Open_EURUSD=X",  # Use flattened column names
        high="High_EURUSD=X",
        low="Low_EURUSD=X",
        close="Close_EURUSD=X",
        volume="Volume_EURUSD=X",
        openinterest=None,
    )
    cerebro.adddata(data_feed)

    # Add analyzers
    cerebro.addanalyzer(bt.analyzers.Returns, _name="returns")
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="sharpe")
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name="drawdown")

    # Run backtest
    results = cerebro.run()
    strategy = results[0]

    # Print trade results
    trade_results = strategy.trade_results
    win_rate = len([x for x in trade_results if x > 0]) / len(trade_results) * 100
    print(f"Win Rate: {win_rate:.2f}%")

    # Print performance metrics
    print(f"Total Return: {strategy.analyzers.returns.get_analysis()['rtot']:.2f}%")
    print(f"Sharpe Ratio: {strategy.analyzers.sharpe.get_analysis()['sharperatio']:.2f}")
    print(f"Max Drawdown: {strategy.analyzers.drawdown.get_analysis()['max']['drawdown']:.2f}%")

    # Plot results
    cerebro.plot()

#  Execute the Trading Bot
ticker = "GBPUSD=X"  # Use Yahoo Finance format for Forex
data = get_data(ticker)

# Debug: Check the structure of the data
print("Data Type:", type(data))  # Should output <class 'pandas.core.frame.DataFrame'>
print("Data Head:\n", data.head())  # Check the first few rows

model, scaler = train_ml_model(data)
backtest(data, model, scaler)