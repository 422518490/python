from collections import OrderedDict;

favorite_languages = OrderedDict();

favorite_languages["Jan"] = "python";
favorite_languages["Bob"] = "c";
favorite_languages["Lucy"] = "java";
favorite_languages["Tom"] = "js";

for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title());
