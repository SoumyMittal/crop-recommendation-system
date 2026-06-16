# utils/train_model.py

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("dataset.csv")

# Features
X = df.drop("label", axis=1)

# Target
y = df["label"]

# Encode Labels
encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy: {accuracy * 100:.2f}%")

# Save Model
joblib.dump(
    model,
    "crop_model.pkl"
)

joblib.dump(
    encoder,
    "label_encoder.pkl"
)

print("Model Saved Successfully")