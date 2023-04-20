def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)
 
a = int(input("Please select first number: "))
b = int(input("Please select second number: "))
 
# prints 12
print(f"The gcd of {a} and {b} is : ", hcfnaive(a, b))
