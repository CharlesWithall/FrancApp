class Translation:
    def __init__(self, en, fr, dt):
        self.english = en
        self.foreign = fr
        self.datetime = dt

    def __eq__(self, other):
        return self.foreign == other.foreign

    def __ne__(self, other):
        return self.foreign != other.foreign
