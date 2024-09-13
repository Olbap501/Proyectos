import random

caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
n_caracter = int(input("Introduce la longitud de la contraseña:"))
password = ""

for i in range(n_caracter):
    generation = random.randint(0, 71)
    password += str(caracter[generation])

print("Tu contraseña es:", password)
