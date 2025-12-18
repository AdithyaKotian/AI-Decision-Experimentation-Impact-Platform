import numpy as np
import pandas as pd

np.random.seed(42)

N = 5000

data = pd.DataFrame({
    "amount": np.random.randint(100, 50000, N),
    "account_age_days": np.random.randint(1, 2000, N),
    "velocity_1h": np.random.randint(1, 15, N),
    "location_mismatch": np.random.choice([0, 1], size=N, p=[0.85, 0.15])
})

# hidden fraud logic (realistic but imperfect)
risk_score = (
    (data["amount"] > 20000).astype(int) +
    (data["velocity_1h"] > 5).astype(int) +
    (data["location_mismatch"] == 1).astype(int) +
    (data["account_age_days"] < 30).astype(int)
)

data["is_fraud"] = (risk_score >= 2).astype(int)

data.to_csv("data/base_data.csv", index=False)

print("Base transaction data generated:", data.shape)
