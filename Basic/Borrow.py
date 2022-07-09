# when borrow

import os
from kivy.uix.screenmanager import Screen
from Basic.GuiControl import changeScreen
import Basic.ImageProcessing as ImageProcessing
from kivy.lang import Builder

import cv2, threading, time

Builder.load_file('Basic/borrow.kv')



# GUI
class Borrow(Screen):

    # press button, decode then finish
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        
        # will improve
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        
        frame = cv2.imread("IMG_{}.png".format(timestr))
        os.remove("IMG_{}.png".format(timestr))
        #print(frame)

        result = ImageProcessing.deCode(frame)
        #print(result)
        
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
        
        global screenManager
        changeScreen(screenManager, currentScreen = 'scMainMenu')

class BorrowProcessing():

    # main processing
    def borrowStart(self):

        # change screen
        scBorrow = Borrow(name  = 'scBorrow')
        global screenManager
        changeScreen(screenManager, scBorrow, 'scBorrow')

        '''
        # will coming

        # define a capture for ImageProcessing.takeCapture()
        capture = cv2.VideoCapture(0)
        
        # take picture, decode and prevent mistake
        lastResult = None
        sameResultNum = 0
        while True:
            frame = ImageProcessing.takeCapture(capture)
            result = ImageProcessing.deCode(frame)
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
        '''
    
    # get screenManager
    def getSM(mainScreenManager):
        global screenManager
        screenManager = mainScreenManager
    

