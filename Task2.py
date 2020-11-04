class Airplane:

	def __init__(self, consumption, position_x, position_y, fuel_level):
		self.consumption = consumption
		self.position_x=position_x
		self.position_y=position_y
		self.fuel_level=fuel_level

	def constructor(self,initX, initY,consumption,initial_fuel_level):
		self.position_x=initX
		self.position_y=initY
		self.fuel_level=initial_fuel_level
		self.consumption = consumption

	def goto(self,destX,destY):
		#Calculate distancie between my point and the dest point. See if the consumption is enoug. Euclidian Dist on Km, consumption on Km/l, fuel_level on liters.
		distance=((destX-self.position_x)**2+(destY-self.position_y)**2)**(1/2)
		if self.consumption*self.fuel_level > distance:
			self.fuel_level=self.fuel_level-(distance/self.consumption)
			return True
		else:
			return False

	def refuel(self,fuel_added):
		self.fuel_level = self.fuel_level + fuel_added
