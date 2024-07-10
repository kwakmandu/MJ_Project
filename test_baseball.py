from unittest import TestCase

from baseball import Baseball


class TestBaseball(TestCase):
    def setUp(self):
        self.game = Baseball()

    def assert_if_argument_is_legal(self, user_try):
        try:
            self.game.guess(user_try)
            self.fail()
        except TypeError:
            pass

    def assert_game_result_is_right(self, game_result, solved, strikes, balls):
        self.assertIsNotNone(game_result)
        self.assertEqual(solved, game_result.get_solved())
        self.assertEqual(strikes, game_result.get_strikes())
        self.assertEqual(balls, game_result.get_balls())

    def test_illegal_input(self):
        test_cases = ("None", "12", 12, "1004", 0, "12s", "121")
        for test_case in test_cases:
            with self.subTest(f"{test_case}"):
                self.assert_if_argument_is_legal(test_case)

    def test_no_strike_no_ball_input(self):
        self.assert_game_result_is_right(self.game.guess("789"), False, 0, 0)

    def test_all_strikes_input(self):
        self.assert_game_result_is_right(self.game.guess("123"), True, 3, 0)

    def test_all_balls_input(self):
        self.assert_game_result_is_right(self.game.guess("312"), False, 0, 3)

    def test_1_strike_no_ball_input(self):
        self.assert_game_result_is_right(self.game.guess("176"), False, 1, 0)

    def test_1_strike_2_balls_input(self):
        self.assert_game_result_is_right(self.game.guess("132"), False, 1, 2)

    def test_2_strikes_0_ball_input(self):
        self.assert_game_result_is_right(self.game.guess("127"), False, 2, 0)
