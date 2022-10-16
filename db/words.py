import json
from pathlib import Path
from random import sample


class Words:
    json_words: dict

    def __init__(self):
        p = Path(__file__).with_name('words.json')
        with p.open('r') as openfile:
            self.json_words = json.load(openfile)

    def get_random_words(self, quantity):
        return sample(list(self.json_words), k=quantity)

    def get_translation(self, word_to_translate):
        return self.json_words[word_to_translate]

    def add_word(self, word_to_add: str, translation_of_word_to_add: str):
        if word_to_add not in self.json_words:
            self.json_words.update({word_to_add: translation_of_word_to_add})
        else:
            self.json_words[word_to_add] = translation_of_word_to_add
        self.commit()

    def delete_word(self, word_to_delete):
        if word_to_delete in self.json_words:
            self.json_words.pop(word_to_delete)
            self.commit()
        elif word_to_delete in list(self.json_words.values()):
            self.reformat()
            self.json_words.pop(word_to_delete)
            self.reformat()
        else:
            return -1

    def clear_dict(self):
        self.json_words.clear()
        self.commit()

    def commit(self):
        p = Path(__file__).with_name('words.json')
        with p.open('w', encoding='utf-8') as openfile:
            json.dump(self.json_words, openfile, indent=4)

    def reformat(self):
        """simple function that changes keys with values"""
        self.json_words = {y: x for x, y in self.json_words.items()}