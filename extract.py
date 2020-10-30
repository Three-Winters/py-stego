from itertools import tee

class ExtractData():
	def __init__(self, cover):
		self.cover = cover
		self.data = cover[2]

	def find_end(self, height, width, data):
		r=0
		b=0
		while r+1 < height:
			if b+1 < width:
				if data[b][r] == 128:
					if data[b+1][r] == 64 and data[b+2][r] == 32:
						return((b)*(r))
				b += 1
			else:
				if data[b][r] == 128:
					if data[b+1][r] == 64 and data[b+2][r] == 32:
						return((b+1)*(r+1))
				b = 0
				r += 1
		return(0)


	def lsb(self):
		height = self.cover[0]
		width = self.cover[1]
		l=list(self.cover[2])
		ls = self.find_end(height, width, l)

		data = bytearray(ls)
		a = b''

		b=0
		r=0
		counter = 0
		for byte in data:
			bit = 0
			while bit < 9:
				if b < width:
					swap = (l[b][r] ^ byte ) & (1<<bit)
					#byte ^= ((byte ^ l[b][r]) & (1<<bit)) #swap #bytes([l[b][r]])
					byte ^= swap
					b += 1
					bit += 1
				else:
					b = 0
					r += 1
					swap = (l[b][r] ^ byte ) & (1<<bit)
					#byte ^= ((byte ^ l[b][r]) & (1<<bit))
					#byte ^= swap #bytes([l[b][r]])
					byte ^= swap
					bit += 1
				if bit == 8:
					a += bytes([byte])
			counter += 1
		return(a)
