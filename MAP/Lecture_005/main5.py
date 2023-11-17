from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('main5.kv')

DemoApp().run()
