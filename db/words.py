from kivy.storage.jsonstore import JsonStore
from pathlib import Path
from random import sample


def singleton(class_):
    """"simple decorator to realize singleton pattern"""
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Words:
    def __init__(self):
        p = Path(__file__).with_name('words.json')
        self.json_words = JsonStore(p)

    def get_random_words(self, quantity):
        if self.json_words.count() >= 4:
            return sample(list(self.json_words), k=quantity)
        else:
            return []

    def get_translation(self, word_to_translate):
        return self.json_words[word_to_translate]['ua']

    def add_word(self, word_to_add: str, translation_of_word_to_add: str):
        self.json_words.put(word_to_add, ua=translation_of_word_to_add)

    def delete_word(self, word_to_delete):
        if word_to_delete in self.json_words.keys():
            self.json_words.delete(word_to_delete)
        else:
            return -1

    def clear_dict(self):
        self.json_words.clear()

    def is_empty(self):
        return self.json_words.count() == 0
