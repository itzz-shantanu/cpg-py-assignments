inventory = ['pen', 'pencil', 'eraser']
product = input("Enter product name: ").lower()
if product in inventory:
    print("Product available")
else:
    print("Product not available")