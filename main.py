import Password
import pymongo
import random
import string

x=0
alfa = string.ascii_letters + string.digits

while x == 0 :
    #random_character = random.choice(alfa)
    print(random.choice(alfa))
    x = int(input("quieres seguir? 1/0 \n"))
