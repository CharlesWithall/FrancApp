from FA_Accents import FA_Accents as Accents
from FA_Save import load_saved_entries
from FA_Save import save_new_entry
from FA_Translation import Translation
from FA_Translator import FA_Translator as Translator
from FA_WordList import WordList

from Wordsearch.FA_Wordsearch_Window import Wordsearch_Window

from tkinter import *

from datetime import date
from enum import Enum

class TranslateDirection(Enum):
    FrenchToEnglish = 0
    EnglishToFrench = 1

class MainWindow:
    def __init__(self, root):
        # region HEADER
        self.main_window = root
        self.translator = Translator()
        self.saved_translations = load_saved_entries()
        self.wordsearch_window = Wordsearch_Window()

        root.title("FrancApp - Come up with a better name")
        root.iconbitmap("french_flag.ico")
        # endregion
        # region VARIABLES
        self.translate_direction = TranslateDirection.FrenchToEnglish
        self.string_source_label = StringVar()
        self.string_target_label = StringVar()
        self.string_source_label.set("Français:")
        self.string_target_label.set("English:")
        self.string_source_text = StringVar()
        # endregion

        # region WIDGET DECLARATIONS
        self.frame_main = Frame(root)
        self.label_source = Label(self.frame_main, textvariable=self.string_source_label)
        self.label_target = Label(self.frame_main, textvariable=self.string_target_label)
        self.text_source = Entry(self.frame_main, textvariable=self.string_source_text)
        self.text_source.bind("<Return>", self.translate)
        self.text_target = Entry(self.frame_main, state="readonly")
        self.button_translate = Button(self.frame_main, text="Translate", command=self.translate, state=DISABLED)
        self.button_save = Button(self.frame_main, text="Save", command=self.save, state=DISABLED)
        self.scale_direction = Scale(self.frame_main, from_=0, to=1, resolution=1, orient=HORIZONTAL, showvalue=0, command=self.set_direction)
        self.button_wordsearch = Button(self.frame_main, text="Word Search", command=self.generate_wordsearch)

        # endregion
        # region WIDGET ARRANGEMENTS
        self.label_source.grid(row=0, column=0)
        self.scale_direction.grid(row=0, column=1)
        self.label_target.grid(row=0, column=2)
        self.text_source.grid(row=1, column=0)
        self.text_target.grid(row=1, column=2)
        self.button_translate.grid(row=2, column=0)
        self.button_save.grid(row=2, column=2)
        self.button_wordsearch.grid(row=3, column=2)
        self.frame_main.grid(row=0, column=0, sticky="N")

        # endregion
        # region CALLBACKS
        self.string_source_text.trace_add("write", self.on_source_changed)
        self.text_source.focus_set()
        # endregion

        self.accents = Accents(self)
        self.word_list = WordList(root, self.saved_translations)

    def on_source_changed(self, *args):
        self.button_save.configure(state=DISABLED)
        if self.string_source_text.get() == "":
            self.button_translate.configure(state=DISABLED)
        else:
            self.button_translate.configure(state=NORMAL)

    def set_direction(self, value):
        self.translate_direction = TranslateDirection(int(value))

        swap = self.string_source_label.get()
        self.string_source_label.set(self.string_target_label.get())
        self.string_target_label.set(swap)

        swap = self.string_source_text.get()
        self.string_source_text.set(self.text_target.get())
        self.text_target.config(state="normal")
        self.text_target.delete(0, END)
        self.text_target.insert(0, swap)
        self.text_target.config(state="readonly")

        self.on_source_changed(None)

    def translate(self, event=None):
        if self.translate_direction is TranslateDirection.FrenchToEnglish:
            result = self.translator.translate_from_french(self.text_source.get())
        else:
            result = self.translator.translate_to_french(self.text_source.get())

        self.text_target.config(state="normal")
        self.text_target.delete(0, END)
        self.text_target.insert(0, result.text)
        self.text_target.config(state="readonly")
        self.button_save.configure(state=NORMAL)

    def save(self):
        if self.translate_direction is TranslateDirection.FrenchToEnglish:
            fr = self.text_source.get()
            en = self.text_target.get()
        else:
            en = self.text_source.get()
            fr = self.text_target.get()

        entry = Translation(en.title(), fr.title(), date.today().strftime("%d/%m/%Y"))
        if entry not in self.saved_translations:
            self.word_list.append_item(entry.english, entry.french, date.today())
            self.saved_translations.append(entry)
        save_new_entry(entry)

    def generate_wordsearch(self):
        self.wordsearch_window.launch(self)


# endregion

window_root = Tk()
main = MainWindow(window_root)
window_root.mainloop()