import pygal;
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS;

my_style = LS("#333366",base_style=LCS);
chat = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False);

chat.title = "Python Project";
chat.x_labels = ["httpie","django","flask"];
plot_dicts = [
	{"value":16101,"label":"Description of httpie"},
	{"value":15208,"label":"Description of django"},
	{"value":14798,"label":"Description of flask"}
];

chat.add("",plot_dicts);
chat.render_to_file("my_chat.svg");
