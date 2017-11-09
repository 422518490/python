import json;

fileName = "numbers.json";

with open(fileName) as fileOpen:
	numbers = json.load(fileOpen);

print(numbers);
