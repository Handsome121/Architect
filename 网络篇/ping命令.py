import re
import subprocess

"""
ping(选项)(参数)
-d：使用Socket的SO_DEBUG功能；
-c<完成次数>：设置完成要求回应的次数；
-f：极限检测；
-i<间隔秒数>：指定收发信息的间隔时间；
-I<网络界面>：使用指定的网络界面送出数据包；
-l<前置载入>：设置在送出要求信息之前，先行发出的数据包；
-n：只输出数值；
-p<范本样式>：设置填满数据包的范本样式；
-q：不显示指令执行过程，开头和结尾的相关信息除外；
-r：忽略普通的Routing Table，直接将数据包送到远端主机上；
-R：记录路由过程；
-s<数据包大小>：设置数据包的大小；
-t<存活数值>：设置存活数值TTL的大小；
-v：详细显示指令的执行过程。

"""


def check():
    online = []
    with open('host') as f:
        for ip in f.readlines():
            ip = ip.strip()
            cmd = 'ping -n 1 -i 1 -w 3 %s' % ip
            p = subprocess.run(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)
            out = p.stdout
            regex = re.compile("TTL=(\d+)", re.S | re.I)
            if len(regex.findall(out)) > 0:
                online.append(ip)
                print('%s 主机可达。。。' % ip)
            else:
                print('%s 主机不可达。。。' % ip)
                with open('fail_host', 'a') as f2:
                    f2.write(ip)
                    f2.write('\n')
    print(online)


if __name__ == '__main__':
    check()
