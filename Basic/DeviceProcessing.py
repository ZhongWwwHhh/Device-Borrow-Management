
import pickle


def readFile(fileAddress):
    with open(fileAddress, 'rb') as fileList:
        deviceList = pickle.load(fileList)
    return(deviceList)

def writeFile(fileAddress, deviceList):
    with open(fileAddress, 'wb') as fileList:
        pickle.dump(deviceList, fileList)

def changeDeviceStatus(deviceUid, deviceList, newStatus):
    deviceList[deviceUid] = newStatus
    return(deviceList)

def searchDevice(deviceUid, deviceList):
    if deviceUid in deviceList:
        return(True)
    else:
        return(False)