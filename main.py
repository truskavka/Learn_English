from kivymd.app import MDApp
from kivy.lang.builder import Builder

from Screens import Manager, Menu, LearnWords


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        screen = Builder.load_file('layout.kv')
        return screen


DemoApp().run()
