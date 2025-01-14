import Password
import pymongo
import random
import string
import sys

x=0
alfa = string.ascii_letters + string.digits

while x == 0 :
    #random_character = random.choice(alfa)
    #print(random.choice(alfa))
    random_character = ""
    cantDig = int(input("De cuantos dígitos quieres tu contraseña?\n"))
    for i in range( cantDig):
        random_character = random.choice(alfa) + random_character
    print(random_character)
    x = int(input("quieres seguir? 1/0 \n"))
