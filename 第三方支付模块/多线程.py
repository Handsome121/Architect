import threading


def addTaskThread():
    pass


def updateStatusThread():
    pass


def downloadPcapThread():
    pass


init_submit = 1
threads = []
for i in range(3):
    if i == 0:
        t = threading.Thread(target=addTaskThread, args=(init_submit,))
    elif i == 1:
        t = threading.Thread(target=updateStatusThread, args=(init_submit,))
    else:
        t = threading.Thread(target=downloadPcapThread, args=(init_submit,))
    threads.append(t)
for t in threads:
    t.start()
for thread in threads:
    thread.join()
