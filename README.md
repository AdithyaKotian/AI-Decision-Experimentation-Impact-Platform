Live demo:
https://ai-decision-experimentation-impact-platform-fgubk3wtu9qfh9zpu7.streamlit.app

# AI Decision Experimentation & Impact Platform

## Product Problem
In real world products,AI models do not make a final decisions.They generate signals that a product teams translate into actions such as approve,review or block.The real challenge is not to achieving higher model accuracy,but choosing a decision strategy that balances user experience,risk,operational effort and overall business cost.

This project explores a practical product question:
Which AI driven decision policy should a product deploy to minimize the business loss?

---

## Why a Single ML Model Is Not Enough
An ML model produces a risk score,not a decision.The same score can lead to very a different outcomes depending on how it is used:
- Aggressive strategies prioritize growth but accept higher risk.
- Conservative strategies reduce the risk but increase friction and the operational cost.
- Balanced strategies aim to optimize trade offs.
  
Selecting among these strategies is a product decision,not a modeling decision.
This platform evaluates a multiple decision policies and recommends the most effective one based on business impact.

---

## System Architecture

Transaction Data

↓

ML Risk Scoring Model

↓

Decision Policies (Aggressive / Balanced / Conservative)

↓

Offline Experiment Engine

↓

KPI & Cost Impact Analysis

↓

Policy Recommendation



The ML model acts strictly as a signal generator. All business logic and trade offs are handled at the policy layer.

---

## Data and ML Signal
Each transaction contains:
- Transaction amount
- Account age (days)
- Transaction velocity
- Location mismatch indicator

A simple ML model generates a continuous risk_score between 0 and 1.The model is intentionally imperfect and not a optimized for accuracy, reflecting how ML signals are used in production systems.

---

## Decision Policies
Three decision policies were implemented using the same ML risk score:

**Policy A – Aggressive Growth**
- Maximizes approvals
- Minimizes user friction
- Accepts higher fraud risk

**Policy B – Balanced Strategy**
- Balanced approvals, reviews and blocks
- Typical of mature production systems

**Policy C – Conservative Safety**
- Minimizes fraud risk
- Higher friction and operational cost

Each policy represents a different product strategy,not a different ML model.

---

## Experiment Design
All policies are evaluated on the same transaction dataset using offline experimentation.For each policy,the following KPIs are measured:
- Approval rate (user experience)
- Review rate (operational friction)
- Fraud caught
- Fraud missed

This mirrors how the decision strategies are evaluated before production deployment.
---

## Business Impact and Cost Modeling
Decisions are translated into business cost using realistic assumptions:
- Fraud missed: ₹5,000 loss
- Legit transaction blocked: ₹1,000 loss
- Manual review: ₹200 cost

Total business impact is calculated as:
Total Cost = Fraud Loss + Block Loss + Review Cost

This allows policies to be compared using business outcomes rather than ML metrics.

---

## Final Recommendation
After evaluating all policies:
- The aggressive policy led to high fraud losses.
- The balanced policy reduced losses but still missed significant fraud.
- The conservative policy minimized fraud misses at the cost of higher friction.
  
**Recommended Policy: Policy C (Conservative Safety)**

This policy minimizes the overall business loss by prioritizing fraud prevention,even at the expense of user friction and operational cost.
---

## Key Takeaways
- ML models should be treated as signals,not decision makers.
- Product impact depends on decision strategy,not just model accuracy.
- Offline experimentation is critical before deployment.
- The optimal policy minimizes business loss,not prediction error.

---

## Limitations and Future Work
- Cost assumptions can be tuned for different businesses.
- Experiments are offline and can be extended to live A/B testing.
- Additional policies can be easily added.
- Can be extended with drift monitoring and human feedback loops.

---

## Why This Project 
This project demonstrates product oriented ML thinking by combining decision experimentation,KPI analysis and cost aware evaluation.It reflects how AI driven decisions are designed,tested and validated in real production systems.
