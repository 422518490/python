with open("pi_digits.txt") as file_object:
	#一次性读取
	#contents = file_object.read();
	#print(contents);
	#逐行读取
	#for line in file_object:
	#	print(line);
	lines = file_object.readlines();
	
for line in lines:
	print(line.strip());
