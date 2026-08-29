#os module
import os
print(os.getcwd())
'''
os.chdir("C:\\Users\\Studnent\\Document")
print(os.getcwd())
'''

print(os.listdir())

##############################
import os
pid = os.fork()
if pid == 0:
    print("I am child")
else:
    print("I am parent")

#fork() -> create a new child process.
''' exec() -> does not create a new process, 
 Instead it replaces the current process with another program'''
