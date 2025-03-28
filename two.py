import numpy as np
import pandas as pd
from collections import Counter
import math

# Sample dataset
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]

df = pd.DataFrame(data, columns=["Outlook", "Temp", "Humidity", "Wind", "Tennis"])

# Function to calculate entropy
def entropy(target_column):
    counts = Counter(target_column)
    total = len(target_column)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

# Function to calculate Information Gain
def information_gain(df, attribute, target="Tennis"):
    total_entropy = entropy(df[target])
    values = df[attribute].unique()
    weighted_entropy = sum((len(df[df[attribute] == value]) / len(df)) * entropy(df[df[attribute] == value][target])
                           for value in values)
    return total_entropy - weighted_entropy

# Calculate Information Gain for each attribute
attributes = ["Outlook", "Temp", "Humidity", "Wind"]
for attr in attributes:
    print(f"Information Gain for {attr}: {information_gain(df, attr):.4f}")
