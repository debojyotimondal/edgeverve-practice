import threading
import time
data=1

def increase(lock):
    global data
    lock.acquire()
    data+=1
    #print(data)
    lock.release()

def decrease(lock):
    global data
    lock.acquire()
    data-=1
    #print(data)
    lock.release()

def do(func, lock):
    for n in range(1, 100000):
        func(lock)

start = time.perf_counter()

lock = threading.Lock()

t1=threading.Thread(target=do,args=(increase, lock))
t2=threading.Thread(target=do,args=(decrease, lock))

t1.start()
t2.start()
t1.join()
t2.join()


end = time.perf_counter()
print(f"Completed in {end-start} seconds")