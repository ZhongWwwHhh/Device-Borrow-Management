from kivy.app import App
from kivy.lang import Builder


root = Builder.load_file('MainGui.kv')

class MainApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    MainApp().run()