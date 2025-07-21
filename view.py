from model import Verdict


class GuessingGameView:
    def ask_for_guess(self, min_guess: int, max_guess: int) -> int:
        raw_guess = input(
            f"Please enter a number from {min_guess}-{max_guess} (inclusive).\n")

        while not raw_guess.isnumeric():
            raw_guess = input(
                f"Please enter a number from {min_guess}-{max_guess} (inclusive).\n")

        return int(raw_guess)

    def print_verdict(self, verdict: Verdict, min_guess: int, max_guess: int):
        match verdict:
            case Verdict.OUT_OF_BOUNDS:
                print(
                    f"Guess is not within the range {min_guess}-{max_guess} (inclusive).")
            case Verdict.CORRECT:
                print("You win!")
            case Verdict.TOO_HIGH:
                print("Too high!")
            case Verdict.TOO_LOW:
                print("Too low!")
            case Verdict.GAME_IS_OVER:
                print("Game is over! Restart to continue...")

    def lose_message(self, answer: int):
        print(f"You lose! The answer is {answer}.")
