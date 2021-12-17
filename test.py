from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('layout.kv')


class MyLayout(FloatLayout):
    pass


class TestApp(App):
    def build(self):
        return MyLayout()


TestApp().run()


