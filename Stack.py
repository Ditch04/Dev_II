import random
from FlashCard import FlashCard


class Stack:
    def __init__(self):

        self.flashcards = []
        self.current_card_index = 0

    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)

    def draw_card(self):
        unused_flashcards = [card for card in self.flashcards if not card.used]
        if unused_flashcards:
            card = random.choice(unused_flashcards)
            card.used = True
            return card
        else:
            return None
