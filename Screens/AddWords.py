from Screens.BaseScreen import BaseScreen
from .LearnWords import Words


class AddWords(BaseScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'addWords'
        self.word = str()
        self.translation = str()

    def add_word_to_dict(self):
        self.word = self.ids.txt0.text
        self.translation = self.ids.txt1.text

        if self.word and self.translation:
            print(self.word, self.translation)
            Words.add_word(word_to_add=self.word, translation_of_word_to_add=self.translation)
