import random

from Screens.BaseScreen import BaseScreen
from db.words import Words

Words = Words()


class WordsScreen(BaseScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'learnWords'
        self.is_answer_chosen = False

        self.words_list = Words.get_random_words(quantity=4)

        self.choice_button1_text = self.words_list[0]
        self.choice_button2_text = self.words_list[1]
        self.choice_button3_text = self.words_list[2]
        self.choice_button4_text = self.words_list[3]

        self.correct_word = random.choice(self.words_list)

        self.label_text = Words.get_translation(self.correct_word)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        if self.is_answer_chosen:
            # in case of right to left slide next test will be displayed
            if touch.dx < 0:
                self.move_to_next_screen()

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
        self.words_list = Words.get_random_words(quantity=4)

        for i in range(4):
            self.ids['btn' + str(i)].text = self.words_list[i]
            self.ids['btn' + str(i)].text_color = 'orange'
            self.ids['btn' + str(i)].line_color = 'orange'

        self.correct_word = random.choice(self.words_list)
        self.ids['lbl0'].text = Words.get_translation(self.correct_word)


class WordsScreen2(WordsScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = 'learnWords2'

    def move_to_next_screen(self, *args):
        self.manager.get_screen('learnWords').refresh()
        self.manager.transition.direction = 'left'
        self.manager.current = 'learnWords'
