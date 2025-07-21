from controller import GuessingGameController
from model import GuessingGameModel
from view import GuessingGameView
from random import randint


if __name__ == "__main__":
    answer = randint(1, 100)
    model = GuessingGameModel(answer, 8, 1, 100)
    view = GuessingGameView()
    controller = GuessingGameController(model, view)
    controller.start()
