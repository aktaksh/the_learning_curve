def greet(name): # positional argument
    return f"Hello, {name}"

print(greet("Tiger"))
print("-----------------------------------------")

def check_disk_usage(value):
    if value < 80:
        return "oka lah"
    else: return "not good"

res = check_disk_usage(99)
print(res)
