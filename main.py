import random

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
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


# def get_list_of_keys(list_of_dicts):
#     list_of_keys = list()
#     for i in list_of_dicts:
#         list_of_keys.append(i)
#     print(list_of_keys)
#     return list_of_keys


class MenuScreen(Screen):
    name = 'menu'
    button_name = 'Learn words'


class WordsScreen(Screen):
    name = 'learnWords'
    buttons_text = []

    words_list = random.sample(list(x.keys()), k=4)

    choice_button1_text = words_list[0]
    choice_button2_text = words_list[1]
    choice_button3_text = words_list[2]
    choice_button4_text = words_list[3]

    label_text = random.choice(words_list)


class IrregularVerbsScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(WordsScreen(name='learnWords'))
sm.add_widget(IrregularVerbsScreen(name='irregularV'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        screen = Builder.load_file('layout.kv')
        return screen


DemoApp().run()
