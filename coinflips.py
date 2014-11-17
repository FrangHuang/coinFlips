#!/usr/bin/env python
import random

f = open("score.txt", "r+") # read and write
highestScore = f.read()

print("\nCoin guessing game. All time high score: {}.".format(highestScore))
score = 0

while True:
	side = random.choice(["heads", "tails"])
	guess = (raw_input("\nPredict heads or tails: ").lower())[0]

	while True:
		if guess != "h" and guess !="t":
			guess = (raw_input("\nPlease choose from heads and tails: ").lower())[0]
		else:
			break
	if guess == side[0]:
		score += 1
		print("You are correct! It is {}. Your present score is {}.".format(side, score))
	else:
		print("Sorry, it's {}. Good luck next time! Your final score is {}.".format(side, score))
		break

if score >= int(highestScore):
	f.seek(0)
	f.write(str(score))
	print("Congratulation! You are the highest score!")