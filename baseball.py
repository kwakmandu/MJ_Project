class Baseball:
    def __init__(self):
        self.answer = 123

    def guess(self, user_try):
        if not user_try:
            raise TypeError()