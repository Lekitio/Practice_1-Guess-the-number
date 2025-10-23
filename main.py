


import random as r


#hälsning

name = input("Vad heter du? ")
print(f"Hej {name} välkommen tll spelet!")


#sluma ett tal
guess_to = r.randint(1, 10) #idk if this includes 1 or not

print("Du ska gissa ett tal emellan 1 och 10")

#Task: you can make this into a thiing tha tries if its an int or not
# guess = int(input())

# if guess == guess_to:
#     print("yay confetti")
# else:
#     print(f"Nope answer is {guess_to}")

#flera försök:

count = 0
for i in range(3):
    guess = int(input())
    count += 1

    if guess == guess_to:
        print("yay confetti")
        print(f"it took you {count} tries")
        break
    else:
        print("Nope")
        if count == 3:
            print(f"Sucks the answer is {guess_to}")
