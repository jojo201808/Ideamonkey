import  os
import  time
import logging
import threading
import subprocess

class Ideamonkey():
    def __init__(self):
        self.devicelist = []
        self.devicemodels = []
        self.execfiles = []
        self.logfiles = []

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
        #对每个手机创建文件夹和monkey执行脚本
        for i,d in enumerate(self.devicemodels):
            devdir = os.path.exists("E:\\monkey_test\\"+d)
            if devdir:
                print(d,'手机文件夹已经创建')
            else:
                os.mkdir("E:\\monkey_test\\"+d)
            #创建要执行的monkey脚本
            seed,rtime = self.get_time()
            monkey_src = "adb -s %s shell monkey -p com.alashow.live -s %s \
            --pct-touch 70 --pct-motion 30 --ignore-crashes --ignore-timeouts \
            --monitor-native-crashes --throttle 200 -v -v 500000 2>&1 &" \
            % (self.devicelist[i],seed)
            filedir = "E:\\monkey_test\\"+d+"\\"+ d + ".txt"
            logdir = "E:\\monkey_test\\"+d+"\\" + d + rtime + ".log"
            with open(filedir,'w') as f:
                f.write(monkey_src)
            self.execfiles.append(filedir)
            self.logfiles.append(logdir)
    
    #执行脚本输出
    def exec_monkey(self,fi,flog):
        print("run " + fi)
        with open(fi,'r') as f:
            src = f.read()
        #child = subprocess.Popen(src,stdout=subprocess.PIPE)
        #data = child.communicate()
        data = os.popen(src).read()
        with open(flog,'w') as f:
            #f.write(data[0].decode('utf-8'))
            f.write(data)

    
    #多线程调用执行脚本
    def multithread(self):
        for i,d in enumerate(self.execfiles):
            t = threading.Thread(target=self.exec_monkey, args=(d,self.logfiles[i]))
            t.start()
        t.join()
      
            


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
    t.multithread()
    print("测试完成，请查看日志")