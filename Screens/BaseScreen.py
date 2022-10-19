from kivy.uix.screenmanager import Screen


class BaseScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_touch_move(self, touch):
        # in case of left to right slide Menu screen will be displayed
        if touch.dx > 10:
            self.manager.transition.direction = 'right'
            self.manager.current = 'menu'
