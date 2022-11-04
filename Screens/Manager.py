from kivy.uix.screenmanager import ScreenManager
from Screens import Menu, LearnWords, AddWords, DeleteWords, BaseScreen


class Manager(ScreenManager):
    def __init__(self):
        super(Manager, self).__init__()

        # register all screens
        self.add_widget(Menu.MenuScreen(name='menu'))
        self.add_widget(LearnWords.WordsScreen(name='learnWords'))
        self.add_widget(LearnWords.WordsScreen2(name='learnWords2'))
        self.add_widget(AddWords.AddWords(name='addWords'))
        self.add_widget(DeleteWords.DeleteWords(name='delWords'))
        self.add_widget(BaseScreen.BaseScreen(name='base'))
