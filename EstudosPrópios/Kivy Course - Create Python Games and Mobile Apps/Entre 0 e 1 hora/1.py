from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="Jojo 1 ")
    #     b2 = Button(text="Jojo 2 ")
    #     b3 = Button(text="Jojo 3 ")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)


class MainWidget(Widget): # Interface principal
    pass


class TheLabApp(App):
    pass

TheLabApp().run()