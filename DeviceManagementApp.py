from kivy.core.text import LabelBase
LabelBase.register(name='msyh',fn_regular='chinese.msyh.ttf')

import kivy

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class MainMenu(FloatLayout):
    pass


class DeviceManagementApp(App):

    def build(self):
        return MainMenu()


if __name__ == '__main__':
    DeviceManagementApp().run()