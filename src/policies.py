import pandas as pd

# Load scored data
data = pd.read_csv("data/scored_data.csv")


def policy_aggressive(risk):
    if risk < 0.7:
        return "APPROVE"
    else:
        return "BLOCK"


def policy_balanced(risk):
    if risk < 0.5:
        return "APPROVE"
    elif risk < 0.75:
        return "REVIEW"
    else:
        return "BLOCK"


def policy_conservative(risk):
    if risk < 0.4:
        return "APPROVE"
    elif risk < 0.6:
        return "REVIEW"
    else:
        return "BLOCK"


# Apply policies
data["policy_A"] = data["risk_score"].apply(policy_aggressive)
data["policy_B"] = data["risk_score"].apply(policy_balanced)
data["policy_C"] = data["risk_score"].apply(policy_conservative)

# Save decisions
data.to_csv("data/policy_decisions.csv", index=False)

print("Policy decisions generated:", data.shape)
