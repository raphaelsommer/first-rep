import random

num = random.randint(0, 100)

print(num)

if input("randomize again? Y/N: ") == "Y":
    num_final = random.randint(0, 100)
    print(num_final)
else:
    print("ok. Your number stays ", num)
