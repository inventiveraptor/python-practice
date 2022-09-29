#! /usr/bin/env python3

num_players = input("How many players are there? ")
num_players = int(num_players)

players = []

player_1_score = 0
player_2_score = 0
player_3_score = 0
player_4_score = 0

while len(players) < num_players:
    player_name = input("Enter player's name: ")
    players.append(player_name)

if len(players) == 2:
    player_1 = players[0]
    player_2 = players[1]
    while True:
        print("How many points for ", player_1, "? ")
        p1_increment = int(input())
        player_1_score += p1_increment
        print("How many points for ", player_2, "? ")
        p2_increment = int(input())
        player_2_score += p2_increment
        print(player_1, " has ", player_1_score, " points")
        print(player_2, " has ", player_2_score, " points")
elif len(players) == 3:
    player_1 = players[0]
    player_2 = players[1]
    player_3 = players[2]
    while True:
        print("How many points for ", player_1, "? ")
        p1_increment = int(input())
        player_1_score += p1_increment
        print("How many points for ", player_2, "? ")
        p2_increment = int(input())
        player_2_score += p2_increment
        print("How many points for ", player_3, "? ")
        p3_increment = int(input())
        player_3_score += p3_increment
        print(player_1, " has ", player_1_score, " points")
        print(player_2, " has ", player_2_score, " points")
        print(player_3, " has ", player_3_score, " points")
elif len(players) == 4:
    player_1 = players[0]
    player_2 = players[1]
    player_3 = players[2]
    player_4 = players[3]
    while True:
        print("How many points for ", player_1, "? ")
        p1_increment = int(input())
        player_1_score += p1_increment
        print("How many points for ", player_2, "? ")
        p2_increment = int(input())
        player_2_score += p2_increment
        print("How many points for ", player_3, "? ")
        p3_increment = int(input())
        player_3_score += p3_increment
        print("How many points for ", player_4, "? ")
        p4_increment = int(input())
        player_4_score += p4_increment
        print(player_1, " has ", player_1_score, " points")
        print(player_2, " has ", player_2_score, " points")
        print(player_3, " has ", player_3_score, " points")
        print(player_4, " has ", player_4_score, " points")
else:
    print("Number of players must be 2-4")