import pandas as pd

# Load data
decisions = pd.read_csv("data/policy_decisions.csv")
results = pd.read_csv("data/experiment_results.csv")

# Cost assumptions (INR)
COST_FRAUD_MISSED = 5000
COST_LEGIT_BLOCKED = 1000
COST_REVIEW = 200

impact = []

for _, row in results.iterrows():
    policy = row["policy"]

    policy_decisions = decisions[policy]

    fraud_missed = (
        (decisions["is_fraud"] == 1) &
        (policy_decisions == "APPROVE")
    ).sum()

    legit_blocked = (
        (decisions["is_fraud"] == 0) &
        (policy_decisions == "BLOCK")
    ).sum()

    reviews = (policy_decisions == "REVIEW").sum()

    total_cost = (
        fraud_missed * COST_FRAUD_MISSED +
        legit_blocked * COST_LEGIT_BLOCKED +
        reviews * COST_REVIEW
    )

    impact.append({
        "policy": policy,
        "fraud_missed": fraud_missed,
        "legit_blocked": legit_blocked,
        "reviews": reviews,
        "total_cost_inr": total_cost
    })

impact_df = pd.DataFrame(impact)
impact_df.to_csv("data/policy_impact.csv", index=False)

print(impact_df)
