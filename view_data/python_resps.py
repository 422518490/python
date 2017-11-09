import requests;
import pygal;
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS;

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars';
r= requests.get(url);

print("status code :" + str(r.status_code));

#将API响应存储在一个变量中
response_dict = r.json();

#处理结果
print(response_dict.keys());

#探索有关仓库的信息
repo_dicts = response_dict["items"];

names,stars,plot_dicts = [],[],[];

for repo_dict in repo_dicts:
	names.append(repo_dict["name"]);
	#stars.append(repo_dict["stargazers_count"]);
	plot_dict = {
		"value":repo_dict["stargazers_count"],
		"label":repo_dict["full_name"],
		"xlink":repo_dict["html_url"]
	};
	plot_dicts.append(plot_dict);
	
#可视化
my_style = LS("#333366",base_style=LCS);

my_config = pygal.Config();
my_config.x_label_rotation = 45;
my_config.show_legend = False;
#设置图表主标题、副标题和主标签字体大小
my_config.title_font_size = 24;
my_config.label_font_size = 14;
my_config.major_label_font_size = 18;
#将较长的项目名缩短为15个字符
my_config.truncate_label = 15;
my_config.show_y_guides = False;
my_config.width = 1000;


#chat = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False);
chat = pygal.Bar(my_config,style=my_style);
chat.title = "Most-Starred Python project on Github";
chat.x_labels = names;
#chat.add("",stars);
chat.add("",plot_dicts);
chat.render_to_file("python_github.svg");
