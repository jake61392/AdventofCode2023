#################################################################################################
# Advent of Code 2023- Day 4
#################################################################################################
import math
import re

def countWinningNums(lineIn):
	card, winningNums = lineIn.split(":")[1].split("|")
	card        = set({int(x) for x in card.split()})
	winningNums = set({int(x) for x in winningNums.split()})
	return len(winningNums.intersection(card))


def main():
	totalPoints = 0
	totalCards  = 0
	lines       = []
	copies      = []
	for line in open("input.txt"):
		winningNumCnt = countWinningNums(line)
		if winningNumCnt > 0:
			totalPoints += 2**(winningNumCnt - 1)

		lines.append(line)
		copies.append(1)

	for i, line in enumerate(lines):
		winningNumCnt = countWinningNums(line)
		if winningNumCnt > 0:
			for j in range(1, winningNumCnt + 1):
				copies[i + j] += copies[i]

	totalCards = sum(copies)

	# Part 1
	print(totalPoints)

	# Part 2
	print(totalCards)

if __name__ == "__main__":
    main()