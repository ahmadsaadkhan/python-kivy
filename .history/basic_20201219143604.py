from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import builder

#builder string
helper_string = '''
Screenmanager:
    hello:

<hello>:
    name: 'hello'
    MDLabel:
        text: 'Saads App'


'''

class hello(Screen):
    pass
sm = screenmanager()
sm.add_widget(hello(name = 'hello'))


class SaadApp(MDApp):
        def build(self):
            LaunchScreen = Screen()
            help_str = builder.load_string(helper_string)

            LaunchScreen.add_widget(help_str)
            return LaunchScreen
SaadApp().run()