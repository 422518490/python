from random import choice;

class RandomWalk():
	"""一个生成随机漫步数据的类"""
	
	def __init__(self,number_points=5000):
		"""初始化随机漫步的属性"""
		
		self.number_points = number_points;
		
		#所有的随机漫步都开始于(0,0)
		self.x_values = [0];
		self.y_values = [0];
		
	def fill_walk(self):
		"""计算随机漫步包含的所有点"""
		
		#不断漫步，直到列表到达指定的长度
		while len(self.x_values) < self.number_points:
			#决定前进的方向，以及前进的距离
			x_direction = choice([1,-1]);
			x_distince = choice([0,1,2,3,4]);
			x_step = x_direction * x_distince;
			
			
			y_direction = choice([1,-1]);
			y_distince = choice([0,1,2,3,4]);
			y_step = y_direction * y_distince;
			
			#拒绝原地踏步
			if x_step == 0 and y_step == 0:
				continue;
				
			#计算下一个节点的x和y值
			next_x = self.x_values[-1] + x_step;
			next_y = self.y_values[-1] + y_step;
			
			self.x_values.append(next_x);
			self.y_values.append(next_y);
