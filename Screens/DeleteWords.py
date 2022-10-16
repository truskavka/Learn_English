from Screens.BaseScreen import BaseScreen
from .LearnWords import Words


class DeleteWords(BaseScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'delWords'
        self.word = str()

    def delete_word(self):
        self.word = self.ids.txt0.text

        if Words.delete_word(word_to_delete=self.word) == -1:
            self.ids.txt0.hint_text = 'Such words is not in dictionary'
            self.ids.txt0.text = ''

    @staticmethod
    def delete_all_words():
        Words.clear_dict()
