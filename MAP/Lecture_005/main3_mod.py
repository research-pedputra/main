from kivy.lang import Builder 
from kivymd.app import MDApp

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('main3_mod.kv')
    def switch_theme_style(self):
        self.theme_cls.primary_palette = ("Orange" if self.theme_cls.primary_palette == "Red" else "Red")
        self.theme_cls.theme_style = ("Dark" if self.theme_cls.theme_style == "Light" else "Light")
Example().run()
