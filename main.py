from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MenuScreen(Screen):
    pass


class WordsScreen(Screen):
    pass


class IrregularVerbsScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(WordsScreen(name='learnWords'))
sm.add_widget(IrregularVerbsScreen(name='irregularV'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_file('layout.kv')
        return screen


DemoApp().run()

