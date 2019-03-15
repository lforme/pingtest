import os, time, sys


def checkIPs(path):
    f = open(path)
    lines = f.readlines()
    start_time = int(time.time())
    count_success = 0
    count_fail = 0
    success = []

    for line in lines:
        ip = line.replace('\n', '')
        result = os.system('ping -c1 -W1 %s'%ip)
        if result:
            print("ping %s is fail" % (ip))
            count_false += 1
        else:

            print("ping %s is ok" % (ip))
            count_success += 1
            success.append(ip)

    end_time = int(time.time())
    cost_time = end_time - start_time
    print("time(秒)：", cost_time,"s")
    print("ping通的ip数：", count_success, "   ping不通的ip数：", count_fail)
    print("可以使用的节点: ", "\033[32m%s\r\033[0m" % success)

    return (cost_time, count_success, count_fail, success)


