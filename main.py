from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return MainWindow()


MainApp().run()
