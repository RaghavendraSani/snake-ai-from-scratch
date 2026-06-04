# Snake AI From Scratch 🐍🤖

A reinforcement learning project where a Snake AI learns to play the game from scratch.

This project is being built step-by-step to understand every component of reinforcement learning instead of relying on high-level machine learning frameworks.

## Project Goals

- Build a Snake game environment using Python and Pygame
- Convert the game into an AI-compatible reinforcement learning environment
- Implement reinforcement learning concepts from scratch
- Train an AI agent to survive longer and collect food efficiently
- Understand every component of the learning process


---

## Current Progress

### Phase 1: Snake Game
- [x] Game window
- [x] Snake movement
- [x] Food spawning
- [x] Snake growth
- [x] Wall collision detection
- [x] Self-collision detection
- [x] Score tracking

### Phase 2: RL Environment Conversion
- [x] Converted game into a `SnakeGame` class
- [x] Implemented `step(action)`
- [x] Added reward system
- [x] Added terminal state (`done`)
- [x] Added `reset()`
- [x] Started `get_state()`
- [x] Improve state representation
- [x] Add danger detection
- [x] Add and test a simple agent

### Phase 3: Learning Agent
- [ ] Q-Learning implementation
- [ ] Experience replay memory
- [ ] Neural network implementation
- [ ] Training loop

### Phase 4: Optimization
- [ ] Reward tuning
- [ ] Hyperparameter tuning
- [ ] Performance improvements


---

## Technologies Used

- Python
- Pygame
- NumPy (planned)

The reinforcement learning logic is being implemented from scratch to understand the underlying concepts rather than relying on high-level ML frameworks.

---

## Reinforcement Learning Setup

The environment follows the standard RL workflow:

```text
State → Action → Reward → Next State
```

### Rewards

| Event | Reward |
|---------|---------|
| Normal Move | -1 |
| Eat Food | +10 |
| Collision / Death | -10 |

### Current Environment Features

- Action-based movement
- Reward system
- Terminal states (`done`)
- Environment reset
- State retrieval (`get_state()`)


---

## Project Structure

```text
snake-ai-from-scratch/
│
├── game/
│   └── snake_game.py
│
├── ai/
│   └──rule_agent.py
│
├── assets/
├── utils/
│
├── main.py
├── README.md
└── .gitignore
```

---

## Running the Project

### Clone the repository

```bash
git clone https://github.com/RaghavendraSani/snake-ai-from-scratch.git
```

### Move into the project directory

```bash
cd snake-ai-from-scratch
```

### Install dependencies

```bash
pip install pygame
```

### Run the project

```bash
python main.py
```


---

## Future Goals

- Train an AI that consistently collects food
- Improve survival time
- Visualize learning progress
- Experiment with different reward strategies
- Compare reinforcement learning approaches
- Build a stronger Snake-playing agent over time

---

## Learning Objectives

This project is focused on understanding:

- Reinforcement Learning fundamentals
- Environment design
- State representation
- Reward engineering
- Agent training
- AI decision-making

---

## Author

Built by Raghavendra Sani as a reinforcement learning project from scratch.