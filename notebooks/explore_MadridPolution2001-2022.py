import pandas as pd
from sklearn.preprocessing import MinMaxScaler

madrid_file = "data/MadridPolution2001-2022.csv"
madrid_data = pd.read_csv(madrid_file)

print(madrid_data.info())
print(madrid_data.head())

if 'Time' in madrid_data.columns:
    madrid_data['Time'] = pd.to_datetime(madrid_data['Time'], errors='coerce')
    print(madrid_data['Time'].head())
else:
    print("The 'Time' column is missing from the dataset.")

print(madrid_data.isnull().sum())

pollutant_columns = ['BEN', 'CH4', 'CO', 'EBE', 'NMHC', 'NO', 'NO2', 'NOx', 'O3', 'PM10', 'PM25', 'SO2', 'TCH', 'TOL']
existing_pollutant_columns = [col for col in pollutant_columns if col in madrid_data.columns]

for col in existing_pollutant_columns:
    madrid_data[col] = madrid_data[col].fillna(madrid_data[col].mean())

if existing_pollutant_columns:
    scaler = MinMaxScaler()
    madrid_data[existing_pollutant_columns] = scaler.fit_transform(madrid_data[existing_pollutant_columns])

print(madrid_data.info())
print(madrid_data.head())

madrid_data.to_csv("data/cleaned_MadridPolution2001-2022.csv", index=False)