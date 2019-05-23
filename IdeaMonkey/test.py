#import  os
##os.system('CHCP 65001')
##data = os.popen(r'adb shell monkey -p com.alashow.live -s 20199 --pct-touch 70 --pct-motion 30 --ignore-crashes --ignore-timeouts --monitor-native-crashes --throttle 200 -v -v 50 >E:\logs\monkey0516.txt').readlines()
#c = 'adb shell monkey -p com.alashow.live -s 20199 --pct-touch 70 --pct-motion 30 --ignore-crashes --ignore-timeouts --monitor-native-crashes --throttle 200 -v -v 500 '
#data = os.popen(c).read()
#with open('a.log','w') as f:
#    f.write(data)
a = [3,4,5]
for i in a:
    print(i)
print('---',i)