from model import GuessingGameModel
from view import GuessingGameView


class GuessingGameController:
    def __init__(self, model: GuessingGameModel, view: GuessingGameView) -> None:
        self.model = model
        self.view = view

    def start(self):
        min_guess, max_guess, answer = self.model.min_guess, self.model.max_guess, self.model.answer
        while not self.model.is_game_over:
            user_guess = self.view.ask_for_guess(min_guess, max_guess)
            verdict = self.model.make_guess(user_guess)
            self.view.print_verdict(verdict, min_guess, max_guess)

        assert self.model.did_player_win != None
        if not self.model.did_player_win:
            self.view.lose_message(answer)
