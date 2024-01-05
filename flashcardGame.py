from stack import Stack
import json
from flashcard import Flashcard


class FlashcardGame:
    def __init__(self):
        self.stack = Stack()
        self.card = Flashcard
        self.game_over = False

    def load_from_file(self, filename, level):
        try:
            with open(filename, 'r') as file:
                flashcards_data = json.load(file)

            for card_data in flashcards_data:
                if int(card_data['level']) == int(level):
                    question = card_data.get('question', '')
                    answer = card_data.get('answer', '')
                    level = card_data.get('level')
                    used = card_data.get('used', False)

                    flashcard = Flashcard(question, answer, level, used)
                    self.stack.add_flashcard(flashcard)
                else: 
                    continue

            print("Flashcards chargées avec succès.")
             

        except FileNotFoundError:
            print("Le fichier spécifié n'existe pas.")
        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement des flashcards : {e}")

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.stack.add_flashcard(flashcard)
        print("Flashcard ajoutée avec succès.") 


    def save_to_file(self, filename):    
        flashcards_data = []
        for card in self.stack.flashcards:
            flashcards_data.append({
                'question': card.question,
                'answer': card.answer,
                'level': card.level,
                'used': card.used
            })
        
        print(flashcards_data)
        
        
        
        with open(filename, 'w') as file:
            json.dump(flashcards_data, file, indent=4)
        
            print("Flashcards sauvegardées avec succès.")

    
    def get_current_flashcard(self):
        if not self.stack.is_empty():
            self.current_card = self.stack.get_flashcard()
            return self.current_card
        else:
            return None
    