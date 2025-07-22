from model import GuessingGameModel, Verdict
import pytest


def test_make_guess_more_than_max():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100
    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    verdict = model.make_guess(101)
    assert verdict == Verdict.OUT_OF_BOUNDS

    # ensure state unchanged
    assert model.answer == answer
    assert model.attempts_left == attempts_left
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess
    assert model.is_game_over == False
    assert model.did_player_win == None


def test_make_guess_less_than_min():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100
    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    verdict = model.make_guess(0)
    assert verdict == Verdict.OUT_OF_BOUNDS

    # ensure state unchanged
    assert model.answer == answer
    assert model.attempts_left == attempts_left
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess
    assert model.is_game_over == False
    assert model.did_player_win == None


def test_make_guess_less_than_answer():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100
    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    verdict = model.make_guess(9)
    assert verdict == Verdict.TOO_LOW

    # ensure state unchanged
    assert model.answer == answer
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess

    assert model.attempts_left == attempts_left - 1
    assert model.is_game_over == False
    assert model.did_player_win == None


def test_make_guess_greater_than_answer():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100
    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    verdict = model.make_guess(99)
    assert verdict == Verdict.TOO_HIGH

    # ensure state unchanged
    assert model.answer == answer
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess

    assert model.attempts_left == attempts_left - 1
    assert model.is_game_over == False
    assert model.did_player_win == None


def test_make_guess_correct():
    test_values: list[int] = [10, 1, 100, 50, 57]
    for val in test_values:
        answer = val
        attempts_left = 7
        min_guess = 1
        max_guess = 100
        model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
        verdict = model.make_guess(val)
        assert verdict == Verdict.CORRECT

        # ensure state unchanged
        assert model.answer == answer
        assert model.min_guess == min_guess
        assert model.max_guess == max_guess

        assert model.attempts_left == attempts_left - 1
        assert model.is_game_over == True
        assert model.did_player_win == True


def test_make_guess_when_game_over():
    test_values: list[int] = [12, 10]
    for val in test_values:
        answer = 10
        attempts_left = 1
        min_guess = 1
        max_guess = 100
        model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
        verdict = model.make_guess(11)
        verdict = model.make_guess(val)
        assert verdict == Verdict.GAME_IS_OVER

        # ensure state unchanged
        assert model.answer == answer
        assert model.min_guess == min_guess
        assert model.max_guess == max_guess

        assert model.attempts_left == 0
        assert model.is_game_over == True
        assert model.did_player_win == False


def test_attempts_left_non_positive_value_error():
    test_values: list[int] = [-7, 0]
    for val in test_values:
        answer = 10
        attempts_left = val
        min_guess = 1
        max_guess = 100

        with pytest.raises(ValueError) as excinfo:
            GuessingGameModel(answer, attempts_left, min_guess, max_guess)

        assert str(excinfo.value) == "attempts_left should be positive."


def test_out_of_bounds_answer_value_error():
    answer = 0
    attempts_left = 7
    min_guess = 1
    max_guess = 100

    with pytest.raises(ValueError) as excinfo:
        GuessingGameModel(answer, attempts_left, min_guess, max_guess)

    assert str(
        excinfo.value) == "answer should be between or exactly min_guess and max_guess."


def test_min_guess_bigger_than_max_guess_value_error():
    answer = 100
    attempts_left = 7
    min_guess = 101
    max_guess = 100

    with pytest.raises(ValueError) as excinfo:
        GuessingGameModel(answer, attempts_left, min_guess, max_guess)

    assert str(
        excinfo.value) == "min_guess should be less than max_guess."
