from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior

class ColorChangingLabel(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(ColorChangingLabel, self).__init__(**kwargs)
        self.original_color = self.color  # Store the original color

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.color = (0, 1, 0, 1)  # Green color
        return super(ColorChangingLabel, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.color = self.original_color
        return super(ColorChangingLabel, self).on_touch_up(touch)

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        # First Label
        label1 = ColorChangingLabel(
            text="Label 1: Touch me!",
            font_size='16sp',
            color=(0, 0, 1, 1),  # Blue color
            bold=True,
            italic=False,
            underline=True)
        self.add_widget(label1)

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
