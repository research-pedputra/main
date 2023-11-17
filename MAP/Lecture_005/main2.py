from kivy.lang import Builder
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Set the theme to Dark
        return Builder.load_file('bkg.kv')

if __name__ == '__main__':
    MyApp().run()
