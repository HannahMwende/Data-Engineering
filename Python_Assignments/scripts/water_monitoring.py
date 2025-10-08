#Import libraries
import pandas as pd


# Loads data from a CSV file into a pandas DataFrame
def load_csv(file_path):
    df = pd.read_csv(file_path)
    print("Data loading completed successfully.")
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
    print("Data cleaning completed successfully.")
    return df




# A class that evaluates pH and turbidity ranges
class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0, dissolved_oxygen_threshold=5.0, temperature_range=(10.0, 30.0)):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold
        self.dissolved_oxygen_threshold = dissolved_oxygen_threshold
        self.temperature_range = temperature_range
    #Checks if water quality is safe
    def is_safe(self, row: pd.Series) -> tuple:
        reasons = []
        if not (self.ph_range[0] <= row['pH'] <= self.ph_range[1]):
            reasons.append(f"pH out of range ({self.ph_range[0]}–{self.ph_range[1]})")
        if row['turbidity'] > self.turbidity_threshold:
            reasons.append(f"turbidity too high (>{self.turbidity_threshold})")
        if row['dissolved_oxygen'] < self.dissolved_oxygen_threshold:
            reasons.append(f"dissolved oxygen too low (<{self.dissolved_oxygen_threshold})")
        if not (self.temperature_range[0] <= row['temperature'] <= self.temperature_range[1]):
            reasons.append(f"temperature out of range ({self.temperature_range[0]}–{self.temperature_range[1]})")

        if reasons:
            return False, ", ".join(reasons)
        else:
            return True, "Safe"
#Evauates water quality and prints results
def evaluate_water_quality(df):
    evaluator = WaterQualityEvaluator()
    for idx, row in df.iterrows():
        is_safe, reason = evaluator.is_safe(row)
        print(f"Sensor {row['sensor_id']} on {row['date']} at {row['time']}: {'Safe' if is_safe else 'Unsafe'} – {reason}")

#Recall functions to load, preprocess, and evaluate data
df = load_csv('sensor_data.csv')
df = preprocess_data(df)
evaluate_water_quality(df)

# Save cleaned data
df.to_csv('../data/results.csv', index=False)
print("Cleaned data saved as 'results.csv'.")