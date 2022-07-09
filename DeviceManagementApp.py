
from kivy.core.text import LabelBase
# define chinese when display
LabelBase.register(name='msyh',fn_regular='chinese.msyh.ttf')

# from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

import Basic.GuiControl as GuiControl

screenManager = ScreenManager()

firstRun = True
firstManage = True

# define main screen with three buttons
class MainMenu(Screen):

    def releaseBorrowBtn(self, arg):
        from Basic.Borrow import BorrowProcessing
        BorrowProcessing.getSM(screenManager)
        BorrowProcessing.getNewStatus(0)
        global firstRun
        if firstRun:
            BorrowProcessing.borrowStart(self)
            firstRun = False
        else:
            GuiControl.changeScreen(screenManager, currentScreen = 'scBorrow')
    
    def releaseReturnBtn(self, arg):
        from Basic.Borrow import BorrowProcessing
        BorrowProcessing.getSM(screenManager)
        BorrowProcessing.getNewStatus(1)
        global firstRun
        if firstRun:
            BorrowProcessing.borrowStart(self)
            firstRun = False
        else:
            GuiControl.changeScreen(screenManager, currentScreen = 'scBorrow')

    
    def releaseManageBtn(self, arg):
        global firstManage
        from Basic.Manage import Manage
        Manage.getSM(screenManager)
        Manage.showDeviceStatus(firstManage)    


# main App
class DeviceManagementApp(App):

    def build(self):
        scMainMenu = MainMenu(name = 'scMainMenu')
        screenManager.add_widget(scMainMenu)
        return screenManager


if __name__ == '__main__':
    DeviceManagementApp().run()