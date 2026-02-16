def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    else:
        return "Invalid Username or Password"

print(login("admin", "admin123"))
