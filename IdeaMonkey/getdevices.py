import logging
import os

def devicesinfo():
    devicetmp = []
    rtd = os.popen('adb devices').readlines()
    #获取手机设备号
    for d in rtd:
        devicetmp.append(d.split('\t')[0])
    devicelist = devicetmp[1:-1]
    print(devicelist)
    #获取手机型号
    devicemodel = []
    for m in range(0,len(devicelist)):
        #tmpmodel = os.popen('adb -s '+devicelist[m]+' shell getprop ro.product.model').readlines()[0].split('\n')[0]
        tmpmodel = os.popen('adb -s ' + devicelist[m] + ' shell getprop ro.product.model').readlines()[0].strip('\n')
        devicemodel.append(tmpmodel)
    print(devicemodel)



devicesinfo()






