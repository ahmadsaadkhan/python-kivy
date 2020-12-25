from kivymd.app import MDApp
from kivymd.uix.screen import Screen


class SaadApp(MDApp):
        def build(self):
            LaunchScreen = Screen()
            return LaunchScreen
SaadApp().run()