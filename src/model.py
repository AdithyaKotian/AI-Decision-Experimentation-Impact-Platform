import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# load data
data = pd.read_csv("data/base_data.csv")

X = data[[
    "amount",
    "account_age_days",
    "velocity_1h",
    "location_mismatch"
]]

y = data["is_fraud"]

# train-test split (simulating historical vs future)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# simple pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)

# generate risk scores (NOT predictions)
risk_scores = pipeline.predict_proba(X_test)[:, 1]

scored_data = X_test.copy()
scored_data["risk_score"] = risk_scores
scored_data["is_fraud"] = y_test.values

scored_data.to_csv("data/scored_data.csv", index=False)

print("Scored data created:", scored_data.shape)
