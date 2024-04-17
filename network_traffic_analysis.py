import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('network_traffic_anomaly_dataset.csv')

print(df.head())

print(df.describe())

print(df.isnull().sum())

print(df['Label'].value_counts())

print(df['Anomaly Type'].value_counts())

plt.figure(figsize=(10, 6))
sns.histplot(df['Packet Length'], bins=30, kde=True)
plt.xlabel('Packet Length')
plt.ylabel('Frequency')
plt.title('Distribution of Packet Length')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Anomaly Type')
plt.xlabel('Anomaly Type')
plt.ylabel('Count')
plt.title('Distribution of Anomaly Types')
plt.xticks(rotation=45)
plt.show()


from sklearn.ensemble import IsolationForest

X = df[['Source Port', 'Destination Port', 'Packet Length']]

model = IsolationForest(contamination=0.1, random_state=42)

model.fit(X)

df['Anomaly'] = model.predict(X)

potential_anomalies = df[df['Anomaly'] == -1]

for idx, row in potential_anomalies.iterrows():
    print(f"Alert: Suspicious activity detected - {row['Anomaly Type']} at {row['Timestamp']}.")

