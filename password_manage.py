master_password = input("enter the master password:")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username,password = data.split("|")
            print("username:",username,"password:",password)
def add():
    username = input("enter the username:")
    password = input("enter the password:")
    with open('password.txt','a') as f:
        f.write(username + "|" + password + "\n")

while True:
   mode = input("do you want to add a new password or view or quit?(add/view/q):")
   if mode == "q":
       break
   if mode == "view":
       view()
   elif mode == "add":
       add()
   else:
       print("invalid mode")
       continue