name = input("What is your name? \n")
allowedUser = ('Yetunde')
allowedPassword = 'jumoke'
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


if(name in allowedUser) :
    password = input("Your password? \n")



    if(password ==allowedPassword):
        
                     print(dt_string)
                     print("What would you like to do today?")
                     print("1. How much would you like to withdraw?")
                     print("2. How much would you like to deposit?")
                     print("3. What issue will you like to report?")
                     

                     option = int(input('Please select an option \n'))
                     
                    
                     if(option == 1):
                         print("How much would you like to withdraw?")
                        

 
                     elif(option == 2):
                          print('you selected %s' %option)

                     elif(option == 3):
                         print('you selected %s' %option)

                     else:
                          print('Invalid option selected, please try again')