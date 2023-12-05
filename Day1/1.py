#################################################################################################
# Advent of Code 2023- Day 1
#################################################################################################
import re

def calibrationSum(dataIn):
	lines    = dataIn.split("\n")
	calTotal = 0

	for i in lines:
		digits = re.findall(r'[0-9]', i)
		calTotal += int(digits[0] + digits[-1])
	return calTotal


def main():
	with open('input.txt') as f:
		calLines = f.read().strip()

	# Part 1
	print(calibrationSum(calLines))

	# Part 2
	calLines = (calLines.replace("one",   "o1e")
		                .replace("two",   "t2o") 
		                .replace("three", "t3ee")
		                .replace("four",  "f4ur")
		                .replace("five",  "f5ve")
		                .replace("six",   "s6x")
		                .replace("seven", "s7ven")
		                .replace("eight", "e8ght")
		                .replace("nine",  "n9ne"))
	
	print(calibrationSum(calLines))


if __name__ == "__main__":
    main()