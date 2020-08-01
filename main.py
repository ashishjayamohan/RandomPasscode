import secrets 
import string 

length = int(input("Enter length of Passcode: "))

alphabet = string.ascii_letters + string.digits 
while True: 
    password = ''.join(secrets.choice(alphabet) for i in range(length-2)) 
    if (any(c.islower() for c in password) and any(c.isupper()  
    for c in password) and sum(c.isdigit() for c in password) >= 3): 
        print('!' + password + '!') 
        break
