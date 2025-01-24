import random
import string
alfa = string.ascii_letters + string.digits


class Password:
    def __init__(self, dateCreation, namePass, password):
        self.dateCreation = dateCreation
        self.namePass = namePass
        self.password = password

    def GenPassword(self):
        random_Password = ""
        cantDig = int(input("De cuantos dígitos quieres tu contraseña?\n"))
        for i in range(cantDig):
            random_Password = random.choice(alfa) + random_Password

        return random_Password

