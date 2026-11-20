# 🎯 Python Number Guessing Game

A terminal-based number guessing game built with Python. Players can challenge themselves across four difficulty levels, track their performance, earn scores, and compete on a leaderboard.

This project was developed as a Python programming exercise, focusing on problem-solving, modular programming, input validation, and JSON-based data persistence.

## ✨ Features

- **Four Difficulty Levels:** Easy, Medium, Hard, and Expert.
- **Player Profiles:** Each player has individual statistics and game history.
- **Leaderboard:** Players are ranked by their total scores.
- **Score System:** Earn points based on the number of attempts needed to guess the secret number.
- **Penalty System:** Losing or quitting a game results in a score deduction.
- **Input Validation:** Prevents invalid inputs and repeated guesses.
- **Smart Number Range:** The available guessing range narrows based on previous guesses.
- **Data Persistence:** Player statistics and game history are stored in a JSON file.
- **Modular Architecture:** The project is organized into separate Python modules, each responsible for a specific part of the application.

## 🎮 Difficulty Levels

| Level  | Number Range | Attempts | Base Score |
| ------ | -----------: | -------: | ---------: |
| Easy   |         1–10 |        4 |        100 |
| Medium |         1–50 |        7 |        180 |
| Hard   |        1–100 |        8 |        300 |
| Expert |        1–500 |       10 |        450 |

## 🧮 Scoring System

Your score depends on how efficiently you guess the secret number.

The scoring formula is:

```python
efficiency = 0.5 + 0.5 * (
    (max_tries - attempts) / (max_tries - 1)
)

score = round(base_score * efficiency)
```

The game also applies penalties:

| Game Result |                Score |
| ----------- | -------------------: |
| Win         | Based on performance |
| Lose        |                  -20 |
| Quit        |                  -30 |

The fewer attempts you need, the higher your score!

## 🛠️ Technologies

- **Python 3**
- `random` – Generating the secret number.
- `json` – Saving and loading player data.
- `os` – Terminal screen management.
- `msvcrt` – Reading keyboard input on Windows.
- `sys` – Program termination.

No external Python packages are required.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-number-guessing-game.git
```

### 2. Navigate to the project directory

```bash
cd python-number-guessing-game
```

### 3. Run the game

```bash
python main.py
```

> **Note:** This project currently uses `msvcrt`, so it is designed to run on Windows.

## 📁 Project Structure

```text
python-number-guessing-game/
│
├── main.py
├── config.py
├── gameplay.py
├── ui.py
├── storage.py
├── utils.py
├── README.md
└── .gitignore
```

### Module Overview

| File          | Responsibility                                                       |
| ------------- | -------------------------------------------------------------------- |
| `main.py`     | Application entry point and main program flow.                       |
| `config.py`   | Game configuration, difficulty levels, and settings.                 |
| `gameplay.py` | Core game logic, guessing mechanics, and score calculation.          |
| `ui.py`       | Terminal interface, menus, player profiles, and leaderboard display. |
| `storage.py`  | Loading and saving player data using JSON.                           |
| `utils.py`    | Helper functions and shared utilities.                               |

The `players.json` file is generated automatically when player records are saved.

## 💾 Data Storage

Player information is stored locally in `players.json`.

The file contains:

- Total games played
- Number of wins and losses
- Total accumulated score
- Individual game history
- Secret numbers, attempts, difficulty levels, and results

## 👨‍💻 Author

**Mehdi Damerchi**

Computer Science Student | Python Programmer

---

_Built as a hands-on Python programming exercise._
