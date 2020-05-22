from tkinter import *
from Wordsearch.FA_Wordsearch_Generator import FA_WordsearchGenerator as WordsearchGenerator

class Wordsearch_Window:
    def __init__(self):
        self.window = None
        self.frame_main = None
        self.wordsearch_generator = WordsearchGenerator()

    def launch(self, root):
        self.window = Toplevel(root.main_window)
        self.window.wm_title("Word Search")
        self.window.grab_set()

        self.frame_main = Frame(self.window)
        wordsearch = self.wordsearch_generator.generate()
        # send letters to grid here
        for i, line in enumerate(wordsearch):
            for j, character in enumerate(line):
                label = Label(self.frame_main, text=character)
                label.grid(row=i, column=j)

        self.frame_main.pack()
