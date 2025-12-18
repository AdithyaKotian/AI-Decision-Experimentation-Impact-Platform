import pandas as pd

# Load policy decisions
data = pd.read_csv("data/policy_decisions.csv")

POLICIES = ["policy_A", "policy_B", "policy_C"]

results = []

for policy in POLICIES:
    decisions = data[policy]

    approval_rate = (decisions == "APPROVE").mean()
    review_rate = (decisions == "REVIEW").mean()

    fraud_caught = (
        (data["is_fraud"] == 1) & (decisions == "BLOCK")
    ).sum()

    fraud_missed = (
        (data["is_fraud"] == 1) & (decisions == "APPROVE")
    ).sum()

    results.append({
        "policy": policy,
        "approval_rate": round(approval_rate, 3),
        "review_rate": round(review_rate, 3),
        "fraud_caught": fraud_caught,
        "fraud_missed": fraud_missed
    })

results_df = pd.DataFrame(results)
results_df.to_csv("data/experiment_results.csv", index=False)

print(results_df)
