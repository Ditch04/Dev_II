import random
import json
from FlashCard import FlashCard
from Stack import Stack
import argparse


class FlashCardGame:
    def __init__(self):
        self.stack = Stack()
        self.args = None
        self.card = None

    def save_to_file(self, filename):
        existing_cards_data = []
        try:
            with open(filename, 'r') as file:
                existing_cards_data = json.load(file)
        except FileNotFoundError:
            pass

        # Mettre à jour les données existantes avec les nouvelles informations
        for existing_card_data in existing_cards_data:
            for card in self.stack.flashcards:
                if (
                        existing_card_data['question'] == card.question
                        and existing_card_data['answer'] == card.answer
                ):
                    existing_card_data['level'] = card.level

        # Ajouter les nouvelles cartes qui n'étaient pas dans le fichier
        for card in self.stack.flashcards:
            if not any(
                    card_data['question'] == card.question and card_data['answer'] == card.answer
                    for card_data in existing_cards_data
            ):
                existing_cards_data.append(
                    {'question': card.question, 'answer': card.answer, 'level': card.level}
                )

        # Écrire les données mises à jour dans le fichier JSON
        with open(filename, 'w') as file:
            json.dump(existing_cards_data, file, indent=2)

    def load_from_file(self, filename, target_level):
        with open(filename, 'r') as file:
            data = json.load(file)
            for card in data:
                if card['level'] == target_level:
                    card = FlashCard(card['question'], card['answer'], level=card['level'])
                    self.stack.add_flashcard(card)

    def play(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('file', type=str, help='Chemin vers le fichier à ouvrir contenant les flashcards')
        parser.add_argument('--level', type=int, help="Specify the level of flashcards to use", default=None)
        self.args = parser.parse_args()

        try:
            self.load_from_file(filename=self.args.file, target_level=self.args.level)
        except FileNotFoundError:
            print("Le fichier spécifié n'existe pas.")
            exit(1)

        print("Bienvenue dans le jeu de flashcards !")

        while True:

            if all(card.used for card in self.stack.flashcards):
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
                self.card = self.stack.draw_card()
                if self.card is None:
                    continue

                print(self.card.question)

                user_answer = input("Entrez votre réponse : ")

                if user_answer.lower() == self.card.answer.lower():
                    print("Bonne réponse !\n")
                    self.card.increase_level()

                else:
                    print(f"Mauvaise réponse. La réponse était {self.card.answer}\n")
                    self.stack.add_flashcard(self.card)

            elif choice == '2':
                question = input("Entrez la nouvelle question : ")
                answer = input("Entrez la réponse correspondante : ")
                if self.args.level != 1:
                    new_flashcard = FlashCard(question, answer, level=1, used=True)
                else:
                    new_flashcard = FlashCard(question, answer, level=1)
                self.stack.add_flashcard(new_flashcard)
                print("Nouvelle flashcard ajoutée.")

            elif choice == '3':
                break

            else:
                print("Option non valide. Veuillez choisir une option valide.")

    def end_game(self):
        print("Game over!")
    # Sauvegarde des flashcards dans un fichier après le jeu
        self.save_to_file(filename=self.args.file)
