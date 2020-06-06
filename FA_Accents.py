from FA_LanguageSelect import get_active_language
from FA_LanguageSelect import Language

from tkinter import *

french_accents = [['à','â','æ','ç'],['é','è','ê','ë'],['ï','î','ô','œ'],['ù','û','ü','ÿ']]
german_accents = [['ä','ö','ü','ß']]
spanish_accents = [['á','é','í','ñ'], ['ó','ú','ü']]

def get_accents():
    language = get_active_language()
    if language is Language.French:
        return french_accents
    if language is Language.German:
        return german_accents
    if language is Language.Spanish:
        return spanish_accents

class FA_Accents:
    def __init__(self, root):
        accents = get_accents()
        self.button_frame = Frame(root.frame_control, padx=5, pady=5)
        self.button_frame.grid(column=0, row=3, columnspan=2, rowspan=len(accents), sticky='W')
        self.buttons_accents = []
        for i in range(len(accents)):
            for j in range(len(accents[i])):
                self.buttons_accents.append(self.create_button(root, accents[i][j], j, i))

    def create_button(self, root, character, x, y):
        button = Button(self.button_frame, text=character, command= lambda: self.type_character(root, character))
        button.grid(column=x, row=y)

    @staticmethod
    def type_character(root, character):
        root.text_source.insert(END, character)
