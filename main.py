import random

from googletrans import Translator
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json

from kivy.core.window import Window

Window.size = (480, 800)


with open('words.json', 'r') as openfile:
    json_words = json.load(openfile)


translator = Translator()


class Manager(ScreenManager):
    def __init__(self):
        super(Manager, self).__init__()
        self.add_widget(MenuScreen(name='menu'))
        self.add_widget(WordsScreen(name='learnWords'))


class MenuScreen(Screen):
    name = 'menu'
    button_name = 'Learn words'


class WordsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'learnWords'
        self.label2_text = self.name
        self.is_answer_chosen = False

        self.words_list = random.sample(list(json_words), k=4)

        self.choice_button1_text = self.words_list[0]
        self.choice_button2_text = self.words_list[1]
        self.choice_button3_text = self.words_list[2]
        self.choice_button4_text = self.words_list[3]

        self.correct_word = random.choice(self.words_list)

        self.label_text = json_words[self.correct_word]

    def on_touch_move(self, touch):
        if self.is_answer_chosen:
            if touch.dx < 0:
                self.move_to_next_screen()
            elif touch.dx > 0:
                self.manager.transition.direction = 'right'
                self.manager.current = 'menu'

    def is_correct_answer(self, instance):
        if instance.text == self.correct_word:
            instance.text_color = 'green'
            instance.line_color = 'green'
        else:
            instance.text_color = 'red'
            instance.line_color = 'red'
            self.ids['btn' + str(self.words_list.index(self.correct_word))].text_color = 'green'
            self.ids['btn' + str(self.words_list.index(self.correct_word))].line_color = 'green'
        self.is_answer_chosen = True

    def move_to_next_screen(self, *args):
        self.manager.get_screen('learnWords2').refresh()
        self.manager.transition.direction = 'left'
        self.manager.current = 'learnWords2'

    def refresh(self):
        self.is_answer_chosen = False
        self.words_list = random.sample(list(json_words), k=4)

        for i in range(4):
            self.ids['btn' + str(i)].text = self.words_list[i]
            self.ids['btn' + str(i)].text_color = 'orange'
            self.ids['btn' + str(i)].line_color = 'orange'

        self.correct_word = random.choice(self.words_list)
        self.ids['lbl0'].text = json_words[self.correct_word]


class WordsScreen2(WordsScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.clear_widgets()
        self.name = 'learnWords2'
        self.label2_text = self.name

    def move_to_next_screen(self, *args):
        self.manager.get_screen('learnWords').refresh()
        self.manager.transition.direction = 'left'
        self.manager.current = 'learnWords'


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        screen = Builder.load_file('layout.kv')
        return screen


DemoApp().run()
