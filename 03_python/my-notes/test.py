import os
pid = os.fork()

if pid == 0:

    print("I am child")

else:

    print("I am parent")