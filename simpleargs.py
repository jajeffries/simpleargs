import sys

__all__ = ["SimpleArgParser"]

_parserClass = None
if '2.7' == sys.version[:3]:
	from argparse import ArgumentParser
	_parserClass = ArgumentParser
elif '2.6' == sys.version[:3]:
	from optparse import OptionParser
	_parserClass = OptionParser
	
class SimpleArgParser(object):
	
	def __init__(self, *args, **kwargs):
		self.parser = _parserClass(*args, **kwargs)
		if self.parser.__class__.__name__ == "OptionParser":
			self.addArg = self.parser.add_option
		elif self.parser.__class__.__name__ == "ArgumentParser":
			self.addArg = self.parser.add_argument
		self.parseArgs = self.parser.parse_args
		
if __name__ == "__main__":
	parser = SimpleArgParser(description="A command line string formatter")
	parser.addArg('-r',
				  dest="rangeMode",
			  	  action="store_true", 
				  default=False,
				  help="run in range mode")
	parser.addArg('-f',
						dest="fmt",
						action="store",
				help="string format")
	parser.addArg('-a',
				  dest="fmtArgs",
				  action="store",
				  help="arguments for string format")
	parser.addArg('-v', '--version', action='version')

	args = parser.parseArgs(sys.argv[1:])
	print args