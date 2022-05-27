# needs opencv_python, pyzbar
import cv2,threading,tkinter,time,csv
from pyzbar.pyzbar import decode

# indentify code and return content of it
def identifycode(waittime=0):
    capture = cv2.VideoCapture(0)
    while True:
        ret,frame = capture.read()
        if ret == True:
            barcode = decode(frame, symbols=None)
            for content in barcode:
                codedata = content.data.decode('utf-8')
                codetype = content.type
                print('success type {} data {}'.format(codetype, codedata))
                return(codedata)
        else:
            print('fail identifycode')
            break
        cv2.imshow('Capture',frame)
        if cv2.waitKey(1) == ord('q'):
            break
        time.sleep(waittime/1000)


ksksks = identifycode(0)
print(ksksks)