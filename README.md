# Implementing Snake and Ladders Game

This project aims to develop a simple version of the classic board game, Snake and Ladders. The game will support multiple players competing on a customizable board that has dynamically placed snakes and ladders. The random placement of snakes and ladders ensures a unique and engaging playthrough every time.

---

## Acceptance Criteria:

### Board Setup:
- The board can be initialized with a size based on user input for horizontal and vertical dimensions.
- Snakes and ladders are randomly placed on the board with constraints:
  - **Snakes:** Start at a higher position and end at a lower one.
  - **Ladders:** Start at a lower position and end at a higher one.
  - Snakes and ladders must not start or end at the same position as another snake or ladder.

### Player Management:
- The game should support multiple players, with each player having a unique ID and name.
- Players are initialized at position 0.

### Gameplay Mechanics:
- Players take turns rolling two six-sided dice to determine their move distance.
- If the rolled dice result would exceed the board's final square, the player's position remains unchanged for that turn.
- If a player lands on a snake, their position moves to the snake's endpoint.
- If a player lands on a ladder, their position moves to the ladder’s endpoint.

### Winning Condition:
- The first player to reach the final square on the board (exact match required) is declared the winner.

### User Interaction:
- The console prompts each player to roll the dice on their turn.
- After each action, the game displays current player positions and any interactions with snakes or ladders.

### Notable Edge Cases:
- Handle scenarios where a player could overshoot the winning square.
- Ensure unique positions for each snake and ladder, allowing no overlap.

---

## Notes:
- Players press Enter on their turn to roll the dice, enhancing interactive play in a console environment.
- Ensure robust handling of player and board state to maintain consistent gameplay.
- Random generations should ensure no overlap in start or end points of snakes and ladders for each game instance.

---


_Feel free to clone this repository, contribute, and experience the simple joy of a classic board game reimagined in a digital format!_
