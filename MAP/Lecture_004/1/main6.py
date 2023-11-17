from kivy.lang import Builder
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        return Builder.load_file('main6.kv')

if __name__ == '__main__':
    MyApp().run()
