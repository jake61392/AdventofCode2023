#################################################################################################
# Advent of Code 2023- Day 2
#################################################################################################
import math
import re
from collections import defaultdict

def main():
	with open('input.txt') as f:
		input = f.read().strip().split("\n")

	validGames, totalPower = 0, 0
	for line in input:
		pieces = re.sub("[;,:]", "", line).split()
		cubeColors = defaultdict(int)

		for count, color in zip(pieces[2::2], pieces[3::2]):
			cubeColors[color] = max(cubeColors[color], int(count))

		if cubeColors["red"] <= 12 and cubeColors["green"] <= 13 and cubeColors["blue"] <= 14:
			validGames += int(pieces[1])

		totalPower += math.prod(cubeColors.values())

	# Part 1
	print(validGames)

	# Part 2
	print(totalPower)


if __name__ == "__main__":
    main()