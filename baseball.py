from baseballresult import BaseballResult


class Baseball:
    LENGTH_OF_ANSWER = 3

    def __init__(self):
        self.answer = "123"

    def assert_if_input_is_legal(self, user_try):
        if not user_try:
            raise TypeError()

        if len(user_try) != self.LENGTH_OF_ANSWER:
            raise TypeError()

        for num in user_try:
            if not ord("0") <= ord(num) <= ord("9"):
                raise TypeError()

        if len(set(list(user_try))) != self.LENGTH_OF_ANSWER:
            raise TypeError()

    def guess(self, user_try):
        user_try = str(user_try)
        self.assert_if_input_is_legal(user_try)
        solved, strikes, balls = self.compare_user_try_with_answer(user_try)
        return BaseballResult(solved, strikes, balls)

    def compare_user_try_with_answer(self, user_try):
        solved = False
        strikes = 0
        balls = 0

        for i in range(3):
            if user_try[i] == self.answer[i]:
                strikes += 1
            elif user_try[i] in self.answer:
                balls += 1

        if strikes == 3:
            solved = True

        return solved, strikes, balls
