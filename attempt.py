import datetime
class Attempt():

	def __init__(self, points, total, currQ):
		self.points = points
		self.total = total
		self.status = "in-progress"
		self.date = datetime.datetime.now().strftime("%x")
		self.currQ = currQ
		self.score = points/total
	
	def calcScore(self):
		self.score = self.points/self.total
	
	def getScore(self):
		self.calcScore()
		return self.score
	
	def setDate(self):
		self.date = datetime.datetime.now().strftime("%x")	
	
	def update(self, points, currQ):
		self.calcScore()
		self.setDate()
		self.points = points
		self.currQ = currQ
	
	def finish(self, points):
		self.calcScore()
		self.setDate()
		self.points = points
		self.status = "complete"
