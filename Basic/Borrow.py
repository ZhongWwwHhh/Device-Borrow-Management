# when borrow
# import def for capture

import pickle
from unicodedata import name
from kivy.uix.screenmanager import Screen
from Basic.ImageProcessing import ImageProcessing
from kivy.lang import Builder

import cv2

Builder.load_file('Basic/borrow.kv')

class Borrow(Screen):
    pass

class BorrowProcessing():

    # main processing
    def borrowStart(self, screenManager):

        # change screen
        from Basic.GuiControl import changeScreen
        scBorrow = Borrow(name  = 'scBorrow')
        changeScreen(screenManager, scBorrow, 'scBorrow')

        # start borrow process
        print('borrow started')
        
        # define a capture for ImageProcessing.takeCapture()
        capture = cv2.VideoCapture(0)
        
        # take picture, decode and prevent mistake
        lastResult = None
        sameResultNum = 0
        while True:
            frame = ImageProcessing.takeCapture(self, capture)
            result = ImageProcessing.deCode(self, frame)
            if result:
                if result == lastResult:
                    sameResultNum += 1
                    if sameResultNum >= 3:
                        break
                else:
                    lastResult = result
                    sameResultNum = 1

        print('result:', result)

        # search information and change state
        result = str(result)
        
        import Basic.DeviceProcessing as DeviceProcessing

        deviceList = DeviceProcessing.readFile('Configure/deviceList')

        if DeviceProcessing.searchDevice(result, deviceList):
            deviceList = DeviceProcessing.changeDeviceStatus(result, deviceList, 0)
            DeviceProcessing.writeFile('Configure/deviceList', deviceList)
            print('yes')
        else:
            print('no')
        

        print('asdfghjkl')

        

