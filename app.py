import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Introduce la longitud de la contraseña: "))
contraseña = ""
for _ in range(longitud):
    contraseña += random.choice(caracteres)

print("Tu contraseña generada es:", contraseña)
