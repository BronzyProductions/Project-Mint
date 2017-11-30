#Real World Assistant
#Features Of this code:
#Print, Loops, If, Elif, Else, Task Kill, SMTP mail server e-mailing
from time import sleep
import os
def quit():
    print("Goodbye, see you soon!")
    #Something You havent seen
    #Kills the programme fully when excecuted
    os.system("taskkill /f /im pythonw.exe")

def add():
    print("Please type it into the following")
    
print("Welcome to the Real World Assistant or RWA created by Stephen Flynn")
sleep(3)
print("This assistant will tell you where to travel in and around Dublin")
sleep(3)
while True:
    choice=input("So what do you like tell me what do like, beaches, history, buildings, food or sport.....")
    sleep(3)

    if choice=="beaches":
        print("Beaches are all over the cost of Ireland!")
        print("But for food, scenary and quality I'd goto Skerries")

    elif choice=="history":
        print("hiiiii")

    elif choice=="buildings":
        print("hello")

    elif choice=="food":
        print("hi")

    elif choice=="sport":
        print("hi")

    else:
        print("It would appear that we do not have that option?")
        break

while True:
    choice =input("Would you like to add that category? y/n....")
    sleep(3)

    if choice=="y":
        add()
        
