#定义函数
def greeter_user():
	print("hello");
	

greeter_user();

#定义默认值
def my_pet(petName,petType="dog"):
	print("my pet name is : " + petName + ",petType is " + petType);
	
my_pet(petName="baogu");
my_pet("diandian");

def get_formate_name(firstName,lastName):
	fullName = firstName + lastName;
	return fullName;

fullName = get_formate_name("lily","zhang");
print(fullName);
