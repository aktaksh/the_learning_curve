name = input("Enter your name: ")
role = input("Enter your role: ")
print(f"Hello {name}, you are a {role}")
disk = int(input("Enter the size of the disk: "))
print(f"The size of the disk is {disk}GB")
if disk > 85:
    print("The disk almostfull")
else:
    print("The disk is healthy")

environment = str(input("Enter the environment: "))
if environment == "production":
    print("The environment is production")
else:
    print("The environment is not production")  



