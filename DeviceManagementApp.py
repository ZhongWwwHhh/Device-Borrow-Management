from unicodedata import name
from kivy.core.text import LabelBase
# define chinese when display
LabelBase.register(name='msyh',fn_regular='chinese.msyh.ttf')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

screenManager = ScreenManager()

# define main screen with three buttons
class MainMenu(Screen):

    def releaseBorrowBtn(self, arg):
        self.clear_widgets()
        from Basic.Borrow import Borrow, BorrowProcessing
        BorrowProcessing.borrowStart(self, screenManager)
    
    def releaseReturnBtn(self, arg):
        print('2')
    
    def releaseManageBtn(self, arg):
        print('3')

# main App
class DeviceManagementApp(App):

    def build(self):
        scMainMenu = MainMenu(name = 'scMainMenu')
        screenManager.add_widget(scMainMenu)
        return screenManager


if __name__ == '__main__':
    DeviceManagementApp().run()