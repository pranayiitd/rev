import re
import Serializer

class Event(object):
	
	def __init__(self, raw):
		"""pass"""
		self.raw_clean = raw[1:-1]
		self.parse()
	
	def parse(self):
		"""pass"""
		arr = self.raw_clean.split(" ")
		self.type = arr[0]
		self.duration = arr[1]

	def toString(self):
		"""pass"""
		s = "Type: %s Duration: %s"%(self.type, self.duration)
		return s

class Monologue(object):
	"""
		The unit of the model where
		each line of transcipt in stored
		in an object.
	"""
	def __init__(self, line):
		"""
			parses line to generate model.
		"""
		self.speaker = self.getSpeaker(line)
		self.text = self.getText(line)
		self.events = self.getEvents(line)

	def getSpeaker(self, line):
		"""
			Extract speaker of the monologue
		"""
		index = line.find(":")
		return line[:index]

	def getText(self, line):
		"""	
		   Extract the text sentences of the
		   monologue
		"""	
		index = line.find(":")
		return line[index+1:]

	def getEvents(self, line):
		"""
			Extracts all the events in the monologue
		"""
		VAR_TOKEN_START = '\['
		VAR_TOKEN_END = '\]'
		TOK_REGEX = re.compile(r"(%s.*?%s)" % (
			VAR_TOKEN_START,
			VAR_TOKEN_END
		))
		events = []
		arr = TOK_REGEX.split(line)
		for tup in arr:
			if(len(tup) > 1 and tup[0] == '['):
				events.append(Event(tup))

		return events
	
	def toString(self):
		s = "Speaker: %s Text: %s\n"%(self.speaker,self.text)
		for e in self.events:
			s += e.toString()		
		
		return s


class Model(object):
	"""
	Model to contain all the information
	
	"""

	def __init__(self):
		"""pass"""
		self.data = []

	def addMonologue(self, monologue):
		"""pass"""
		self.data.append(monologue)

	def generate(self, document):
		"""pass"""
		lines = document.split("\n")
		for line in lines:
			monologue = Monologue(line)
			self.data.append(monologue)


class Parser(object):
	"""
	Parses Rev document text into a model with
	all the data
	"""
	def __init__(self):
		"""pass"""

	def parse(self, document):
		"""pass"""
		m = Model()
		m.generate(document)
		return m

if __name__ == '__main__':
	"""pass"""
	document = "Pranay : I am the one.[pause 1:00][pause 1:00][pause 1:00][pause 1:00]\n" +"Pranay:This is my place[pause 01:00]. So fuck wahat??\n" +"Pranay:"
	p = Parser()
	m = p.parse(document)
	
	s = Serializer.Serializer()
	print s.serialize(m)

	# for o in m.data:
		# print o.toString()


