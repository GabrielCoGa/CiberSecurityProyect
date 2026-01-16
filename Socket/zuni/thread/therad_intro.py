import threading
"""Therading allow us to speed up grograms by task at the same time.
each task will run on its own thead
each tread can run simultaneusly and shae data with each other
Every thread when you start it must do Something, which we can define 
with a function. Our threads will then target these functions.
when we start the treads, the target functions will be fun.
"""

def function1():
    for i in range(10):
        print("ONE")

def function2():
    for i in range(10):
        print("TWO")

def function3():
    for i in range(10):
        print("THREE")


"""If we call these functions, we see the first function call MUST complete 
before the next. They are executed linearly"""

function1()
function2()
function3()
print("\nEND\n")

"""We can execute these functions concurrently using a thread. We must have a target for a thread"""
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

t1.start()
t2.start()
t3.start()

"""Threads can only run once. If you wan to reuse, you must redefine"""
t1 = threading.Thread(target=function1)
t1.start()

"""If you want to pause the main programing until a thread is done you can"""
t1 = threading.Thread(target=function1)
t1.start()
t1.join()#This pauses the main program until the thread is complete
print("threading rules!")

