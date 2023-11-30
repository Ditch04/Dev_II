import random
import json
import argparse


class FlashCard:
    def __init__(self, question, answer, level=1):
        self.question = question
        self.answer = answer
        self.used = False  # Indicateur pour savoir si la carte a été utilisée dans la session de jeu
        self.level = level


class FlashCardGame:
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

    def move_card_down(self, card):
        if card.level < 3:
            card.level += 1

    def move_card_up(self, card):
        if card.level > 1:
            card.level -= 1

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(
                [{'question': card.question, 'answer': card.answer, 'used': card.used} for card in self.flashcards],
                file
            )

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.flashcards = [FlashCard(entry['question'], entry['answer']) for entry in data]

    def play(self):
        print("Bienvenue dans le jeu de flashcards !")
        #level = input("Choisissez le tas que vous voulez")

        while True:

            if all(card.used for card in self.flashcards):
                print("Vous avez utilisé toutes les cartes dans cette session.")
                print("Les options suivantes sont disponibles:")
                print("2. Ajouter une nouvelle flashcard")
                print("3. Quitter le jeu")
                choice = input("Choisissez une option (2/3): ")
            else:
                print("1. Tirer une carte")
                print("2. Ajouter une nouvelle flashcard")
                print("3. Quitter le jeu")
                choice = input("Choisissez une option (1/2/3): ")

            if choice == '1':
                card = self.draw_card()
                if card is None:
                    continue

                print(card.question)

                user_answer = input("Entrez votre réponse : ")

                if user_answer.lower() == card.answer.lower():
                    print("Bonne réponse !\n")
                else:
                    print(f"Mauvaise réponse. La réponse était {card.answer}\n")

                    # Marquer la carte comme non utilisée pour la session actuelle
                    card.used = False

            elif choice == '2':
                question = input("Entrez la nouvelle question : ")
                answer = input("Entrez la réponse correspondante : ")
                new_flashcard = FlashCard(question, answer, level=1)
                self.add_flashcard(new_flashcard)
                print("Nouvelle flashcard ajoutée.")

            elif choice == '3':
                break

            else:
                print("Option non valide. Veuillez choisir une option valide.")


parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='Chemin vers le fichier à ouvrir contenant les flashcards')
args = parser.parse_args()

if __name__ == "__main__":
    game = FlashCardGame()

    # Chargement des flashcards depuis un fichier s'il existe

    try:
        game.load_from_file(filename=args.file)
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
        exit(1)

    game.play()

    # Sauvegarde des flashcards dans un fichier après le jeu
    game.save_to_file(filename=args.file)