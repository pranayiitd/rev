import re

class Serializer(object):
	"""
	Converts the model to XML.
	"""
	def __init__(self):
		pass

	def serialize(self, model):
		"""pass"""

		xml_output = ""
		for monologue in model.data:
			xml_output += self.generate_xml(monologue)+"\n"

		return "<transcript>\n%s</transcript>"%(xml_output)

	def generate_xml(self, monologue):
		"""pass"""
		ret = '<monologue speaker="'+monologue.speaker+'">'
		ret += self.generate_xml_text(monologue.text, monologue.events)
		ret += "</monologue>"

		return ret

	def generate_xml_text(self, text, events):
		"""pass"""
		VAR_TOKEN_START = '\['
		VAR_TOKEN_END = '\]'
		TOK_REGEX = re.compile(r"(%s.*?%s)" % (
			VAR_TOKEN_START,
			VAR_TOKEN_END
		))
		arr = TOK_REGEX.split(text)
		ret = ""
		event_id = 0
		for elem in arr:
			if(len(elem) > 1 and elem[0] == '['):
				elem = '<tag type="%s" timestamp="%s"/>'%(events[event_id].type, events[event_id].duration)
				event_id += 1
			
			ret += elem

		return ret

    
