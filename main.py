# needs opencv_python, pyzbar
from ast import While
from cgi import test
import cv2,threading,tkinter,time,csv
from pyzbar.pyzbar import decode

# take one picture
def Capture():
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    if ret == True:
        return(frame)
    else:
        #loglog
        print()

# indentify code and return content of it
def DeQrCode():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if ret:
            rawCodes = decode(frame, symbols=None)
            for codeContent in rawCodes:
                codeData = codeContent.data.decode('utf-8')
                codeType = codeContent.type
                print('success type {} data {}'.format(codeType, codeData))
                return(codeData)
    #need improve
'''
    cv2.imshow('Capture',frame)
    if cv2.waitKey(1) == ord('q'):
        break
'''

test = Capture()
print(test)
test2 = DeQrCode()
print(test2)