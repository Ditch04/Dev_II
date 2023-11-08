import random


class FlashCard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class FlashCardGame:
    def __init__(self):
        self.flashcards = []
        self.current_card_index = 0

    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)

    def draw_card(self):
        if self.current_card_index < len(self.flashcards):
            card = self.flashcards[self.current_card_index]
            self.current_card_index += 1
            return card
        else:
            return None

    def play(self):
        while True:
            card = self.draw_card()
            if card is None:
                print("Vous avez vu toutes les cartes.")
                break

            input("Appuyez sur 'enter' pour voir la question...")
            print(card.question)

            input("Appuyez sur 'enter' pour voir la réponse...")
            print(card.answer)

            choice = input("Voulez-vous tirer une nouvelle carte ? (Oui/Non): ")
            if choice.lower() != 'oui':
                break


if __name__ == "__main__":
    game = FlashCardGame()


game.add_flashcard(FlashCard("Quelle est la capitale de la Belgique ?", "Bruxelles"))
game.add_flashcard(FlashCard("Question 2", "Réponse 2"))
game.add_flashcard(FlashCard("Question 3", "Réponse 3"))

random.shuffle(game.flashcards)

game.play()
