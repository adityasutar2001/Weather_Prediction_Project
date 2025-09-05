import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    # Convert to datetime safely
    df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], errors='coerce')

    # Rename to simple names
    df.rename(columns={
        'Formatted Date': 'Date',
        'Temperature (C)': 'Temp'
    }, inplace=True)

    # Keep only needed columns
    df = df[['Date', 'Temp']]

    # Drop rows where Date or Temp is missing
    df = df.dropna(subset=['Date', 'Temp']).sort_values('Date')

    return df
