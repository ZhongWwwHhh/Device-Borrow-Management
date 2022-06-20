# needs opencv_python, pyzbar
import cv2
from pyzbar.pyzbar import decode

class ImageProcessing:
    
    def __init__(self):
        pass
    
    # take one picture. require define capture 
    def takeCapture(self, capture):       
        ret, frame = capture.read()
        if ret:
            # return data of picture
            return(frame)
        else:
            pass
    
    # decode in one picture
    def deCode(self,frame):
        rawCodes = decode(frame, symbols=None)
        if rawCodes:
            for codeContent in rawCodes:
                codeData = codeContent.data.decode('utf-8')
                codeType = codeContent.type
                print('success type {} data {}'.format(codeType, codeData))
                return(codeData)
        else:
            return(None)
