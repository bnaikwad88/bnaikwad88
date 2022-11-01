import re

reg = r'\b[A-Za-z0-9_%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
rex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,15}$"


def login():
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
        f.close()
        if email == stored_email and pwd == stored_pwd:
            print("Logged in Successfully!")
        else:
            print("Login failed! BAD CREDENTIALS!!! \n")


def signup():
    email = input("Enter email address: ")
    if re.fullmatch(reg, email):
        pwd = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        if re.match(rex, conf_pwd) :
            if conf_pwd == pwd:
                with open("credentials.txt", "w") as f:
                    f.write(email + "\n")
                    f.write(pwd)
                f.close()
                print("You have registered successfully!")
            else:
                print("Password is not same as above! \n")
        else:
            print("PASSWORD NOT CORRECT!!!")

    else:
        print("Enter valid email format")


def forget():
    email = input("Enter email: ")
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
        f.close()
        if email == stored_email:
            with open("credentials.txt", "r") as f:
                stored_email, stored_pwd = f.read().split("\n")
                f.close()
                print(f"The password for your email is :{stored_pwd}")
        else:
            print("email id not matched/You have not registered")


while True:
    print("<><><><><><><><><><>EMAIL LOGIN / REGISTRATION<><><><><><><><><><>")
    print("1) Login ")
    print("2) Register ")
    print("3) Forget Password")
    print("4) Exit ")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        login()
    elif choice == 2:
        signup()
    elif choice == 3:
        forget()
    elif choice == 4:
        exit()
    else:
        print("WRONG CHOICE!!!")
        break