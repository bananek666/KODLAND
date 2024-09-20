import random

letters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lenght = int(input("Podaj długość hasła: "))

password = ""

for i in range(lenght):
    password = password + random.choice(letters)

print("Twoje hasło:", password)


