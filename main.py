import pytz
import os
import Password
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
x=0
# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
mydb = client["passwords"]
mycol = mydb["myPasswords"]


while x == 0 :
    #random_character = random.choice(alfa)
    #print(random.choice(alfa))
    #ask name for password
    name = input("Define un nombre para tu contraseña\n")
    #define current time to be stored
    hora_actual = datetime.now(pytz.timezone('America/Costa_Rica'))
    #set initial attributes for p1 object to then, be able to call function to generate password
    p1 = Password.Password(hora_actual, name, None)
    p1.password = p1.GenPassword()

    save_pass = {"dateCreation": p1.dateCreation, "namePass" : p1.namePass, "Password": p1.password}
    print(datetime.now(pytz.timezone('America/Costa_Rica')))
    #Store Password attributes in Mongodb
    returnMongodbAction = mycol.insert_one(save_pass)
    print(returnMongodbAction)

    x = int(input("quieres seguir? 1/0 \n"))


