import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model(df):
    # Ensure Date is datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', utc=True)
    
    df['day_num'] = (df['Date'] - df['Date'].min()).dt.days# Convert Date to numeric day number
   # Drop rows with missing values
    df = df.
    dropna(subset=['day_num', 'Temp'])

    X = df[['day_num']]
    y = df['Temp']

    model = LinearRegression()
    model.fit(X, y)
    return model


def predict_future(model, df, days=7):
    # Get last day number
    df['day_num'] = (df['Date'] - df['Date'].min()).dt.days
    last_day = df['day_num'].max()

    # Create future days
    future_days = list(range(last_day + 1, last_day + days + 1))
    future_X = pd.DataFrame(future_days, columns=['day_num'])

    # Predict temperatures
    predictions = model.predict(future_X)

    return future_days, predictions
