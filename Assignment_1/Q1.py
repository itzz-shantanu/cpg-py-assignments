bill = float(input("Enter total bill amount: "))
if bill > 1000:
    discount = 0.2
elif bill > 500:
    discount = 0.1
else:
    discount = 0
final_amount = bill - (bill * discount)
print(f"Final amount after discount: ₹{final_amount:.2f}")