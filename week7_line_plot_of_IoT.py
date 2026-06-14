import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned IoT data
df = pd.read_csv("cleaned_iot_data.csv")

# Display the first few rows to verify data
print(df.head())

# Convert timestamp column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(x=df["timestamp"], y=df["numeric_value"],
             hue=df["device_id"], marker="o")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.title("IoT Data Trends Over Time", fontsize=14)
plt.xlabel("Timestamp", fontsize=12)
plt.ylabel("Numeric Value", fontsize=12)

# Show legend
plt.legend(title="Device ID", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Display the plot
plt.show()

