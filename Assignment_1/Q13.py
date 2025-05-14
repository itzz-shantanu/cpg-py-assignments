balance = 5000  # Example balance
amount = int(input("Enter withdrawal amount: "))

if amount > balance:
    print("Insufficient balance")
elif amount % 100 != 0:
    print("Amount must be multiple of 100")
else:
    print("Withdrawal approved")
    balance -= amount
    print(f"New balance: {balance}")