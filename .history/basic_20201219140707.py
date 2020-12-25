from kivymd.app import MDApp
from kivymd.uix.screen import Screen


class SaadApp(MDApp):
        def build(self):
            screen = Screen()
            return screen
SaadApp().run()