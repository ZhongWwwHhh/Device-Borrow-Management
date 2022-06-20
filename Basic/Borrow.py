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
        
        while True:
            frame = ImageProcessing.takeCapture(self, capture)
            result = ImageProcessing.deCode(self, frame)
            if result:
                break
        
        
        print('result:{}'.format(result))
