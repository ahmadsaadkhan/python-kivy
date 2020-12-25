from kivymd.app import MDApp
from kivymd.uix.screenmanager import Screen, screenmanager


class SaadApp(MDApp):
        def build(self):
            LaunchScreen = Screen()
            return LaunchScreen
SaadApp().run()