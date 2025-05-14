allowed_users = ['john', 'amy', 'sita']
username = input("Enter username: ")
if username in allowed_users:
    print("Login successful")
else:
    print("Login failed")