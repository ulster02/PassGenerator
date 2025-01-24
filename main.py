from xmlrpc.server import list_public_methods

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
passDict = {}


def ListPassword():
    y=1
    for i in mycol.find({}, {"_id": 0, "namePass": 1, "Password": 1}):
        passDict[y] = {"namePass": i["namePass"], "Password": i["Password"]}
        print(f"{y} - Nombre Contraseña: {i["namePass"]} - Contraseña : {i["Password"]}")
        y+=1

def menu(option):
    match option:
        case 1:
            print("Generar contraseña")
            # ask name for password
            name = input("Define un nombre para tu contraseña\n")
            # define current time to be stored
            hora_actual = datetime.now(pytz.timezone('America/Costa_Rica'))
            # set initial attributes for p1 object to then, be able to call function to generate password
            p1 = Password.Password(hora_actual, name, None)
            p1.password = p1.GenPassword()

            save_pass = {"dateCreation": p1.dateCreation, "namePass": p1.namePass, "Password": p1.password}
            # Store Password attributes in Mongodb
            returnMongodbAction = mycol.insert_one(save_pass)
            print(returnMongodbAction)
        case 2:
            print("Listar contraseñas")
            #Function to list password and store them in a Dict Array
            ListPassword()
        case 3:
            print("Eliminar Contraseña")
            #First, list all passwords
            ListPassword()
            #Introduce which one you want to delete
            y = int(input("Ingrese el número de contraseña que desea eliminar\n"))
            #Take password name to remove it from MongoDB atlas and print result
            print(mycol.delete_one({"namePass": passDict[y].get("namePass")}))
        case 4:
            #ends program
            print("Salir")
            global x
            x = 1

while x == 0 :
    option = int(input("Seleccion una opción: \n"
          " 1 - Generar contraseña \n"
          " 2 - Listar contraseñas \n"
          " 3 - Eliminar contraseña \n"
          " 4 - Salir\n"))
    menu(option)



