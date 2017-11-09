class Dog():
	def __init__(self,name,age):
		self.name = name;
		self.age = age;
		self.color = 'white';
		
	def sit(self):
		print(self.name.title() + " is now sitting");
		
	def roll_over(self):
		print(self.name.title() + " rolled over");
	
	def update_color(self,color):
		self.color = color;
		
my_dog = Dog("kiki",5);
print("my dog's name is " + my_dog.name + ".");
print("my dog is " + str(my_dog.age) + " years old.");
print("my dog's color is " + my_dog.color + ".");
my_dog.sit();

my_dog.update_color("red");
print("my dog's color is " + my_dog.color + ".");
