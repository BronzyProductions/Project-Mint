#Real World Assistant
#Features Of this code:
#Print, Loops, If, Elif, Else, Task Kill, SMTP mail server e-mailing
from time import sleep
import os
import smtplib
def quit():
    print("Goodbye, see you soon!")
    #Something You havent seen
    #Kills the programme fully when excecuted
    os.system("taskkill /f /im pythonw.exe")
    
#This part is still in testing and may not work on command, if so please comment this block of code out
#This piece of code is part of a recomendation box we have setup if you type in something thats not listed
#It will e-mail me what you were you looking for or whatever you type in the box below
def add():
    print("Please type it into the following")

    server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("16SFlynn@stjosephsrush.com", "Step@1298")
 
msg = "Hello"
server.sendmail("16SFlynn@stjosephsrush.com", "16SFlynn@stjosephsrush.ie", msg)
server.quit()
    
print("Welcome to the Real World Assistant or RWA created by Stephen Flynn")
sleep(3)
print("This assistant will tell you where to travel in and around Dublin")
sleep(3)
while True:
    choice=input("So what do you like tell me what do like, beaches, history, food or sport.....")
    sleep(3)

    if choice=="beaches":
        print("Beaches are all over the cost of Ireland!")
        print("But for food, scenary and quality I'd goto Skerries")

    elif choice=="history":
        print("Everywhere in Ireland has deep history")
        print("The best place to see Irish history is Dublin, the GPO, Leinster House, Kilmainham Jail.....the list is endless!")

    elif choice=="food":
        print("Great food is all over Dublin, if in the city for mexican the best place is Boojum, for salads Sprout and for burgers you might say McDonalds but can't beat a Bunson")

    elif choice=="sport":
        print("Matches are playing most ofthe time and are fairly cheap to get tickets for, the best place to see a football, hurling or rugby match you'll remeber is Croic Park or the Aviva Stadium, for basketball fans the National Basketball Arena is located in Tallaght")

    else:
        print("It would appear that we do not have that option?")
        break

while True:
    choice =input("Would you like to add that category? y/n....")
    sleep(3)

    if choice=="y":
        sleep(2)
        add()

    elif choice=="n":
        print("No problem, thanks for using Real World Assistant, if this did not help, you can goto the submit a category option and tell us why there! :)")
        sleep(3)
        quit()
        
