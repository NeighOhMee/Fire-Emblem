#Contains the class for the zones of the map

class Zone(object):
	def __init__(self, x1, x2, y1, y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.xa = int((x1+x2)/2) #Pathing location of zone is currently the average x/y
		self.ya = int((y1+y2)/2)

	def inzone(self, pos): #Checks whether a position is within the current zone
		return self.x1 <= pos[0] <= self.x2 and self.y1 <= pos[1] <= self.y2