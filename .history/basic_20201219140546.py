from kivymd.app import MDApp
from kivymd.uix.screen import Screen


class SaadApp(MDApp):
        def build(self):
            Screen = Screen()
            return Screen
SaadApp().run()