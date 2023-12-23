# Snake Game 🐍

This is a simple Snake Game implemented in Python using the Turtle graphics library. The game features a snake that the player controls to eat food and grow longer. The objective is to achieve the highest score possible without colliding with the walls or the snake's own tail.

## Getting Started

To run the Snake Game, make sure you have Python installed on your system. Clone this repository and run the `snake_game.py` file.

```bash
python snake_game.py
```
## How to Play
* Use the arrow keys (Up, Down, Left, Right) to control the snake's direction.
* The snake will continuously move in the current direction.
* The goal is to eat the food represented by a green square to increase your score.
* Avoid colliding with the walls or the snake's own tail.

## Rules
* Collision with the walls or the snake's own tail will end the game.
* Each time the snake eats food, it will grow longer.

## Features
* **Snake:** The main snake class `snake.py` handles the snake's movement and growth.
* **Food:** The food class `food.py` manages the appearance and refreshment of the food on the screen.
* **Scoreboard:** The scoreboard class `scoreboard.py` keeps track of the player's score and displays it on the screen.

## Controls
* **Up Arrow ⬆️:** Move the snake up.
* **Down Arrow ⬇️:** Move the snake down.
* **Left Arrow ⬅️:** Move the snake left.
* **Right Arrow ➡️:** Move the snake right.

## Dependencies
* Python 3.x
* Turtle graphics library

## License
This project is licensed under the [MIT License](https://github.com/ssalidm/snake-game/blob/main/LICENSE).


## Acknowledgments
This Snake Game is inspired by classic arcade games and serves as a simple implementation for learning and entertainment purposes.