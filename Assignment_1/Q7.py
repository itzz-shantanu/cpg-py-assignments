age = int(input("Enter your age: "))
if age >= 21:
    print("Eligible for voting and driving")
elif age >= 18:
    print("Eligible for voting but not driving")
else:
    print("Not eligible for voting or driving")