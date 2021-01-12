import json
import psutil
import threading
import time
import math


def lambda_handler(event, context):
    print('# of thread: ' + str(threading.active_count()))
    
    heavy(10000000)
    
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello good bye"
        }),
    }


def metric():
    for i in range(1):
        print('----------------------------')
        # mem
        mem = psutil.virtual_memory()
        print("mem[%] " + str(mem.percent))

        # cpu
        cpu = psutil.cpu_percent(interval=1)
        print("cpu[%] " + str(cpu))

        # cpu core
        core = psutil.cpu_percent(interval=1, percpu=True)
        print("cor[%] " + str(core))

        # disk
        disk = psutil.disk_usage('/')
        print("dsk[%] " + str(disk.percent))
        # time.sleep(0.5)


def worker(i):
    print('#' + str(i) + 'worker threading')
    for i in range(10):
        True
        

def heavy(n):
    i=0
    for x in range(n):
        a=math.factorial(10)
        i=i+1
    print("# of math: " + str(i))
 

print("namespace: " + __name__)


def threads():
    if __name__ in ['app','lambda_function'] :
        # metric = threading.Thread(target=metric)
        for i in range(20):
            t=threading.Thread(target=worker, args=(i,))
            # t.setDaemon(True) 
            t.start()
          

physical=psutil.cpu_count(logical=False)
logical=psutil.cpu_count(logical=True)

print("physical " + str(physical))
print("logical " + str(logical))

# threads()

# metric()
heavy(10000000)