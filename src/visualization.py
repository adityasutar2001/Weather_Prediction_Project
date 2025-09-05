import matplotlib.pyplot as plt
import pandas as pd

def plot_temperature(df, future_days=None, predictions=None):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Temp'], label='Historical Temperature', marker='o')

    if future_days is not None and predictions is not None:
        future_dates = pd.date_range(start=df['Date'].max()+pd.Timedelta(days=1), periods=len(future_days))
        plt.plot(future_dates, predictions, label='Predicted Temperature', linestyle='dashed', marker='x')

    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Weather Data Analysis and Prediction")
    plt.legend()
    plt.show()
