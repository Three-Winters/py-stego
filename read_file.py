import png

class ReadFile():
	def __init__(self, f):
		self.f = f
		if self.f.endswith('.png'):
			self.read = self.read_image
		else:
			self.read = self.read_bytes

	def read_bytes(self):
		data = b''
		try:
			with open(self.f, 'rb') as f:
				data = f.read()

		except FileNotFoundError:
			print("Invalid file: "+self.f)

		return(data)

	def read_image(self):
		try:
			r = png.Reader(file=open(self.f, 'rb'))
		except FileNotFoundError:
			print("Invalid file: "+self.f)
			return(0)

		data = r.read()
		return(data)
		#for row in data[2]:
		#	for pixel in row:
		#		print(pixel)
