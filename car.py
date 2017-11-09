class Car():
	def __init__(self,make,mode,year):
		self.make = make;
		self.mode = mode;
		self.year = year;
		self.odometer_reading = 0;
		
	def get_descriptive_name(self):
		long_name = str(self.year) + " " + self.make + " " + self.mode;
		return long_name.title();
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " on it");
		
	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage;
		else:
			print("you can not roll back an odometer");
			
	def increment_odometer(self,miles):
		self.odometer_reading += miles;
