import random

from googletrans import Translator
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
import json

from kivy.core.window import Window

Window.size = (480, 800)

x = {
    "see": ["бачити", "see saw seen"],
    "hear": ["чути", "hear heard heard"],
    "touch": ["торкатися", ""],
    "smell": ["нюхати", "smell smelt smelt"]
}

Json_example = json.dumps(x)

translator = Translator()


class Manager(ScreenManager):
    def __init__(self):
        super(Manager, self).__init__()
        self.add_widget(MenuScreen(name='menu'))
        self.add_widget(WordsScreen(name='learnWords'))
        self.add_widget(IrregularVerbsScreen(name='irregularV'))


class MenuScreen(Screen):
    name = 'menu'
    button_name = 'Learn words'


class WordsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'learnWords'
        words_list = random.sample(list(x.keys()), k=4)

        self.choice_button1_text = words_list[0]
        self.choice_button2_text = words_list[1]
        self.choice_button3_text = words_list[2]
        self.choice_button4_text = words_list[3]

        self.correct_word = random.choice(words_list)

        self.label_text = translator.translate(self.correct_word, dest="uk").text

    def is_correct_answer(self, instance):
        if instance.text == self.correct_word:
            instance.text_color = 'green'
            instance.line_color = 'green'
            print(self)
        else:
            instance.text_color = 'red'
            instance.line_color = 'red'



class IrregularVerbsScreen(Screen):
    pass


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        screen = Builder.load_file('layout.kv')
        return screen


DemoApp().run()
