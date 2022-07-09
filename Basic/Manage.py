
from kivy.uix.screenmanager import Screen
import Basic.GuiControl as GuiControl
from kivy.lang import Builder
import Basic.DeviceProcessing as DeviceProcessing


Builder.load_file('Basic/manage.kv')
deviceList = ''

class ManageScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        global deviceList
        self.ids.devicestatusbtn.text = deviceList
    
    def update(self):
        global deviceList
        deviceList = DeviceProcessing.readFile('Configure/deviceList')
        deviceList = str(deviceList)
        self.ids.devicestatusbtn.text = deviceList

    def cancel(self):
        global screenManager
        GuiControl.changeScreen(screenManager, currentScreen = 'scMainMenu')


class Manage():
    def showDeviceStatus():
        # change screen
        scManage = ManageScreen(name  = 'scManage')
        global screenManager
        GuiControl.changeScreen(screenManager, scManage, 'scManage')

    def getSM(mainScreenManager):
        global screenManager
        screenManager = mainScreenManager
