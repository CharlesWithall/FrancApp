import tkinter as tk
import tkinter.font as tkfont

class WordsearchGameOverWindow:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(root.main_window)
        self.window.wm_title("You Win!")
        self.window.grab_set()

        font = tkfont.Font(family="Helvetica", size=14)
        self.button_new_game = tk.Button(self.window, text="New Game", font=font, command=self.regenerate)
        self.button_exit = tk.Button(self.window, text="Exit", font=font, command=self.exit)

        self.button_new_game.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_exit.pack(side=tk.RIGHT, padx=5, pady=5)

    def regenerate(self):
        self.exit()
        self.root.generate_wordsearch()

    def exit(self):
        self.window.destroy()
        self.root.wordsearch_window.window.destroy()

