responses = {};
#设置一个标识，指出调查是否继续
polling_active = True;
while polling_active:
	#提示被调查者的名字和回答
	name = input("\n what your name:");
	response = input("which mountain would you like to climb someday?");
	#将答案存储在字典中
	responses[name] = response;
	#看看是否还有人要参与调查
	repeat = input("would you like to let another person respond?(yes/no)");
	if repeat == "no":
		polling_active = False;

#调查结束显示结果
print("\n ----Poll Result----");

for name,response in responses.items():
	print(name + " would like to climb " + response + ".");
