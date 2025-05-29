#write a python program to get temperature in fahrenhiet to convert into centigrade and kelvin

fahrenheit = float(input("Enter temperature in F : "))

celsius = (fahrenheit - 32) * 5/9 

kelvin =  celsius + 273.15

print(f"The {fahrenheit}f is converting into {celsius}c .")

print(f"The {fahrenheit}f is converting into {kelvin}k.")

