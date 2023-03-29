import random
flag ="y"

while flag =="y" or flag =="":
    print("*"*30)
    print("Password Generator")
    print("*"*30)
    letters="abcdefghijklmnopqrstuvwxyz"
    characters= letters+letters.upper()


    pass_len=str(input("How many characters should the password be? min:8 default:8 "))

    if pass_len =="" or int(pass_len)<=8:
        pass_lenght =8
    else:
        pass_lenght = int(pass_len)
    print(pass_lenght)


    number = input("Do you want to use numbers in your password? Y/n ").lower()

    if  number=="y" or number=="":
        characters += "0123456789"


    special = input("Do you want special characters in your password? !@#$%^&*()? etc. Y/n ").lower()

    if  special == "y" or number == "" :
        characters += "!@#$%^&*()?"

    password = "".join(random.sample(characters,pass_lenght))

    print(f"Your Password: {password}")

    flag = input("Do you want to create a new password? Y/n ").lower()











