import json;

fileName = "numbers.json";

numbers = [1,3,5,7,9,11,13];

with open(fileName,"w") as file_object:
	json.dump(numbers,file_object);
