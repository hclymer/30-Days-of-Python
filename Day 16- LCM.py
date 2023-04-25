def comput_lmc(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    
    while(True):
        if ((greater % x == 0)) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


def compute_gcd(x,y):
    
    while(y):
        x, y = y,x % y
    return x

def compute_lcm(x,y):
    lcm = (x*y)//compute_gcd(x,y)
    return lcm





a = int(input("Please select first number: "))
b = int(input("Please select second number: "))

print(f"The LCM of {a} and {b} is : ", compute_lcm(a, b))





