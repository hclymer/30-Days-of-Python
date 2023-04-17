print()
print("UNIT CONVERTER")

conversions_available = [
    (1, 'km','mi'),
    (2,"mi",'km'),
    (3,'kg','lbs'),
    (4,'lbs','kg'),
    (5,'F','C'),
    (6,'C',"F")
]

print("Concersions available:")
print()

for conversion_number, from_unit, to_unit, in conversions_available:
    print(f'{conversion_number}) {from_unit} -> {to_unit}')


print()
conversion = input("enter of number of the convserion to use")
conversion_index = int(conversion) - 1

conversion_number, from_unit, to_unit = conversions_available[conversion_index]
print()

from_value = float(input(f"Enter {from_unit} -->"))

print()