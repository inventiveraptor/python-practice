#/usr/bin/env python3
# high card low card 

import random

deck = [1,2,3,4,5,6,7,8,9]
d_number = random.choice(deck)

dealer = deck.pop(d_number)

print("dealer drew the ",dealer)

print(" ")
guess = input("do you think the next card is going to be higher or lower? ")

print("you guessed ", guess)
print("")

# player card info

p_number = random.choice(deck[0:len(deck)-1])
player = deck.pop(p_number)

print("your card is....")
print(player)

# determine winner

if player > dealer and guess == "higher":
    print("You win!")    
elif player < dealer and guess == "lower":
    print("You win!")
else:
    print("better luck next time")
