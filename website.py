print("Running my signup file")

def sign_up(username,password,email):               # function definition

    if len(username)>3 and len(password)>=8 and "@" in email:

        if any(char.isdigit() for char in password):
            print("Your entered data is correct.")
        else:
            print("Please try with different username, password, email.")
    else:
        print("Please try with different username, password, email.")

    print(f"UserName is :{username} , Email is : {password}")


un=input("Enter a username :")
pwd=input("Enter a password :")
em=input("Enter email :")

sign_up(un,pwd,em)
print("End of signup file")