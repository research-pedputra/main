from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Load the kv file explicitly
Builder.load_file('myboxlayout.kv')

class MyBoxLayout(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
