
class Stack:
    def __init__(self):
        self.flashcards = []
        self.current_card_index = 0

    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)

    
    def get_flashcard(self):
        if self.flashcards:
            return self.flashcards[self.current_card_index]
        else:
            return None
        
    def is_empty(self):
        return not bool(self.flashcards)
    
    