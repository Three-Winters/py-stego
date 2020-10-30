import png

class WriteFile():
	def __init__(self, f, data):
		self.f = f
		self.data = data

		if self.f.endswith('.png'):
			self.write = self.write_png
		else:
			self.write = self.write_bytes

	def write_bytes(self):
		with open(self.f, 'wb') as f:
			f.write(self.data)

	def write_png(self):
		png.from_array(self.data, 'RGB').save(self.f)
