from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

#builder string
helper_string = '''
ScreenManager:
    Home:

<Home>:
    name: 'home'
    MDLabel:
        text: 'Saads App'
        halign: 'center'
        theme_text_color: 'custom'
        text_color: 148/255,0,211/255,1


'''

class Home(Screen):
    pass
sm = ScreenManager()
sm.add_widget(Home(name = 'hello there'))


class SaadApp(MDApp):
        def build(self):
            LaunchScreen = Screen()
            help_str = Builder.load_string(helper_string)

            LaunchScreen.add_widget(help_str)
            return LaunchScreen
SaadApp().run()