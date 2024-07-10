from unittest import TestCase

from baseball import Baseball


class TestBaseball(TestCase):
    def setUp(self):
        self.game = Baseball()

    def test_no_input(self):
        with self.assertRaises(TypeError):
            self.game.guess(None)


