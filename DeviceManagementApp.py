from kivy.core.text import LabelBase
LabelBase.register(name='msyh',fn_regular='chinese.msyh.ttf')

import kivy

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class MainMenu(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'


class DeviceManagementApp(App):

    def build(self):
        return MainMenu()


if __name__ == '__main__':
    DeviceManagementApp().run()