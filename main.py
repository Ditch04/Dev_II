
import argparse
from FlashCardGame import FlashCardGame
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


if __name__ == "__main__":
    game = FlashCardGame()
    game.play()
    game.end_game()

    root = tk.Tk()
    root.title('Flashcards App')
    root.geometry('500x400')

    style = Style(theme='superhero')
    style.configure('TLabel', font=('TkDefaultFont', 18))
    style.configure('TButton', font=('TkDefaultFont', 16))

    set_name_var = tk.StringVar()
    word_var = tk.StringVar()
    definition_var = tk.StringVar()
    answer_var = tk.StringVar()

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    create_set_frame = ttk.Frame(notebook)
    notebook.add(create_set_frame, text="Créer une pile")

    ttk.Label(create_set_frame, text="Définir le nom de la pile:").pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Question:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=word_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Réponse:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=definition_var, width=30).pack(padx=5, pady=5)

    ttk.Button(create_set_frame, text='Ajouter une carte').pack(padx=5, pady=10)

    ttk.Button(create_set_frame, text='Sauvegarder').pack(padx=5, pady=10)

    select_set_frame = ttk.Frame(notebook)
    notebook.add(select_set_frame, text='Sélectionner une pile')

    sets_combobox = ttk.Combobox(select_set_frame, state='readonly')
    sets_combobox.pack(padx=5, pady=5)

    ttk.Button(select_set_frame, text='Sélectionner une pile').pack(padx=5, pady=5)
    ttk.Button(select_set_frame, text='Supprimer une pile').pack(padx=5, pady=5)

    flashcards_frame = ttk.Frame(notebook)
    notebook.add(flashcards_frame, text='Jouer !')

    word_label = ttk.Label(flashcards_frame, text='', font=('TkDefaultFont', 24))
    word_label.pack(padx=5, pady=40)

    definition_label = ttk.Label(flashcards_frame, text='')
    definition_label.pack(padx=5, pady=5)

    ttk.Entry(flashcards_frame, textvariable=answer_var, width=30).pack(padx=5, pady=5)

    ttk.Button(flashcards_frame, text='Valider la réponse').pack(side='left', padx=5, pady=5)

    ttk.Button(flashcards_frame, text='Retourner la carte').pack(side='left', padx=5, pady=5)

    ttk.Button(flashcards_frame, text='Carte suivante').pack(side='right', padx=5, pady=5)

    root.mainloop()



