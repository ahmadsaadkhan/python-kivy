from kivymd.app import MDApp
from kivymd.uix.screenmanager import Screen, screenmanager
from kivy.lang import builder

#builder string
helper_string = '''
Screenmanager:
    hello:

<hello>:
    MDLabel:
        text: 'Saads App'


'''


class SaadApp(MDApp):
        def build(self):
            LaunchScreen = Screen()
            return LaunchScreen
SaadApp().run()