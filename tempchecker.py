t = float(input("Enter the temperature in Celcius: "))
if t<=15:
    print("Cold")
elif t>15 and t<30:
    print("Warm")
elif t>=30:
    print("Hot")
else:
    print("Invalid input")