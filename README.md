# Tic-Tac-Toe-AI
Unbeatable Tic-Tac-Toe game using the Minimax algorithm. Built with Python and Pygame. CS50 AI project.


## About

This project was developed as part of the [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) course. The AI uses the Minimax algorithm to calculate the optimal move at every turn, making it impossible to beat — the best you can do is tie.

## How It Works

The Minimax algorithm recursively evaluates all possible game states to determine the best move:
- **Maximizing player (X):** Tries to maximize the score
- **Minimizing player (O):** Tries to minimize the score
- **Scores:** Win = +1, Loss = -1, Tie = 0

The AI looks ahead to all possible outcomes and always chooses the optimal path.

## Features

- Play as X or O
- AI opponent that plays optimally
- Clean graphical interface using Pygame
- Play again option after each game

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JawadAlnatah/Tic-Tac-Toe-AI.git
   cd tictactoe-ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python runner.py
   ```

## Requirements

- Python 3.x
- Pygame

## Project Structure

```
├── runner.py          # Main game loop and Pygame interface
├── tictactoe.py       # Game logic and Minimax AI implementation
├── requirements.txt   # Project dependencies
├── OpenSans-Regular.ttf   # Font file for the UI
└── README.md
```

## What I Learned

- Minimax algorithm and game theory
- Recursive problem-solving
- Building interactive applications with Pygame
- Python best practices

## Acknowledgments

This project is part of CS50's Introduction to Artificial Intelligence with Python course by Harvard University.
