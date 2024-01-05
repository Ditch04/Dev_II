import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from flashcardGame import FlashcardGame
import os


class FlashcardGUI:
    def __init__(self, master):

        

        self.master = master
        master.title('Flashcards App')
        master.geometry('500x400')

        self.style = Style(theme='superhero')
        self.style.configure('TLabel', font=('TkDefaultFont', 18))
        self.style.configure('TButton', font=('TkDefaultFont', 16))

        set_name_var = tk.StringVar()
        question = tk.StringVar()
        answer = tk.StringVar()

        self.flashcard_game = FlashcardGame()
        
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill='both', expand=True)

        self.create_set_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.create_set_frame, text="Créer une pile")

        ttk.Label(self.create_set_frame, text="Définir le nom de la pile:").pack(padx=5, pady=5)
        self.set_name_entry = ttk.Entry(self.create_set_frame, textvariable=set_name_var, width=30)
        self.set_name_entry.pack(padx=5, pady=5)

        ttk.Label(self.create_set_frame, text='Question:').pack(padx=5, pady=5)
        self.word_entry = ttk.Entry(self.create_set_frame, textvariable= question, width=30)
        self.word_entry.pack(padx=5, pady=5)

        ttk.Label(self.create_set_frame, text='Réponse:').pack(padx=5, pady=5)
        self.definition_entry = ttk.Entry(self.create_set_frame, textvariable= answer, width=30)
        self.definition_entry.pack(padx=5, pady=5)

        ttk.Button(self.create_set_frame, text='Ajouter une carte', command=self.add_flashcard).pack(padx=5, pady=10)

        self.added_card = ttk.Label(self.create_set_frame, text='')
        self.added_card.pack(padx=5, pady=5)

        ttk.Button(self.create_set_frame, text='Sauvegarder', command=self.save_flashcards).pack(padx=5, pady=10)

        self.select_set_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.select_set_frame, text='Sélectionner une pile')

        self.sets_var = tk.StringVar()
        self.levels_var = tk.StringVar()

        self.sets_combobox = ttk.Combobox(self.select_set_frame, state='readonly', textvariable=self.sets_var)
        self.sets_combobox['values'] = self.load_json_files()
        self.sets_combobox.pack(padx=5, pady=5)

        self.sets_combobox = ttk.Combobox(self.select_set_frame, state='readonly', textvariable=self.levels_var)
        self.sets_combobox['values'] = ['1', '2', '3']
        self.sets_combobox.set('1')
        self.sets_combobox.pack(padx=5, pady=5)


        ttk.Button(self.select_set_frame, text='Sélectionner une pile', command=self.select_flashcards).pack(padx=5, pady=5)
        self.game_played = ttk.Label(self.select_set_frame, text='')
        
        self.flashcards_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.flashcards_frame, text='Jouer !')

        self.word_label = ttk.Label(self.flashcards_frame, text='', font=('TkDefaultFont', 24), wraplength=400)
        self.word_label.pack(padx=5, pady=40)

        self.definition_label = ttk.Label(self.flashcards_frame, text='')
        self.definition_label.pack(padx=5, pady=5)

        self.answer_var = tk.StringVar()
        ttk.Entry(self.flashcards_frame, textvariable=self.answer_var, width=30).pack(padx=5, pady=5)

        ttk.Button(self.flashcards_frame, text='Valider la réponse', command=self.validate_answer).pack(side='left', padx=5, pady=5)

        ttk.Button(self.flashcards_frame, text='Carte suivante', command=self.next_card).pack(side='right', padx=5, pady=5)

        self.load_flashcard()  


    def add_flashcard(self):
        question = self.word_entry.get()
        answer = self.definition_entry.get()
        if question == '' or answer == '':
            self.added_card.config(text='Veuillez entrer une question et une réponse')
        else:
            self.flashcard_game.add_flashcard(question, answer)
            self.word_entry.delete(0, 'end')
            self.definition_entry.delete(0, 'end')
            self.added_card.config(text='Carte ajoutée avec succès !')
            self.master.after(1500, self.reset_success_message)


    def reset_success_message(self):
        self.added_card.config(text='')


    def load_json_files(self):
        json_files = [f for f in os.listdir() if f.endswith('.json')]
        self.sets_combobox['values'] = json_files
        self.sets_var.set(json_files[0])


    def save_flashcards(self):
        set_name = self.set_name_entry.get()
        self.flashcard_game.save_to_file(set_name + '.json')
        self.flashcard_game.stack.flashcards = []
        self.load_json_files()
        self.set_name_entry.delete(0, 'end')
        self.added_card.config(text='Pile sauvegardée avec succès !')
        self.master.after(1500, self.reset_success_message)


    def select_flashcards(self):
        print(len(self.flashcard_game.stack.flashcards))
        if len(self.flashcard_game.stack.flashcards) != 0:
            self.game_played.config(text='Une partie est déjà en cours')
            self.master.after(1500, self.reset_success_message)
        else:
            selected_file = self.sets_var.get()
            level = self.levels_var.get()
            self.flashcard_game.load_from_file(selected_file, level)
            self.load_flashcard()


    def load_flashcard(self):
        
        if self.flashcard_game.stack.flashcards != []:
            current_flashcard = self.flashcard_game.get_current_flashcard()
            self.definition_label.config(text='')
            self.word_label.config(text=current_flashcard.question)
            
        else:
            self.word_label.config(text='Aucune flashcard disponible')
            self.definition_label.config(text='veuillez charger une pile ou changer le niveau')

        
    def delete_flashcards(self):
        set_name = self.sets_combobox.get()


    def validate_answer(self):
        user_answer = self.answer_var.get()
        current_flashcard = self.flashcard_game.get_current_flashcard()
        if self.flashcard_game.stack.is_empty():
            self.definition_label.config(text='veuillez charger une pile ou changer le niveau')
            self.word_label.config(text='Aucune flashcard disponible')
        elif user_answer == '':
            self.definition_label.config(text='Veuillez entrer une réponse')
        
        else:
            if user_answer.lower() == current_flashcard.answer.lower():
                self.definition_label.config(text='Bonne réponse !')
                self.answer_var.set('')
                self.flashcard_game.stack.current_card_index += 1
                current_flashcard.level += 1  
                
            else:
                self.definition_label.config(text='Mauvaise réponse ! \n La bonne réponse est: ' + current_flashcard.answer)
                self.answer_var.set('')
                self.flashcard_game.stack.current_card_index += 1 
            

    def next_card(self):
        if self.flashcard_game.stack.is_empty():
            self.word_label.config(text='Aucune flashcard disponible')
            self.definition_label.config(text='veuillez charger une pile ou changer le niveau')

        elif self.definition_label.cget('text') == '':
            self.definition_label.config(text='Veuillez valider une réponse')

        elif self.flashcard_game.stack.current_card_index >= len(self.flashcard_game.stack.flashcards):
            self.word_label.config(text='Plus de cartes disponibles')
            self.definition_label.config(text='veuillez charger une nouvelle pile ou changer le niveau')
            self.flashcard_game.save_to_file(self.sets_var.get())
            

        else:
            self.load_flashcard()
            self.answer_var.set('')
            self.definition_label.config(text='')


