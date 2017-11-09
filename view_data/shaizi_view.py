import pygal;

from shaizi import Shaizi;

shaizi = Shaizi();

#投掷几次骰子，并将其存放到数组里
results = [];

for roll_num in range(1000):
	result = shaizi.roll();
	results.append(result);

#print(results);

#分析结果
frequencies = [];

for value in range(1,shaizi.num_sides+1):
	frequency = results.count(value);
	frequencies.append(frequency);
	
print(frequencies);

#对结果进行可视化
hits = pygal.Bar();

hits.title = "Results of rolling touzi 1000 times";
hits.x_labels = ["1","2","3","4","5","6"];
hits.x_title = "Result";
hits.y_title = "Frequency of Result";

hits.add("touzi",frequencies);

hits.render_to_file("touzi_view.svg");
