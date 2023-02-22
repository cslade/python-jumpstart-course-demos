import random


print("Welcome to Program 02")
print("-----------------------------")
print("Lets Play the Guessing game", end:="\n")


name = input("Tell me your name first: ")
lucky_number = random.randint(0, 100)
wag = -1
while wag != lucky_number:
    wag_text = input("Guess what number is in my head: " )
    wag = int(wag_text)
    if wag < lucky_number:
        print(f"Yo {name} {wag} is too low my friend")
    elif wag > lucky_number:
        print(f"Yo {name} {wag} is too high my friend")
    else: 
        print(f"Dang {name} you guessed {wag} and it is {lucky_number}")

print('we done here')
    
    
        