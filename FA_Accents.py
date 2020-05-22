from tkinter import *

accents = [['à','â','æ','ç'],['é','è','ê','ë'],['ï','î','ô','œ'],['ù','û','ü','ÿ']]

class FA_Accents:
    def __init__(self, root):
        self.button_frame = Frame(root.frame_main, padx=5, pady=5)
        self.button_frame.grid(column=0, row=3, columnspan=2, sticky='W')
        self.buttons_accents = []
        for i in range(len(accents)):
            for j in range(len(accents[i])):
                self.buttons_accents.append(self.create_button(root, accents[i][j], j, i))

    def create_button(self, root, character, x, y):
        button = Button(self.button_frame, text=character, command= lambda: self.type_character(root, character))
        button.grid(column=x, row=y)

    def type_character(self, root, character):
        root.text_source.insert(END, character)
