#!/usr/bin/env python3

# as the user for a 9 digit integer and compute its checksum
user_int = input("Please enter a 9 digit integer: ")
hash = 10*int(user_int[0]) + 9*int(user_int[1]) + 8*int(user_int[2]) + 7*int(user_int[3]) + 6*int(user_int[4]) + 5*int(user_int[5]) + 4*int(user_int[6]) + 3*int(user_int[7]) + 2*int(user_int[8])

i = 0
while (hash+i)%11 != 0:
    i += 1

if i == 10:
    i = "X"

hash_str = str(user_int)
isbn = hash_str + str(i)
print(isbn)