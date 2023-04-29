import math

a = math.pi

game_on = True

while game_on:

    b = input("Guess the value of pi: ")

    diff = round(abs(a - float(b)), 5)

    if diff == 0:
        print("You got it!")
        game_on = False
    else:
        print("You were off by: " + str(diff))
