from args import Args
from read_file import ReadFile
from embed import EmbedData
from write_file import WriteFile
from extract import ExtractData

def main():
	a = Args()
	extract, embed, method, secret, output = a.parse()

	if extract and embed:
		print('Use only one of the following: --extract, --embed\nAborting.')
		return(1)
	elif not extract and not embed:
		print('Use only one of the following: --extract, --embed\nAborting.')
		return(1)

	if embed:
		if not secret:
			print("No secret supplied. Aborting.")
			return(1)

		cover = ReadFile(embed)
		cover_data = cover.read()

		secret = ReadFile(secret)
		secret_data = secret.read()

		e = EmbedData(cover_data, secret_data)
		if method == 'lsb':
			e_image_data = e.lsb()
		else:
			print("Unknown method supplied, aborting.")
			return(0)

		if not output.endswith('.png'):
			output += '.png'
		secret_image = WriteFile(output, e_image_data)
		secret_image.write()
	else:
		e_cover = ReadFile(extract)
		e_cover_d = e_cover.read()
		ext = ExtractData(e_cover_d)
		if method == 'lsb':
			hidden_data = ext.lsb()
		w_secret = WriteFile(output, hidden_data)
		w_secret.write()

main()
