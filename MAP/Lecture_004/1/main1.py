from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        label = Label(
            text="Custom Text Style",
            font_size='20sp',  # Corrected quotation mark
            font_name='Calibri',
            color=(1, 0, 0, 1),
            bold=True,
            italic=True,
            underline=True
        )
        self.add_widget(label)

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
