import time
def measure_time(func):
    def inner():
        start = time.time()
        func()
        time_length = time.time() - start
        print(f"time : {time_length}")
    return inner

@measure_time
def greetings():
    print("Hello World!")
    
greetings()