from kivymd.app import MDApp
from kivymd.uix.screenmanager import Screen, screenmanager
from kivy.lang import builder


class SaadApp(MDApp):
        def build(self):
            LaunchScreen = Screen()
            return LaunchScreen
SaadApp().run()