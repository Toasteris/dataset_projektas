import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned Madrid pollution dataset
madrid_file = "data/cleaned_MadridPolution2001-2022.csv"
madrid_data = pd.read_csv(madrid_file, parse_dates=['Time'])
madrid_data.set_index('Time', inplace=True)

# Time Series Analysis: CO Levels Over Time
madrid_data['CO'].plot(figsize=(12, 6), title='CO Levels Over Time')
plt.ylabel('Normalized CO Levels')
plt.savefig('outputs/co_trend_over_time.png')
plt.show()

# Daily Average CO Levels
daily_avg = madrid_data.resample('D').mean()
daily_avg['CO'].plot(figsize=(12, 6), title='Daily Average CO Levels')
plt.ylabel('Normalized CO Levels')
plt.savefig('outputs/daily_avg_co.png')
plt.show()

# Correlation Matrix Between Pollutants
pollutant_columns = ['BEN', 'CH4', 'CO', 'EBE', 'NMHC', 'NO', 'NO2', 'NOx', 'O3', 'PM10', 'PM25', 'SO2', 'TCH', 'TOL']
corr = madrid_data[pollutant_columns].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title('Correlation Between Pollutants')
plt.savefig('outputs/pollutant_correlation_matrix.png')
plt.show()