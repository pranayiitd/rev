import optparse
import Parser
import Serializer

if __name__ == '__main__':
	"""pass"""
	
	p = optparse.OptionParser()
	document, xml_output = p.parse_args()[1]

	f = open(document, "r")
	document = f.read()
	f.close()

	p = Parser.Parser()
	m = p.parse(document)
	
	s = Serializer.Serializer()
	xml = s.serialize(m)

	f = open(xml_output, "w")
	f.write(xml)
	f.close()