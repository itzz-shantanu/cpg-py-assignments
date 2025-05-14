temp = float(input("Enter temperature in °C: "))
if temp > 40:
    print("Heat Alert")
elif 30 < temp <= 40:
    print("Warm")
else:
    print("Normal")