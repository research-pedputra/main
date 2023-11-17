from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        label = Label(
            text="Custom Text Style",
            font_size='20sp',
            font_name='Calibri',
            color=(1, 0, 0, 1),  # Red color
            bold=True,
            italic=True,
            underline=True,
            size_hint_y=None,
            height=50  # Adjust the height as needed
        )

        label2 = Label(
            text="Second Label",
            font_size='16sp',
            font_name='Arial',
            color=(0, 0, 1, 1),  # Blue color
            bold=False,
            italic=False,
            underline=False,
            size_hint_y=None,
            height=50,  # Adjust the height as needed
            pos_hint={'center_x': 0.5}  # Center the label horizontally
        )

        # Add the labels to the layout
        self.add_widget(label)
        self.add_widget(label2)

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
