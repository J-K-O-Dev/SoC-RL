# Week 5 — Model-Free Learning

## Goal
Train an agent **without knowing** transition probabilities — learn purely from interaction.

## Topics
- Monte Carlo (MC) prediction and control
- Temporal Difference (TD) learning — TD(0)
- SARSA (on-policy TD control)
- Q-Learning (off-policy TD control)
- Exploration strategies: ε-greedy, GLIE
- On-policy vs off-policy distinction

## Resources

### 📺 YouTube
| Video | Link |
|---|---|
| David Silver — Lecture 4: Model-Free Prediction | https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ |
| David Silver — Lecture 5: Model-Free Control | https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ |

### 📖 Reading
| Resource | Link |
|---|---|
| Sutton & Barto — Chapter 5: Monte Carlo Methods | http://incompleteideas.net/book/the-book-2nd.html |
| Sutton & Barto — Chapter 6: Temporal Difference Learning | http://incompleteideas.net/book/the-book-2nd.html |
| Q-Learning & SARSA with Python — Towards Data Science | https://towardsdatascience.com/q-learning-and-sasar-with-python-3775f86bd178/ |
| SARSA Full Guide — DataCamp | https://www.datacamp.com/tutorial/sarsa-reinforcement-learning-algorithm-in-python |
| Original Q-Learning paper (Watkins & Dayan 1992) | https://link.springer.com/article/10.1007/BF00992698 |

### 🗒️ Slides
- David Silver Lectures 4 & 5 slides: https://github.com/zyxue/youtube_RL_course_by_David_Silver
- SARSA & Q-Learning — PSU CMPSC 448: https://www.cse.psu.edu/~mzm616/courses/cmpsc448/slides/22.%20Sarsa%20and%20Q-learning.pdf

## Notebooks in this folder
| File | Description |
|---|---|
| `01_monte_carlo.ipynb` | MC prediction and first-visit MC control on FrozenLake |
| `02_td_learning.ipynb` | TD(0) prediction — bootstrapping explained |
| `03_sarsa.ipynb` | SARSA on-policy control on Taxi-v3 |
| `04_q_learning.ipynb` | Q-Learning off-policy control + SARSA vs Q-Learning comparison |

## Daily Schedule (1.5–2 hrs)
- **30 min** — David Silver Lecture 4 or 5
- **60 min** — Work through notebooks in order
- **15–30 min** — Visualise Q-table and tweak hyperparameters

## Week 5 Checklist
- [ ] Implement first-visit MC control from scratch
- [ ] Understand the one-line difference between SARSA and Q-Learning update rules
- [ ] Implement both SARSA and Q-Learning on Taxi-v3
- [ ] Plot learning curves and compare them on the same axes
- [ ] Visualise the Q-table as a heatmap
