import pandas as pd
from src.data_preprocessing import load_and_clean_data
from src.model import train_model, predict_future
from src.visualization import plot_temperature

# Load and clean data
df = load_and_clean_data("data/weatherHistory.csv")


model = train_model(df)
# Train model

# Predict next 7 days
future_days, predictions = predict_future(model, df, days=7)

#Create dataframe for predictions
future_dates = pd.date_range(start=df['Date'].max() + pd.Timedelta(days=1), periods=len(future_days))
pred_df = pd.DataFrame({
    "Date": future_dates,
    "Temp": predictions
})

#   Merge historical + predicted
final_df = pd.concat([df, pred_df], ignore_index=True)

#  Save to CSV
final_df.to_csv("data/predicted_weather.csv", index=False)

#Visualize
plot_temperature(df, future_days, predictions)

print("Predictions saved to data/predicted_weather.csv")
