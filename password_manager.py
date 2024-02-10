# from cryptography.fernet import Fernet
master_password = input("what is the master password : ")


def add():
    user_name = input("Enter the username : ")
    password = input("Enter the password : ")
    with open("password.txt", "a") as f:
        f.write(user_name + "|" + password + "\n")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, psw = data.split("|")
            print("User Name : ", user, " | Password : ", psw)


while True:
    option = input(
        "would you like to add the password or view the password (view/add),If you want to quit type (q) : ").lower()
    if option == "q":
        break
    if option == "view":
        view()
    elif option == "add":
        add()
    else:
        print("You entered something wrong \n Try again")
        continue
