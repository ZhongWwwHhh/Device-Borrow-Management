# when borrow
# import def for capture
from Basic.ImageProcessing import ImageProcessing

import cv2

class Borrow:
    
    def __init__(self):
        pass
    
    # main processing
    def borrowStart(self):
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

        
        
        print('result:{}'.format(result))
