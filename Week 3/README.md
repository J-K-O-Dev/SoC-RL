# Week 3 — Reinforcement Learning Fundamentals

## Goal
Be able to formulate any sequential decision problem as a **Markov Decision Process (MDP)** and explain its key components.

## Topics
- Agent, Environment, State, Action, Reward framework
- Return and Discount Factor (γ)
- Episodic vs Continuous tasks
- Exploration vs Exploitation dilemma
- Markov Decision Processes (MDPs) formally
- Value functions V(s) and Q(s,a)

## Resources

### 📺 YouTube
| Video | Link |
|---|---|
| David Silver — Lecture 1: Intro to RL | https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ |
| David Silver — Lecture 2: Markov Decision Processes | https://www.youtube.com/watch?v=lfHX2hHRMVQ |
| Mathematical Foundations of RL — Lectures 4–6 (Shiyu Zhao) | https://www.youtube.com/playlist?list=PLEhdbSEZZbDaFWPX4gehhwB9vJZJ1DNm8 |

### 📖 Reading
| Resource | Link |
|---|---|
| Sutton & Barto — Chapters 1–3 (free PDF) | http://incompleteideas.net/book/the-book-2nd.html |
| OpenAI Spinning Up — Key Concepts in RL | https://spinningup.openai.com/en/latest/spinningup/rl_intro.html |

### 🗒️ Slides
- David Silver Lectures 1 & 2 slides: https://github.com/zyxue/youtube_RL_course_by_David_Silver

## Notebooks in this folder
| File | Description |
|---|---|
| `01_mdp_formulation.ipynb` | Formal MDP definition — states, actions, rewards, transitions |
| `02_grid_world_env.ipynb` | Build a custom 5×5 Grid World from scratch |
| `03_returns_and_discount.ipynb` | Return, discount factor γ, episodic vs continuing tasks |
| `04_frozen_lake_exploration.ipynb` | Gymnasium Frozen Lake — random and ε-greedy policies |

## Daily Schedule (1.5–2 hrs)
- **30 min** — Watch one David Silver lecture
- **60 min** — Work through the corresponding notebook
- **15–30 min** — Read the corresponding S&B chapter section

## Week 3 Checklist
- [ ] Write the 5-tuple (S, A, R, T, γ) for at least two real problems
- [ ] Implement a Grid World from scratch (no Gymnasium)
- [ ] Compute discounted return for a sample trajectory by hand then verify in code
- [ ] Run a random policy on FrozenLake-v1 and plot win rate
