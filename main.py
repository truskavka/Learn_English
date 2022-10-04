from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json

from kivy.core.window import Window

Window.size = (480, 800)


x = {
  "see": ["бачити", "see saw seen"]
}

Json_example = json.dumps(x)


class MenuScreen(Screen):
    pass


class WordsScreen(Screen):
    name = 'learnWords'


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

