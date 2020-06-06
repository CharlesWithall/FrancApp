class Question:
    def __init__(self, clue="", answer_index=-1, answers=[]):
        self.clue = clue
        self.answer_index = answer_index
        self.answers = answers

    def get_correct_answer(self):
        return self.answers[self.answer_index]
