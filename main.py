from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

from Screens import Manager, Menu, LearnWords

Window.size = (480, 800)


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        screen = Builder.load_file('layout.kv')
        return screen


DemoApp().run()
