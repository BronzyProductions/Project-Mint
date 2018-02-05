from time import sleep
class Monster:

    health = 10
    stamina = 10
    stealth = 10

    def getHit(self):
        self.health = self.health - 2

    def sayHealth(self):
        print("Monster health is " + str(self.health))

    def startRunning(self):
        self.stamina = self.stamina - 3

    def sayStamina(self):
        print("Monster stamina is " + str(self.stamina))

    def makeNoise(self):
        self.stealth = self.stealth - 5

    def sayStealth(self):
        print("Monster stealth is " + str(self.stealth))

Larry = Monster()
Barry = Monster()


choice = input("You are faced by two zombies, which one do you attack first? /Hit Larry or Hit Barry....")
sleep(2)

if choice == "Barry":
    sleep(2)
    print("The smack didn't do much")
    Barry.getHit()
    Barry.sayHealth()

elif choice == "Larry":
    sleep(2)
    print("The smack didn't do much")
    Larry.getHit()
    Larry.getHit() 

