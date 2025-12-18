# AI Decision Experimentation & Impact Platform

## Product Problem
In real-world products, AI models do not make final decisions. They generate signals that product teams convert into actions such as approve, review, or block. The core challenge is not model accuracy, but selecting the decision strategy that best balances user experience, risk, operational effort, and business cost.

This project addresses a practical product question:
Which AI-driven decision policy should a product deploy to maximize business impact?

---

## Why a Single ML Model Is Not Enough
An ML model outputs a risk score, not a decision. Different product strategies can use the same score in different ways:
- Aggressive strategies favor growth but accept higher risk
- Conservative strategies reduce risk but increase user friction and operational cost
- Balanced strategies aim to optimize trade-offs

Choosing between these strategies is a product decision. This platform is designed to experiment with multiple policies and recommend the most effective one.

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



The ML model acts strictly as a signal generator. All business logic and trade-offs are handled at the policy layer.

---

## Data and ML Signal
Each transaction contains:
- Transaction amount
- Account age (days)
- Transaction velocity
- Location mismatch indicator

A simple ML model generates a continuous risk_score between 0 and 1. The model is intentionally imperfect and not optimized for accuracy, reflecting how ML signals are used in production systems.

---

## Decision Policies
Three decision policies were implemented using the same ML risk score:

**Policy A – Aggressive Growth**
- Maximizes approvals
- Minimizes user friction
- Accepts higher fraud risk

**Policy B – Balanced Strategy**
- Balanced approvals, reviews, and blocks
- Typical of mature production systems

**Policy C – Conservative Safety**
- Minimizes fraud risk
- Higher friction and operational cost

Each policy represents a different product strategy, not a different ML model.

---

## Experiment Design
All policies are evaluated on the same transaction dataset using offline experimentation. For each policy, the following KPIs are measured:
- Approval rate (user experience)
- Review rate (operational friction)
- Fraud caught
- Fraud missed

This simulates real-world A/B testing before deploying a policy to production.

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
- The aggressive policy led to high fraud losses
- The conservative policy reduced fraud but increased friction and operational cost
- The balanced policy achieved the lowest overall business cost

**Recommended Policy: Policy B (Balanced)**

This policy provides the best trade-off between fraud prevention, user experience, and operational efficiency.

---

## Key Takeaways
- ML models should be treated as signals, not decision-makers
- Product impact depends on decision strategy, not just model accuracy
- Offline experimentation is critical before deployment
- The optimal policy minimizes business loss, not prediction error

---

## Limitations and Future Work
- Cost assumptions can be tuned for different businesses
- Experiments are offline and can be extended to live A/B testing
- Additional policies can be easily added
- Can be extended with drift monitoring and human feedback loops

---

## Why This Project 
It demonstrates product-oriented ML thinking by combining experimentation, KPI analysis, and cost-aware decision-making. The platform reflects how AI-driven decisions are designed and evaluated in real production systems.
