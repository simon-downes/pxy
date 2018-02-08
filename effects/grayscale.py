

# http://www.tannerhelland.com/3643/grayscale-image-algorithm-vb6/

def average(src, channels):

	def gray(r, g, b):
		return (r + g + b) / 3

	return _apply(src, channels, gray)

def luma(src, channels):

	def gray(r, g, b):
		return int((r * 0.2126) + (g * 0.7152) + (b * 0.0722))

	return _apply(src, channels, gray)

def desaturate(src, channels):

	def gray(r, g, b):
		return int((max(r, g, b) + min(r, g, b) ) / 2)

	return _apply(src, channels, gray)

def decompose_min(src, channels):

	def gray(r, g, b):
		return min(r, g, b)

	return _apply(src, channels, gray)

def decompose_max(src, channels):

	def gray(r, g, b):
		return max(r, g, b)

	return _apply(src, channels, gray)

def red(src, channels):

	def gray(r, g, b):
		return r

	return _apply(src, channels, gray)

def green(src, channels):

	def gray(r, g, b):
		return g

	return _apply(src, channels, gray)

def blue(src, channels):

	def gray(r, g, b):
		return b

	return _apply(src, channels, gray)

def shades_4(src, channels):
	return _shades(src, channels, 4)

def shades_8(src, channels):
	return _shades(src, channels, 8)

def shades_16(src, channels):
	return _shades(src, channels, 16)

def _shades(src, channels, shades):

	def gray(r, g, b):
		conversion_factor = 255 / (shades - 1)
		avg = (r + g + b) / 3
		return int((avg / conversion_factor) + 0.5) * conversion_factor

	return _apply(src, channels, gray)

def _apply(src, channels, func):

	dest = bytearray(len(src))

	for i in range(0, len(src), channels):

		gray = func(ord(src[i]), ord(src[i + 1]), ord(src[i + 2]))

		dest[i]     = gray
		dest[i + 1] = gray
		dest[i + 2] = gray

		if channels == 4:
			dest[i + 3] = src[i + 3]

	print 'done'

	return dest