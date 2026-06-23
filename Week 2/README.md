# Week 2 — Mathematical Foundations for RL

## Goal
Understand why RL is fundamentally a problem of learning from **stochastic rewards**.

## Topics
- Probability: random variables, distributions, expectation, variance
- Linear algebra essentials (vectors, matrices, eigenvalues)
- Markov processes and the Markov property
- Optimization basics (gradient descent intuition)

## Resources

### 📺 YouTube
| Video | Link |
|---|---|
| Essence of Linear Algebra — 3Blue1Brown (Ch 1–7) | https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab |
| Probability & Statistics — Khan Academy | https://www.youtube.com/playlist?list=PL1328115D3D8A2566 |
| Mathematical Foundations of RL — Shiyu Zhao (Lectures 1–3) | https://www.youtube.com/playlist?list=PLEhdbSEZZbDaFWPX4gehhwB9vJZJ1DNm8 |

### 📖 Reading
| Resource | Link |
|---|---|
| Mathematical Foundations of RL — free textbook (Shiyu Zhao), Ch 1–3 | https://github.com/MathFoundationRL/Book-Mathematical-Foundation-of-Reinforcement-Learning |
| Deep Learning Book — Linear Algebra chapter (Goodfellow) | https://www.deeplearningbook.org/contents/linear_algebra.html |
| RL explained with minimum math — Understanding AI | https://www.understandingai.org/p/reinforcement-learning-explained |

### 🗒️ Slides
- Shiyu Zhao lecture slides (downloadable from the GitHub repo above)

## Notebooks in this folder
| File | Description |
|---|---|
| `01_probability_basics.ipynb` | Random variables, expectation, variance — dice & coin simulations |
| `02_markov_chains.ipynb` | Markov property, transition matrices, stationary distribution |
| `03_multi_armed_bandit.ipynb` | Greedy vs ε-greedy vs UCB on a k-armed bandit |
| `04_random_walk.ipynb` | 1D and 2D random walks, distribution over time |

## Daily Schedule (1.5–2 hrs)
- **30 min** — Watch one lecture segment or read one chapter section
- **60 min** — Work through the corresponding notebook
- **15–30 min** — Experiment: change parameters and re-plot

## Week 2 Checklist
- [ ] Understand what a random variable, expectation, and variance are
- [ ] Know what the Markov property means and why it matters for RL
- [ ] Build the multi-armed bandit simulation
- [ ] Simulate a Markov chain and verify the stationary distribution
