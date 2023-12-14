import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()
while True:
    ask = input("To login press 1 \nTo signup press 2\n")

    #login functionality
    if ask == "1":
        un = input("Username: ")
        pw = input("Password: ")
        c.execute(f"select username, password from user_info where username = '{un}' and password = '{pw}'")
        result = c.fetchone()
        if result != None:
            print("Login Successful!")
        else:
            print("Login Failed")


    #signup functionality
    elif ask == "2":
        new_name = input("New Name: ")
        new_un = input("New Username: ")
        new_pw = input("New Password: ")
        c.execute(f"select username from user_info where username = '{new_un}'")
        result2 = c.fetchone()
        if result2 != None:
            print("Username has been taken")
        else:
            c.execute(f"insert into user_info values('{new_name}', '{new_un}', '{new_pw}')")
        conn.commit()
        
conn.commit()

