class Translation:
    def __init__(self, en, fr, dt):
        self.english = en
        self.french = fr
        self.datetime = dt

    def __eq__(self, other):
        return self.french == other.french

    def __ne__(self, other):
        return self.french != other.french
