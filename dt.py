import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Define dataset
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
df_encoded = df.apply(LabelEncoder().fit_transform)

# Split input and output
X = df_encoded.drop(columns=["Tennis"])
y = df_encoded["Tennis"]

# Train dt model
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=X.columns, class_names=["No", "Yes"], filled=True)
plt.savefig("decision_tree.png")
print("Decision tree saved as 'decision_tree.png'")
