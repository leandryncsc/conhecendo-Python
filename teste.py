import os
from random import randint

user_pass = input("digite sua senha: ")

key = ['1', '2','3','4','5','6','7','8','9','10',
       'a','b','c','d','e','f','g','h','i','j',
       'k','l','m','n','o','p','q','r','s','t',
       'u','v','w','x','y','z','@','#','$','%','&']

guess = ""

while (guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = key[randint(0,25)]
        guess = str(guess_letter) + str(guess)
        print(guess)

print("sua senha é", guess)