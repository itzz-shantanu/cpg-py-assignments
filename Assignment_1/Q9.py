allowed_users = ['john', 'amy', 'sita']
allowed_roles = ['admin', 'manager']

username = input("Enter username: ")
role = input("Enter role: ")

if username in allowed_users and role in allowed_roles:
    print("Login successful")
else:
    print("Login failed")