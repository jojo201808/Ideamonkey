import  os
import  time
import logging

class Ideamonkey():
    def __init__(self):
        self.devicelist = []
        self.devicemodels = []

#获得设备信息
    def get_devices(self):
        devicetmp = []
        rtd = os.popen('adb devices').readlines()
        # 获取手机设备号
        for d in rtd:
            devicetmp.append(d.split('\t')[0])
        self.devicelist = devicetmp[1:-1]
        print(self.devicelist)

        # 获取手机型号
        for m in range(len(self.devicelist)):
            # tmpmodel = os.popen('adb -s '+devicelist[m]+' shell getprop ro.product.model').readlines()[0].split('\n')[0]
            tmpmodel = os.popen('adb -s ' + self.devicelist[m] + ' shell getprop ro.product.model') \
                .readlines()[0].strip('\n').replace(' ','')
            self.devicemodels.append(tmpmodel)
        print(self.devicemodels)

#给不同的设备创建不同的文件夹以手机型号命名，存储于monkey_test
    def creatfolder(self):
        testdir = os.path.exists("E:\\monkey_test")
        if testdir:
            print('monkey_test文件夹已经存在')
        else:
            os.mkdir("E:\\monkey_test")
        #对每个手机创建文件夹和批处理脚本
        for i,d in enumerate(self.devicemodels):
            devdir = os.path.exists("E:\\monkey_test\\"+d)
            if devdir:
                print(d,'手机文件夹已经创建')
            else:
                os.mkdir("E:\\monkey_test\\"+d)
            #判断批处理文件是否存在，不在就创建一个
            filedir = "E:\\monkey_test\\"+d+"\\"+d+".bat"
            seed,rtime = self.get_time()
            monkey_src = "adb -s %s shell monkey -p com.alashow.live -s %s \
            --pct-touch 70 --pct-motion 30 --ignore-crashes --ignore-timeouts \
            --monitor-native-crashes --throttle 200 -v -v 500000 >E:\monkey_test\%s\monkey_%s_%s.txt" \
            % (self.devicelist[i],seed,d,d,rtime)
            with open(filedir,'w') as f:
                f.write(monkey_src)

    def get_time(self):
        timestruct = time.localtime(time.time())
        a = time.strftime('%Y-%m-%d %H:%M:%S', timestruct)
        b = time.strftime('%Y%m%d', timestruct)
        timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        return  timeStamp,b








if __name__ == '__main__':
    t = Ideamonkey()
    t.get_devices()
    t.creatfolder()