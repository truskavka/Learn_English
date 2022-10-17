from Screens.BaseScreen import BaseScreen
from db import words

Words = words.Words()


class AddWords(BaseScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'addWords'
        self.word = str()
        self.translation = str()

    def add_word_to_dict(self):
        self.word = self.ids.txt0.text
        self.translation = self.ids.txt1.text

        if (len(self.word) or len(self.translation)) < 0:
            self.ids.txt0.text = 'One of words is too short'
        elif (len(self.word) or len(self.translation)) >= 15:
            self.ids.txt0.text = 'One of words is too long'
        else:
            print(self.word, self.translation)
            Words.add_word(word_to_add=self.word, translation_of_word_to_add=self.translation)
            self.ids.txt0.text = self.ids.txt1.text = ''
            self.ids.txt0.hint_text = 'Word was added to dictionary'
            self.ids.txt1.hint_text = 'Translation was added to dictionary'
