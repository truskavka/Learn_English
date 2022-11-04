from Screens.BaseScreen import BaseScreen
from db import words

Words = words.Words()


class DeleteWords(BaseScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'delWords'
        self.word = str()

    def delete_word(self):
        # gets word from label
        self.word = self.ids.txt0.text

        if Words.delete_word(word_to_delete=self.word) == -1:
            self.ids.txt0.hint_text = 'Such words is not in dictionary'
            self.ids.txt0.text = ''
        else:
            self.ids.txt0.hint_text = f'Word "{self.word}" was deleted'
            self.ids.txt0.text = ''

    def delete_all_words(self):
        Words.clear_dict()
        self.ids.txt0.hint_text = 'All words were deleted from dictionary'
