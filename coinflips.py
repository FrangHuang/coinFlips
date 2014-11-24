#!/usr/bin/env python
import random


while True:

	f = open("score.txt", "r+") # read and write
	record = f.readlines()
	#highestScore = f.read()

	print("\nCoin guessing game. All time high score: {}, by {}".format(str(int(record[0])),record[1]))
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

	if score >= int(record[0]):
		f.seek(0)
		f.truncate()
		f.write(str(score) + "\n")
		print("\nAnd congratulation! You are the highest score!")
		winner = raw_input("Please enter your name:")
		f.write(winner)

	f.close()
	
	clarify = raw_input("Do you want to play again?")
	if (clarify.lower())[0] != "y":
		print("Goodbye!")
		exit()