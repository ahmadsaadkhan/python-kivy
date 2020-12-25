from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

#builder string
helper_string = '''
ScreenManager:
    hello:

<hello>:
    name: 'hello'
    MDLabel:
        text: 'Saads App'


'''

class hello(Screen):
    pass
sm = ScreenManager()
sm.add_widget(hello(name = 'hello there'))


class SaadApp(MDApp):
        def build(self):
            LaunchScreen = Screen()
            help_str = Builder.load_string(helper_string)

            LaunchScreen.add_widget(help_str)
            return LaunchScreen
SaadApp().run()