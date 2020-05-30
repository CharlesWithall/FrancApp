from FA_LanguageSelect import get_active_language_abbreviation_string

from googletrans import Translator

class FA_Translator:
    def __init__(self):
        self.translator = Translator()

    def translate_to_english(self, text):
        return self.translator.translate(text, src=get_active_language_abbreviation_string(), dest='en')

    def translate_from_english(self, text):
        return self.translator.translate(text, src='en', dest=get_active_language_abbreviation_string())
