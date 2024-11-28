import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned esophageal cancer dataset
esophageal_file = "data/cleaned_esophageal_data.csv"
esophageal_data = pd.read_csv(esophageal_file)

# Age Distribution
sns.histplot(esophageal_data['age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('outputs/age_distribution.png')
plt.show()

# Gender Distribution
sns.countplot(x='gender', data=esophageal_data)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.savefig('outputs/gender_distribution.png')
plt.show()

# Histology Type Counts
histology_counts = esophageal_data['primary_pathology_histological_type'].value_counts()
print("Cancer Histology Types and Their Counts:")
print(histology_counts)

sns.countplot(
    y='primary_pathology_histological_type',
    data=esophageal_data,
    order=histology_counts.index
)
plt.title('Cancer Histology Types')
plt.xlabel('Count')
plt.ylabel('Histology Type')
plt.savefig('outputs/histology_type_counts.png')
plt.show()

# Pathologic Stages
sns.countplot(
    y='stage_event_pathologic_stage',
    data=esophageal_data,
    order=esophageal_data['stage_event_pathologic_stage'].value_counts().index
)
plt.title('Pathologic Cancer Stages')
plt.xlabel('Count')
plt.ylabel('Stage')
plt.tight_layout()
plt.savefig('outputs/pathologic_cancer_stages.png')
plt.show()

# Survival by Age and Gender
sns.boxplot(x='vital_status', y='age', hue='gender', data=esophageal_data)
plt.title('Survival by Age and Gender')
plt.xlabel('Vital Status')
plt.ylabel('Age')
plt.savefig('outputs/survival_by_age_gender.png')
plt.show()