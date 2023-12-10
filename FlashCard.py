class FlashCard:
    def __init__(self, question, answer, level, used=False):
        self.question = question
        self.answer = answer
        self.level = level
        self.used = used  # Indicateur pour savoir si la carte a été utilisée dans la session de jeu

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_level(self):
        return self.level

    def set_question(self, question):
        self.question = question

    def set_answer(self, answer):
        self.answer = answer

    def increase_level(self):
        if self.level < 3:
            self.level += 1

