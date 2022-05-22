import threading
import time
class power(threading.Thread):
    def __init__(self, num1, num2):
        super().__init__()
        self.num1 = num1
        self.num2 = num2
    def run(self):
        print("in thread", threading.current_thread().name)
        result=self.num1*self.num2
        time.sleep(1)
        print("result calculated", result)

start = time.perf_counter()

t1 = power(2, 25)
t2 = power(3, 255)
t3 = power(2, 15)
t4 = power(3, 155)

#t1 = threading.Thread(target=product, args=(100, 100000))
#t2 = threading.Thread(target=product, args=(100, 100000))
#t3 = threading.Thread(target=product, args=(100, 100000))
#t4 = threading.Thread(target=product, args=(100, 100000))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

t1.join()
t2.join()
t3.join()
t4.join()

end = time.perf_counter()
print(f"Completed in {end-start} seconds")