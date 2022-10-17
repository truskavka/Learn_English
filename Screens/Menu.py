from kivy.uix.screenmanager import Screen


class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        self.name = 'menu'
        self.button1_name = 'Learn words'
        self.button2_name = 'Add words'
        self.button3_name = 'Delete words'

    def refresh_words_screen(self):
        self.manager.get_screen('learnWords').refresh()
