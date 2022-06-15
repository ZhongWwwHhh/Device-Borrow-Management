# when borrow
# import def for capture
from Basic.ImageProcessing import ImageProcessing

class Borrow:
    
    def __init__(self):
        pass
    
    # main processing
    def borrowStart(self):
        # start borrow process
        print('borrow started')

        result = ImageProcessing.deQrCode()
        print('result:{}'.format(result))
