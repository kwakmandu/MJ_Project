from baseballresult import BaseballResult


class Baseball:
    LENGTH_OF_ANSWER = 3

    def __init__(self):
        self.answer = 123

    def assert_if_illegal_input(self, user_try):
        if not user_try:
            raise TypeError()

        if len(str(user_try)) != self.LENGTH_OF_ANSWER:
            raise TypeError()

        for num in str(user_try):
            if not ord("0") <= ord(num) <= ord("9"):
                raise TypeError()

        if len(set(list(str(user_try)))) != self.LENGTH_OF_ANSWER:
            raise TypeError()

    def guess(self, user_try):
        self.assert_if_illegal_input(user_try)


        return BaseballResult(True, 3, 0)
