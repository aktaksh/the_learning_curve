"""
def greet(name, role="devops"):
    print(f" --- your name is {name}, role is {role}")
    return f"your name is {name}, you work as {role}"

print(greet("Tiger", "sysadmin"))
"""

def check_service(service, status, env="prod"):
     if status:
        return f"service {service} is up in {env} "     
     else:
        return f"service {service} is down in {env} "

result = check_service("tomcat", False, "dev")
print(result)
            
