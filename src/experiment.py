import pandas as pd

def run_experiment():
    # Load scored data
    data = pd.read_csv("data/scored_data.csv")

    policies = {
        "policy_A": {"approve": 0.7, "review": 0.2},
        "policy_B": {"approve": 0.5, "review": 0.3},
        "policy_C": {"approve": 0.3, "review": 0.4},
    }

    results = []

    for policy, thresholds in policies.items():
        decisions = []

        for score in data["risk_score"]:
            if score < thresholds["approve"]:
                decisions.append("APPROVE")
            elif score < thresholds["approve"] + thresholds["review"]:
                decisions.append("REVIEW")
            else:
                decisions.append("BLOCK")

        decisions = pd.Series(decisions)

        approval_rate = (decisions == "APPROVE").mean()
        review_rate = (decisions == "REVIEW").mean()

        fraud_caught = ((data["is_fraud"] == 1) & (decisions == "BLOCK")).sum()
        fraud_missed = ((data["is_fraud"] == 1) & (decisions == "APPROVE")).sum()

        results.append({
            "policy": policy,
            "approval_rate": round(approval_rate, 3),
            "review_rate": round(review_rate, 3),
            "fraud_caught": fraud_caught,
            "fraud_missed": fraud_missed
        })

    results_df = pd.DataFrame(results)
    results_df.to_csv("data/experiment_results.csv", index=False)

    # ✅ SAFE recommendation logic
    best_policy = (
        results_df
        .sort_values(by=["fraud_missed", "review_rate"], ascending=[True, True])
        .iloc[0]["policy"]
    )

    return {
        "summary_table": results_df,
        "recommended_policy": best_policy
    }
