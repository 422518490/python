motor = [];
motor.append("b");
motor.append("c");
motor.append("a");

print(motor);

print(sorted(motor));
print(motor);

motor.reverse();
print(motor);

print(len(motor));

for m in motor:
	print(m);


motor.sort();

print(motor);



del motor[1];

print(motor);

motor.append("d");
motor.append("e");

print(motor);

popout = motor.pop();

print(popout);
print(motor);

locpop = motor.pop(1);
print(locpop);
print(motor);

motor.remove("a");
print(motor);

for value in range(1,5):
	print(value);
	
numbers = list(range(1,6,2));
print(numbers);

print(min(numbers));

print(max(numbers));

print(sum(numbers));

squares = [value**3 for value in numbers];
print(squares);

print(numbers[0:1]);

dimensions = (200,100);
for dimension in dimensions:
	print(dimension);
	
#dimensions[0] = 50;
#print(dimensions);

dimensions = (10,20);
for dimension in dimensions:
	print(dimension);
	
age0 = 17;
age1 = 20;
if age0 > 18:
	print("aged 18...");
else:
	print("less than 19");
	
if age0 > 18 and age1 > 20:
	print("bird");
else:
	print("duck");

if age0 >= 18 or age1 >= 20:
	print("big");
else:
	print("small");
	
if 10 in dimensions:
	print("exists");
else:
	print("please add new ");
	
if 15 not in dimensions:
	print("please add new ");
else:
	print("exists");
	
if age0 < 10:
	print("smaller");
elif age0 < 18:
	print("small");
else:
	print("big");


alien0 = {
	"color":"green",
	"points":5
};
print(alien0["color"]);
print(alien0["points"]);

alien0["color"] = "yellow";
print(alien0);

del alien0["color"];
print(alien0);

user_0 = {
	"username":"lily",
	"age":18,
	"sex":"girl"
	}
	
for key,value in user_0.items():
	print("key: " + key);
	print("value: " + str(value));
	
for key in user_0.keys():
	print("key: " + key);
	
for value in set(user_0.values()):
	print("value: " + str(value));

current_number = 1;
while current_number <= 5:
	print(current_number);
	current_number += 1;
