
class EmbedData():
	def __init__(self, cover, secret):
		self.cover = cover
		self.secret = secret

	def lsb(self):
		height = self.cover[0]
		width = self.cover[1]
		l=list(self.cover[2])

		if len(self.secret) > height+width:
			print("Error: image is too small for secret!")
			print("Your image: "+str(len(self.secret))+" bytes")
			print("Max secret size: "+str(height+width)+" bytes")
			return(0)
		else:
			b = 0
			r = 0
			for byte in self.secret:
				bit = 0
				while bit < 9:
					if b < width:
						swap = (l[b][r] ^ byte) & (1 << bit)
						l[b][r] ^= swap
						#l[b][r] = ((byte ^ l[b][r]) & (1<<bit))
						b += 1
						bit += 1
					else:
						b = 0
						r += 1
						swap = (l[b][r] ^ byte) & (1 << bit)
						l[b][r] ^= swap
						#l[b][r] = ((byte ^ l[b][r]) & (1<<bit))
						bit += 1
		#l[b+1][r] = 128
		#l[b+2][r] = 64
		#l[b+3][r] = 32
		return(l)
