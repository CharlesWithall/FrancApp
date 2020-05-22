from googletrans import Translator

class FA_Translator:
    def __init__(self):
        self.translator = Translator()

    def translate_from_french(self, text):
        return self.translator.translate(text, src='fr', dest='en')

    def translate_to_french(self, text):
        return self.translator.translate(text, src='en', dest='fr')
