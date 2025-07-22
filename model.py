from enum import StrEnum, auto


class Verdict(StrEnum):
    CORRECT = auto()
    TOO_HIGH = auto()
    TOO_LOW = auto()
    OUT_OF_BOUNDS = auto()
    GAME_IS_OVER = auto()


class GuessingGameModel:
    def __init__(self, answer: int, attempts_left: int, min_guess: int, max_guess: int) -> None:
        if attempts_left <= 0:
            raise ValueError("attempts_left should be positive.")

        elif min_guess > max_guess:
            raise ValueError("min_guess should be less than max_guess.")

        elif answer < min_guess or answer > max_guess:
            raise ValueError(
                "answer should be between or exactly min_guess and max_guess.")

        else:
            self._answer = answer
            self._attempts_left = attempts_left
            self._min_guess = min_guess
            self._max_guess = max_guess
            self._is_game_over = False
            self._did_player_win: bool | None = None

    @property
    def answer(self):
        return self._answer

    @property
    def attempts_left(self):
        return self._attempts_left

    @property
    def min_guess(self):
        return self._min_guess

    @property
    def max_guess(self):
        return self._max_guess

    @property
    def is_game_over(self):
        return self._is_game_over

    @property
    def did_player_win(self):
        return self._did_player_win

    def make_guess(self, guess: int) -> Verdict:
        verdict = self._check_guess(guess)

        match verdict:
            case Verdict.CORRECT:
                self._attempts_left -= 1
                self._is_game_over = True
                self._did_player_win = True
            case Verdict.TOO_HIGH | Verdict.TOO_LOW:
                self._attempts_left -= 1
            case _:
                pass

        if self.attempts_left == 0 and not self.is_game_over:
            self._is_game_over = True
            self._did_player_win = False

        return verdict

    def _check_guess(self, guess: int) -> Verdict:
        if self.is_game_over:
            return Verdict.GAME_IS_OVER
        elif self.min_guess > guess or guess > self.max_guess:
            return Verdict.OUT_OF_BOUNDS
        elif guess == self.answer:
            return Verdict.CORRECT
        elif guess > self.answer:
            return Verdict.TOO_HIGH
        else:
            return Verdict.TOO_LOW
