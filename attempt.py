import datetime
class Attempt():

	def __init__(self, currQ = None, al = [], points=0):
		self.al = al

		if len(al) != 0:
			self.currQ = al[0]
			self.points = al[1]
			self.status = "in-progress"
			self.date = datetime.datetime.now().strftime("%x")
			self.calcScore()
		else:
			self.points = points
			self.status = "in-progress"
			self.date = datetime.datetime.now().strftime("%x")
			self.currQ = currQ
			self.calcScore()
			
	
	def __str__(self):
		if len(self.al) == 0:
			self.setAll()
		text = ""
		i = 0
		while i < len(self.al) - 2:
			text += str(self.al[i]) + "\n"
		text += self.al[len(self.al) - 1] 
		return text
	
	def calcScore(self):
		self.score = self.points/81
	
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
	
	def setAll(self):
		self.al.append(self.currQ)
		self.al.append(self.points)
		self.al.append(self.getScore)
		self.al.append(self.status)
		self.al.append(self.date)
	
