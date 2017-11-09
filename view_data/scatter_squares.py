import matplotlib.pyplot as plt;


#x_value = [1,2,3,4,5];
#y_value = [1,4,9,16,25];

x_value = list(range(1,1001));
y_value = [x**2 for x in x_value];

#plt.scatter(x_value,y_value,c="red",edgecolor="none",s=40);
#plt.scatter(x_value,y_value,c=(0.5,0.5,0.6),edgecolor="none",s=40);
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Reds,edgecolor="none",s=40);

#设置图表标题并给坐标轴加标签
plt.title("Scatter Square",fontsize=24);
plt.xlabel("Value",fontsize=14);
plt.ylabel("Square Value",fontsize=14);

#设置刻度的标记大小
plt.tick_params(axis="both",which="major",labelsize=14);

#设置每个坐标值的取值范围
plt.axis = [0,1100,0,1100000];

#保存的和显示的不能同时使用
#plt.show();
#自动保存图片,第一个参数表示保存图片的名字，第二个参数表示是否要把图表多余的空白区域裁剪掉，该参数可以忽略
plt.savefig("scatter_squares.png",bbox_inches="tight");
