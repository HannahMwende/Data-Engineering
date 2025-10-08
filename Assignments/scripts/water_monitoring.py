#Import libraries
import pandas as pd


# Loads data from a CSV file into a pandas DataFrame
def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df


# Cleans and preprocesses water quality data
def preprocess_data(df):
    """
    Cleans and preprocesses water quality data.
    - Cleans 'sensor_id'
    - Converts 'timestamp' to datetime and extracts 'date' and 'time'
    - Handles missing values
    """
    df['sensor_id'] = df['sensor_id'].str.replace('SENSOR_', '', regex=False).astype(int).astype(str)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['date'] = df['timestamp'].dt.date
    df['time'] = df['timestamp'].dt.time
    df = df.drop('timestamp', axis=1)
    df = df.dropna(subset=['pH', 'turbidity', 'dissolved_oxygen', 'temperature'])

    return df

load_csv('sensor_data.csv')
preprocess_data(df)