# Week 4 — Dynamic Programming

## Goal
Compute optimal policies when the **full model** (transition probabilities + rewards) is known.

## Topics
- Bellman Expectation Equation
- Policy Evaluation (iterative)
- Policy Improvement Theorem
- Policy Iteration
- Value Iteration
- Visualising value functions and policies

## Resources

### 📺 YouTube
| Video | Link |
|---|---|
| David Silver — Lecture 3: Planning by Dynamic Programming | https://www.youtube.com/watch?v=Nd1-UUMVfz4 |
| Bellman Equations, DP & Generalized Policy Iteration — Mutual Information | https://www.youtube.com/c/MutualInformation |

### 📖 Reading
| Resource | Link |
|---|---|
| Sutton & Barto — Chapter 4: Dynamic Programming | http://incompleteideas.net/book/the-book-2nd.html |
| Bellman Equations & DP visual walkthrough — int8.io | https://int8.io/bellman-equations-reinforcement-learning/ |
| Understanding the Bellman Equation — DataCamp | https://www.datacamp.com/tutorial/bellman-equation-reinforcement-learning |

### 🗒️ Slides
- David Silver Lecture 3 slides: https://github.com/zyxue/youtube_RL_course_by_David_Silver

## Notebooks in this folder
| File | Description |
|---|---|
| `01_policy_evaluation.ipynb` | Iterative policy evaluation — compute V^π for any policy |
| `02_policy_iteration.ipynb` | Policy iteration — full loop to find the optimal policy |
| `03_value_iteration.ipynb` | Value iteration — single loop, faster convergence |
| `04_frozen_lake_dp.ipynb` | Solve FrozenLake with DP using the env.P transition model |

## Daily Schedule (1.5–2 hrs)
- **30 min** — Watch David Silver Lecture 3 (or sections of it)
- **60 min** — Work through notebooks in order
- **15–30 min** — Extend the Grid World (add obstacles, change rewards)

## Week 4 Checklist
- [ ] Implement policy evaluation and verify convergence
- [ ] Implement policy iteration — watch the policy arrows change each iteration
- [ ] Implement value iteration — compare sweep count vs policy iteration
- [ ] Solve FrozenLake (non-slippery) with value iteration and achieve 100% win rate
- [ ] Visualise value functions as heatmaps
