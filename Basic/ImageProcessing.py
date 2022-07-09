# needs pyzbar
from pyzbar.pyzbar import decode
    
# take one picture. require define capture 
def takeCapture(capture):       
    ret, frame = capture.read()
    if ret:
        # return data of picture
        return(frame)
    else:
        pass

# decode in one picture
def deCode(frame):
    rawCodes = decode(frame, symbols=None)
    if rawCodes:
        for codeContent in rawCodes:
            codeData = codeContent.data.decode('utf-8')
            codeType = codeContent.type
            #print('success type {} data {}'.format(codeType, codeData))
            return(codeData)
    else:
        return(None)