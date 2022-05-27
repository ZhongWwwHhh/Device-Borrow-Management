# needs opencv_python, pyzbar
import cv2,threading,tkinter,time,csv
from pyzbar.pyzbar import decode

testtestdict = {}
stopcontrol = 'continue'

def decode(waittime=0):
    capture = cv2.VideoCapture(0)
    
    while True:
        ret,frame = capture.read()

        if ret == True:
            barcode = decode(frame, symbols=None)

            for content in barcode:
                codedata = content.data.decode('utf-8')
                codetype = content.type
                printout = '{} ({})'.format(codedata, codetype)
                return(codedata)
                break

        else:
            print('read capture fail')
        time.sleep_ms(waittime)