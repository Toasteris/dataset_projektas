import pandas as pd

esophageal_file = "data/Esophageal_Dataset.csv"
esophageal_data = pd.read_csv(esophageal_file)

print(esophageal_data.info())
print(esophageal_data.head())

print(esophageal_data.isnull().sum())

if 'height' in esophageal_data.columns:
    esophageal_data['height'] = esophageal_data['height'].fillna(esophageal_data['height'].mean())

if 'gender' in esophageal_data.columns:
    esophageal_data['gender'] = esophageal_data['gender'].fillna("Unknown")

if 'days_to_birth' in esophageal_data.columns:
    esophageal_data['age'] = -esophageal_data['days_to_birth'] // 365
    
columns_to_drop = ['column_name']
existing_columns_to_drop = [col for col in columns_to_drop if col in esophageal_data.columns]
esophageal_data.drop(columns=existing_columns_to_drop, inplace=True)

esophageal_data.to_csv('data/cleaned_esophageal_data.csv', index=False)

print(esophageal_data.info())
print(esophageal_data.head())