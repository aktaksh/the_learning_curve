# '''import os
# print(os.path.exists("student.txt")) # check files and folders
# print(os.path.isdir("Day9_functions.py"))
# print(os.path.isfile("Day9_functions.py"))

# if not os.path.exists("data"):
#     os.mkdir("data")

# os.makedirs("data/students/marks")
# '''

# #subprocess - create new process and execute os commands/prgram

# '''
# run a shell program
# run ping
# open another program
# send input to  progrm
# cpture its outputs
# executes programs
# '''

# import subprocess
# result = subprocess.run("dir",shell=True)
# print(result.returncode)
# subprocess.run(["python","--version"])
# subprocess.run("python --version",shell=True)
# # subprocess.run(["cmd","/C","dir"])
# # subprocess.run(["ls"])
# # subprocess.run(["pwd"])

# result = subprocess.run(["Python","--version"],capture_output=True)
# print(result.stdout)

# result = subprocess.run(
#     ["python","-c","name=input(); print('Hello',name)"],
#     input="John\n",
#     capture_output=True,
#     text=True
# )
# print(result.stdout)

# subprocess.run(
#     ["python","-c","import time; time.sleep(10)"],
#     timeout = 3
# )

#THREADING
import threading
#thread: small unit of execution inside a process

# import time
# def task1():
#     time.sleep(3)
#     print("Task 1 completed")

# def task2():
#     time.sleep(3)
#     print("Task 2 completed")

# task1()
# task2()

#CREATING A THREAD
# import threading
# def task():
#     print("Task is running")
# t = threading.Thread(target=task) #creates a thread object
# t.start()

'''
import threading
import time
def task1():
    for i in range(5):
        print("Task 1:",i)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2:",i)
        time.sleep(1)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()

t1.join()
t2.join()
print("All tasks completed")
'''

import threading
def greet(name):
    print("Hello",name)
    print("Running: ",threading.current_thread().name)

t = threading.Thread(
    target=greet,
    args=("Harry",),
    name="Worker-1"
)
t.start()
print(t.is_alive())
t.join()

'''
Threading              Multiprocessing

Multiple threads      Multiple processes
Same Process          Separate Processes
Shared memory         Separate memory spaces
For I/O bound tasks   CPU-bound tasks

'''

#Lock: allows only one thread at a time.
import threading
counter = 0
lock = threading.Lock()
def increment():
    global counter
    for i in range(100000):
        with lock:
            counter+=1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()

print(counter)



