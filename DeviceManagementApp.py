from kivy.core.text import LabelBase
# define chinese when display
LabelBase.register(name='msyh',fn_regular='chinese.msyh.ttf')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen


class MainMenu(FloatLayout):

    def releaseBorrowBtn(self, arg):
        self.clear_widgets()
        from Basic.Borrow import Borrow
        Borrow.borrowStart(self)
    
    def releaseReturnBtn(self, arg):
        print('2')
    
    def releaseManageBtn(self, arg):
        print('3')

# main App
class DeviceManagementApp(App):

    def build(self):
        return MainMenu()


if __name__ == '__main__':
    DeviceManagementApp().run()