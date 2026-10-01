<div align="center">

# 🐍 Snake AI From Scratch 🤖

### Building an Intelligent Snake using Reinforcement Learning from Scratch

*A complete Reinforcement Learning project built without high-level machine learning frameworks.*

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-Game_Development-green?style=for-the-badge)
![Reinforcement Learning](https://img.shields.io/badge/Reinforcement-Learning-orange?style=for-the-badge)
![GitHub](https://img.shields.io/badge/Open_Source-GitHub-black?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Project-In_Progress-yellow?style=for-the-badge)

</div>

---

# 📖 About The Project

This project aims to build a **Snake AI capable of learning how to play the classic Snake game completely from scratch using Reinforcement Learning**.

Unlike many Reinforcement Learning tutorials that depend on libraries such as:

- TensorFlow
- PyTorch
- Stable Baselines
- OpenAI Gym

this project focuses on **understanding every single component** involved in building an intelligent agent.

Every major part of the system is implemented manually, including:

- Environment Design
- Reward Engineering
- State Representation
- Neural Network
- Q-Learning
- Experience Replay
- Agent Training
- Decision Making

The primary objective is **learning**, not simply obtaining a trained model.

---

# 🎯 Project Objectives

This project has been designed with the following goals:

- Build a fully functional Snake game from scratch.
- Convert the game into a Reinforcement Learning environment.
- Implement an intelligent agent capable of learning through interaction.
- Build every major RL component manually.
- Understand how Reinforcement Learning works internally.
- Avoid relying on high-level machine learning frameworks.
- Document every stage of development.

---

# ✨ Features

## ✅ Currently Implemented

- Playable Snake Game
- Object-Oriented Code Structure
- Food Generation
- Snake Growth
- Collision Detection
- Score Tracking
- Reinforcement Learning Environment
- Action-Based Control
- Reward System
- Episode Reset
- State Representation
- Rule-Based Testing Agent
- Git Version Control
- GitHub Documentation

---

## 🚧 Under Development

- Neural Network from Scratch
- Q-Learning
- Experience Replay
- Target Network
- Deep Q-Learning
- Model Training
- Hyperparameter Tuning
- Performance Evaluation

---

# 📚 Table of Contents

- [About The Project](#-about-the-project)
- [Project Objectives](#-project-objectives)
- [Features](#-features)
- [Current Progress](#-current-progress)
- [Project Architecture](#-project-architecture)
- [Reinforcement Learning Pipeline](#-reinforcement-learning-pipeline)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Running the Project](#-running-the-project)
- [Technologies Used](#-technologies-used)
- [Development Roadmap](#-development-roadmap)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Contributing](#-contributing)
- [Author](#-author)

---

# 📈 Current Progress

The project is being developed incrementally, with each phase focusing on a specific Reinforcement Learning concept. The objective is not only to build an AI that can play Snake, but to understand every component involved in designing, training, and optimizing an intelligent agent.

---

## ✅ Phase 1 — Building the Snake Game

The first phase focused on creating a fully functional Snake game using Python and Pygame.

### Completed Features

- ✔️ Game Window
- ✔️ Snake Movement
- ✔️ Food Generation
- ✔️ Snake Growth
- ✔️ Dynamic Score Counter
- ✔️ Wall Collision Detection
- ✔️ Self Collision Detection
- ✔️ Game Reset
- ✔️ Frame Rate Control
- ✔️ Object-Oriented Design

At the end of this phase, the game was completely playable by a human.

---

## ✅ Phase 2 — Converting the Game into an RL Environment

A normal Snake game cannot directly train an AI.

To solve this, the game was redesigned as a Reinforcement Learning environment.

Major components implemented include:

### Environment Class

The entire game was converted into a reusable environment through the `SnakeGame` class.

Responsibilities include:

- Managing the game state
- Handling movement
- Collision detection
- Food generation
- Reward calculation
- Episode reset
- Rendering

---

### Step Function

A dedicated `step(action)` function was implemented to allow an external AI agent to interact with the environment.

Every call to `step(action)` performs:

1. Receive an action from the agent
2. Move the snake
3. Update the snake body
4. Detect collisions
5. Calculate reward
6. Determine whether the episode has ended
7. Return the updated environment information

This follows the standard Reinforcement Learning interaction pattern.

---

### Reward Engineering

The environment provides numerical feedback to guide the learning process.

| Event | Reward |
|---------|---------:|
| Normal Move | -1 |
| Eat Food | +10 |
| Wall Collision | -10 |
| Self Collision | -10 |

This reward system encourages:

- Efficient movement
- Survival
- Food collection
- Avoiding dangerous actions

---

### Episode Management

Terminal states are represented using:

```python
done = True
```

The environment automatically resets after an episode finishes, preparing it for the next training iteration.

---

### State Representation

Current implementation includes:

- Snake Head Position
- Food Position
- Basic Environment State

Currently under development:

- Danger Detection
- Relative Food Direction
- Direction Encoding
- Final AI State Vector

---

### Rule-Based Agent

A simple rule-based agent has been introduced to test the environment before implementing machine learning.

Its purpose is to verify:

- Environment stability
- Correct reward generation
- State transitions
- Collision detection
- Episode reset

---

# 🏗️ Project Architecture

```
                    +----------------+
                    |     Agent      |
                    +----------------+
                             |
                             | Action
                             ▼
                  +----------------------+
                  |   Snake Environment  |
                  +----------------------+
                  |                      |
                  | Snake Movement       |
                  | Food Generation      |
                  | Collision Detection  |
                  | Reward Function      |
                  | Episode Handling     |
                  | Rendering            |
                  +----------------------+
                             |
                             |
                             ▼
              Next State + Reward + Done
```

---

# 🧠 Reinforcement Learning Pipeline

The environment follows the standard Reinforcement Learning workflow.

```
Current State
      │
      ▼
Agent selects Action
      │
      ▼
Environment executes Action
      │
      ▼
Snake moves
      │
      ▼
Environment calculates Reward
      │
      ▼
New State generated
      │
      ▼
Episode ends?
      │
 ┌────┴─────┐
 │          │
No         Yes
 │          │
 ▼          ▼
Continue   Reset Environment
```

This interaction loop will later be used to train the Neural Network using Q-Learning.

---

# 🎮 Environment Components

Current environment consists of:

### Input

- Agent Action

### Processing

- Movement Logic
- Boundary Checking
- Collision Detection
- Reward Assignment
- Snake Growth
- Food Respawning

### Output

- Next State
- Reward
- Done Flag

---

# 🗺️ Planned Project Structure

```text
snake-ai-from-scratch/
│
├── ai/
│   ├── neural_network.py
│   ├── q_learning.py
│   ├── replay_memory.py
│   ├── trainer.py
│   └── rule_agent.py
│
├── game/
│   ├── snake_game.py
│   ├── food.py
│   ├── snake.py
│   └── constants.py
│
├── assets/
│   ├── screenshots/
│   └── demo/
│
├── outputs/
│   ├── models/
│   ├── graphs/
│   └── logs/
│
├── utils/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

> This represents the intended architecture of the project as additional Reinforcement Learning components are implemented.

---

# 🧪 Current Testing

The following components have been verified through manual testing:

- ✅ Snake Movement
- ✅ Food Collection
- ✅ Snake Growth
- ✅ Reward Assignment
- ✅ Collision Detection
- ✅ Episode Reset
- ✅ Environment Stability
- ✅ State Updates

Further testing will be performed once the learning agent is implemented.

---

# 🛠️ Technologies Used

## Current Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pygame | Game development and rendering |
| Git | Version control |
| GitHub | Project hosting and documentation |
| Object-Oriented Programming | Modular code architecture |

---

## Planned Technologies

| Technology | Purpose |
|------------|---------|
| NumPy | Neural Network and mathematical operations |
| Custom Neural Network | Function approximation |
| Q-Learning | Initial Reinforcement Learning algorithm |
| Experience Replay | Improve training stability |
| Deep Q-Network (DQN) | Future enhancement after completing Q-Learning |

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/RaghavendraSani/snake-ai-from-scratch.git
```

Move into the project directory

```bash
cd snake-ai-from-scratch
```

---

## Create a Virtual Environment (Recommended)

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install pygame
```

Future versions will also require:

```bash
pip install numpy
```

---

# ▶️ Running the Project

Launch the game using

```bash
python main.py
```

The current version launches the Snake environment and allows testing of the RL environment components.

---

# 🧩 Core Components

The project is divided into independent modules.

## Game Module

Responsible for:

- Rendering
- Snake movement
- Food spawning
- Collision detection
- Reward calculation
- State updates

---

## AI Module

Current

- Rule-based testing agent

Future

- Neural Network
- Q-Learning
- Experience Replay
- Training logic

---

## Utilities

Helper functions and reusable utilities shared across modules.

---

# 🧠 Reinforcement Learning Roadmap

## Phase 1 ✅

Game Development

- Build Snake Game
- Implement collisions
- Add scoring
- Add food generation

Completed ✔

---

## Phase 2 ✅

Environment Conversion

- SnakeGame class
- step(action)
- Reward system
- done state
- reset()
- get_state()
- Rule Agent

Completed ✔

---

## Phase 3 🚧

State Engineering

- Final state vector
- Danger detection
- Food direction encoding
- Direction encoding
- Environment testing

Status: In Progress

---

## Phase 4 🚧

Neural Network

Planned implementation

- Dense Layers
- ReLU Activation
- Output Layer
- Forward Propagation
- Backpropagation

Status: Planned

---

## Phase 5 🚧

Q-Learning

Implementation goals

- Bellman Equation
- Q-value Updates
- Loss Calculation
- Target Prediction
- Training Step

Status: Planned

---

## Phase 6 🚧

Experience Replay

Features

- Replay Memory
- Random Mini-batches
- Improved Stability

Status: Planned

---

## Phase 7 🚧

Training

Objectives

- Autonomous Learning
- Increasing Average Score
- Better Survival
- Efficient Food Collection

Status: Planned

---

## Phase 8 🚧

Optimization

Future work

- Reward tuning
- Hyperparameter tuning
- Learning rate experiments
- Exploration decay
- Model optimization

Status: Planned

---

# 📅 Development Timeline

```
Snake Game
      │
      ▼
RL Environment
      │
      ▼
State Representation
      │
      ▼
Neural Network
      │
      ▼
Q-Learning
      │
      ▼
Experience Replay
      │
      ▼
Training
      │
      ▼
Optimization
      │
      ▼
Final Intelligent Agent
```

---

# 🚀 Future Improvements

The long-term vision for this project includes:

- Complete Deep Q-Learning implementation
- Improved reward engineering
- Better state representation
- Dynamic difficulty
- Model checkpoint saving
- Automatic training visualization
- Performance graphs
- TensorBoard-style metrics (custom implementation)
- Training statistics dashboard
- Configurable environment settings
- Benchmark against rule-based agents
- Export trained models
- Evaluate multiple reward strategies

---

# 📊 Planned Performance Metrics

Once training begins, the following metrics will be tracked.

- Average Score
- Maximum Score
- Average Reward
- Survival Time
- Exploration Rate
- Training Loss
- Episode Count
- Learning Curve

Performance graphs will be added to this repository as the project progresses.

---

# 📷 Screenshots

> Screenshots will be added as the project progresses.

> Gameplay screenshots and training visualizations will be added in future updates.

Planned additions:

- 📸 Current gameplay
- 🧠 Rule-based agent gameplay
- 🤖 AI training progress
- 📈 Learning graphs
- 🏆 Final trained AI performance

# 🎥 Demo

A demonstration video/GIF showing the AI's learning progress will be added after the training pipeline is complete.

Future demonstrations will include:

- Human gameplay
- Rule-based agent
- Early training
- Mid training
- Fully trained AI
- Performance comparison

---

# 📊 Training Results

This section will be updated once the Reinforcement Learning agent begins training.

Future metrics include:

| Metric | Status |
|---------|---------|
| Average Score | ⏳ Planned |
| Highest Score | ⏳ Planned |
| Average Reward | ⏳ Planned |
| Episode Length | ⏳ Planned |
| Training Loss | ⏳ Planned |
| Exploration Rate (ε) | ⏳ Planned |
| Learning Curve | ⏳ Planned |

Example graphs that will be included:

- Score vs Episodes
- Reward vs Episodes
- Loss vs Episodes
- Exploration Decay
- Moving Average Score

---

# 📁 Repository Structure

```
snake-ai-from-scratch
│
├── ai/
│   ├── neural_network.py
│   ├── q_learning.py
│   ├── replay_memory.py
│   ├── rule_agent.py
│   └── trainer.py
│
├── game/
│   ├── snake_game.py
│   ├── food.py
│   ├── snake.py
│   └── constants.py
│
├── assets/
│   ├── screenshots/
│   ├── demo/
│   └── icons/
│
├── utils/
│
├── outputs/
│   ├── models/
│   ├── graphs/
│   └── logs/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

> **Note:** Some files and directories shown above represent the planned project architecture and will be added in future development phases.

---

# 📖 Learning Outcomes

This project is being built to gain a practical understanding of the complete Reinforcement Learning pipeline.

Topics explored include:

## Reinforcement Learning

- Environment Design
- Agent-Environment Interaction
- Markov Decision Process
- Reward Engineering
- State Representation
- Exploration vs Exploitation
- Q-Learning
- Deep Q-Learning
- Experience Replay
- Target Networks

---

## Machine Learning

- Neural Networks
- Forward Propagation
- Backpropagation
- Gradient Descent
- Loss Functions
- Optimization

---

## Software Engineering

- Object-Oriented Programming
- Modular Architecture
- Debugging
- Testing
- Version Control
- Documentation
- Project Organization

---

# 💡 Design Philosophy

The objective of this repository is not to build the strongest Snake AI in the shortest amount of time.

Instead, the project focuses on understanding every layer involved in creating an intelligent agent.

Every major algorithm and component is implemented manually whenever possible so that the learning process remains transparent and educational.

This repository documents not only the final implementation but also the engineering decisions and iterative improvements made throughout development.

---

# 🤝 Contributing

Although this project is primarily a personal learning journey, suggestions and constructive feedback are always welcome.

If you discover a bug, identify an optimization, or have ideas for improving the implementation, feel free to open an issue or submit a pull request.

---

# ⭐ Future Vision

The long-term goal of this project is to evolve from a simple Snake game into a fully featured Reinforcement Learning playground capable of demonstrating modern RL techniques implemented from scratch.

Planned milestones include:

- ✅ Complete RL environment
- 🔄 Neural Network implementation
- 🔄 Q-Learning
- 🔄 Deep Q-Network (DQN)
- 🔄 Experience Replay
- 🔄 Model persistence
- 🔄 Training visualization
- 🔄 Performance benchmarking
- 🔄 Configurable environments
- 🔄 AI vs Rule-Based comparison

---

# 🎯 Current Development Status

| Component | Status |
|-----------|--------|
| Snake Game | ✅ Complete |
| RL Environment | ✅ Complete |
| Rule-Based Agent | ✅ Complete |
| State Representation | 🚧 In Progress |
| Neural Network | ⏳ Planned |
| Q-Learning | ⏳ Planned |
| Experience Replay | ⏳ Planned |
| Training Pipeline | ⏳ Planned |
| Model Optimization | ⏳ Planned |

# 📚 References

The following resources have inspired or supported the concepts explored in this project:

- Sutton & Barto — *Reinforcement Learning: An Introduction*
- Python Documentation
- Pygame Documentation
- NumPy Documentation
- DeepMind DQN Paper (for conceptual understanding)

---

# 📜 License

This project is released under the MIT License.

You are free to use, modify, and distribute this project for educational and personal purposes.

---

# 👨‍💻 Author

<div align="center">

## Raghavendra Sani

**B.Tech Computer Science Engineering**

Building Artificial Intelligence systems from scratch to understand the foundations of Reinforcement Learning, Machine Learning, and Neural Networks.

### Connect with me

- GitHub: https://github.com/RaghavendraSani

If you found this project interesting, consider giving it a ⭐ on GitHub.

It motivates me to continue building and documenting projects like this.

---

### 🚀 "Understand Every Layer. Build Every Component."

</div>