import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ----------------------------------
# LOAD DATASET
# ----------------------------------

df = pd.read_csv("PCOS_data.csv")

print("Dataset Loaded Successfully ✅")

# ----------------------------------
# REMOVE UNWANTED COLUMNS
# ----------------------------------

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# ----------------------------------
# CLEAN DATA
# ----------------------------------

# Remove extra dots like 1.99.
df = df.replace(r"\.$", "", regex=True)

# Convert columns to numeric
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove missing values
df = df.dropna()

print("Dataset Cleaned Successfully ✅")

# ----------------------------------
# TARGET VARIABLE
# ----------------------------------

y = df["PCOS (Y/N)"]

# ----------------------------------
# FEATURES
# ----------------------------------

X = df.drop("PCOS (Y/N)", axis=1)

# ----------------------------------
# TRAIN TEST SPLIT
# ----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------------
# RANDOM FOREST MODEL
# ----------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# ----------------------------------
# TRAIN MODEL
# ----------------------------------

model.fit(X_train, y_train)

print("Model Trained Successfully ✅")

# ----------------------------------
# PREDICTION
# ----------------------------------

y_pred = model.predict(X_test)

# ----------------------------------
# ACCURACY
# ----------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")

# ----------------------------------
# SAVE MODEL
# ----------------------------------

joblib.dump(model, "pcos_model.pkl")

print("Model Saved Successfully ✅")