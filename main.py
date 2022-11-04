from kivymd.app import MDApp
from kivy.lang.builder import Builder

# importing screens so then
# builder was able to use them to link front and back end
from Screens import Manager, Menu, LearnWords


class DemoApp(MDApp):

    def build(self):
        #  set themes
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        # load kivy file with markup
        screen = Builder.load_file('layout.kv')
        return screen


DemoApp().run()
