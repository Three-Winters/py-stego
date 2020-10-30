import argparse

class Args():
	def __init__(self):
		self.parser = argparse.ArgumentParser(description='b')
		#self.parser.add_argument('image', type=str, help='The cover image to use')
		self.parser.add_argument('--secret', type=str, help='Path to data to be hidden')

		#self.parser.add_argument('methods', metavar='METHOD', type=str,
		#							 help='The embed/extract mode to use')
		self.parser.add_argument('--method', type=str, default='lsb',
									 help='The embed/extract method to use')

		#self.parser.add_argument('image', type=str, metavar='COVER',
		#							 help='The cover image to use')
		self.parser.add_argument('--extract', type=str, help='Extract a secret')
		self.parser.add_argument('--embed', type=str, help='Embed a secret')
		self.parser.add_argument('--output', type=str, default='output',
									 help='Path to store program output')

	def parse(self):
		self.args = self.parser.parse_args()
		return((self.args.extract, self.args.embed, self.args.method, self.args.secret,
					self.args.output))
