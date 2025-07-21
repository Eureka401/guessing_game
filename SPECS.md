
# SPECS.md

## 🎯 Project: Console-Based Number Guessing Game

This is a simple number guessing game implemented using **Model-View-Controller (MVC)** architecture in Python. The game picks a random number, and the player has limited attempts to guess it. The program provides feedback on whether the guess is too high, too low, out of bounds, or correct.

---

## 🧠 Design Overview

### 📐 Architecture
- **Model:** Manages game state and logic.
- **View:** Handles input/output with the player.
- **Controller:** Orchestrates the game flow between Model and View.

---

## 🧩 Components

### 1. `Verdict` Enum
Enum of possible outcomes of a guess:
```python
class Verdict(StrEnum):
    CORRECT
    TOO_HIGH
    TOO_LOW
    OUT_OF_BOUNDS
    GAME_IS_OVER
````

---

### 2. `GuessingGameModel`

Encapsulates all the core logic and game state.

#### Constructor:

```python
GuessingGameModel(answer: int, attempts_left: int, min_guess: int, max_guess: int)
```

#### Properties:

* `answer`: the correct number
* `attempts_left`: remaining attempts
* `min_guess`, `max_guess`: valid range
* `is_game_over`: bool flag
* `did_player_win`: bool flag

#### Methods:

* `make_guess(guess: int) -> Verdict`:

  * Reduces attempts accordingly.
  * Updates game state flags.
* `_check_guess(guess: int) -> Verdict`:

  * Returns appropriate `Verdict` without modifying state.

---

### 3. `GuessingGameView`

Handles all user interaction (I/O).

#### Methods:

* `ask_for_guess(min_guess: int, max_guess: int) -> int`

  * Prompts the user to enter a guess.
* `print_verdict(verdict: Verdict, min_guess: int, max_guess: int)`

  * Prints feedback based on the guess.
* `print_lose_message(answer: int)`

  * Prints final lose message if player fails.

---

### 4. `GuessingGameController`

Coordinates between model and view.

#### Constructor:

```python
GuessingGameController(model: GuessingGameModel, view: GuessingGameView)
```

#### Method:

* `start()`:

  * Main game loop.
  * Ends when game is over.
  * Prompts for guess, evaluates it, prints result.
  * If game ends in failure, prints the correct answer.

---

## 🧪 Gameplay Flow

1. Initialize a random answer between 1 and 100.
2. Set up the model with 8 attempts.
3. Start the controller loop:

   * Ask user for guess.
   * Evaluate and respond with verdict.
   * Stop if correct guess or attempts run out.

---

## 🛠 Example Bootstrapping Code

```python
answer = random.randint(1, 100)
model = GuessingGameModel(answer, 8, 1, 100)
view = GuessingGameView()
controller = GuessingGameController(model, view)
controller.start()
```

---

## 🧠 Key Rules

* If guess is outside the valid range: return `OUT_OF_BOUNDS`, don’t consume an attempt.
* If guess is correct: return `CORRECT`, end game, player wins.
* If guess is incorrect (but within bounds): return `TOO_LOW` or `TOO_HIGH`, consume one attempt.
* When attempts reach zero: game ends, player loses.

---

## 💡 Suggested Enhancements (Optional for Future Iteration)

* Add difficulty levels that adjust attempt count.
* Record and display past guesses.
* Add CLI color for verdicts (e.g., green for win, red for loss).
* Unit tests for each component.
* High score tracking.

