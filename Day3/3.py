#################################################################################################
# Advent of Code 2023- Day 3
#################################################################################################
import math
import re

def main():
	total1 = 0
	total2 = 0
	with open("input.txt") as file:
		input = file.readlines()
		for row in range(len(input)):
			for col in range(len(input[0])):
				symbolCount = 0
				symbolMult  = 1
	
				if not (input[row][col]).isdigit() and input[row][col] not in [".", "\n"]:
					for rowOFF in range(row - 1,row + 2):
						for colOFF in ["-3,0", "-2,1", "-1,2", "0,3", "1,4", "-2,0", 
									   "-1,1", "0,2", "1,3", "-1,0", "0,1", "1,2"]:
							colA, colB = [int(a) for a in colOFF.split(",")]
	
							if input[rowOFF][col+colA:col+colB].isdigit():
								symbolCount  += 1
								number        = int(input[rowOFF][col + colA:col + colB])
								total1       += number
								symbolMult   *= number
								input[rowOFF] = input[rowOFF][0:col + colA] + 
												("." * abs(colA - colB))    + 
												input[rowOFF][col + colB:]

				if symbolCount == 2:
					total2 += symbolMult

	# Part 1
	print(total1)

	# Part 2
	print(total2)


if __name__ == "__main__":
    main()