from unittest import TestCase

from baseball import Baseball


class TestBaseball(TestCase):
    def setUp(self):
        self.game = Baseball()

    def assert_if_illegal_argument(self, user_try):
        try:
            self.game.guess(user_try)
            self.fail()
        except TypeError:
            pass

    def test_illegal_input(self):
        test_cases = ("None", "12", 12, "1004", 0, "12s", "121")
        for test_case in test_cases:
            with self.subTest(f"{test_case}"):
                self.assert_if_illegal_argument(test_case)

    def test_all_strike_input(self):
        game_result = self.game.guess("123")

        self.assertIsNotNone(game_result)
        self.assertTrue(game_result.get_solved())
        self.assertEqual(3, game_result.get_strikes())
        self.assertEqual(0, game_result.get_balls())

