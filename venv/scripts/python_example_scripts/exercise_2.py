# Write a Python program to convert temperatures to and from celsius,
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
# author Jaba


print("Calculate Temperature in Degrees Celicius or Fahrenheit")

temp = int(input("Temp :"))
unit = input("(F) or (C) :").upper()

if unit == "F":
    fahrenheit = (temp * 1.8) + 32
    Fahrenheit = 9.0 / 5.0 * temp + 32
    print(f"Ans:{Fahrenheit}")
elif unit == "C":
    celsius = (temp - 32) * 1.8
    Celsius = (temp - 32) * 5.0 / 9.0
    print(f"Ans:{Celsius}")
