import gi

import ui

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GdkPixbuf, GObject

# http://www.tannerhelland.com/3643/grayscale-image-algorithm-vb6/
# http://www.tannerhelland.com/4660/dithering-eleven-algorithms-source-code/

# foreground #7F92FF
# background #FF6A00

class ImgViewer():

	def __init__(self, img_path):
		
		self.ui = ui.MainWindow(400, 300)

		self.ui.connect('load_image', self._load_image)


		if img_path:
			self.load_image(img_path)
			self.img.flip_vertical()
			self.ui.update_image(self.img.pixbuf)

		self.ui.show()

	def _load_image(self, object, img_path):
		self.load_image(img_path)

	def load_image( self, img_path ):
		self.img = Img(GdkPixbuf.Pixbuf.new_from_file(img_path))
		self.ui.update_image(self.img.pixbuf)


#
# This presents an image held in memory.
# It holds a pixbuf instance internally, this is updated when operations are performed
# The UI will request an operation and the new pixbuf will be returned ready to be
# loaded into the image widget
#
class Img:

	def __init__(self, pixbuf):
		self.update_pixbuf(pixbuf)

	def update_pixbuf( self, pixbuf ):
		self.pixbuf = pixbuf
		self.width  = pixbuf.get_width()
		self.height = pixbuf.get_height()

	def get_pixel(self, x, y):

		if x < 0 or x > self.width - 1:
			raise IndexError('Invalid pixel')

		elif y < 0 or y > self.height - 1:
			raise IndexError('Invalid pixel')

		# find the offset into the array at which the pixel is
		offset = ((y * self.width) + x) * 4

		return bytes(self.pixbuf.get_pixels()[offset:offset + 4])

	def flip_horizontal(self):
		self.update_pixbuf(self.pixbuf.flip(True))

	def flip_vertical(self):
		self.update_pixbuf(self.pixbuf.flip(False))


# which file do we want to load?
target = None
# target = '/home/simon/Desktop/test.png'
# target = '/home/simon/Desktop/maslow.gif'
target = '/home/simon/Desktop/monkey.jpg'
# target = '/home/simon/Desktop/landscape.jpg'

# create the application and UI
app = ImgViewer(target)


pb = app.img.pixbuf;

if pb:

	print pb.get_width()
	print pb.get_height()
	# print pb.get_rowstride()
	# print pb.get_n_channels()
	# print pb.get_has_alpha()
	# print pb.get_bits_per_sample()

	# i = Img(pb.get_width(), pb.get_height(), pb.get_pixels())
	i = app.img

	print i.width

	# j = 0
	# for x in range(0, i.width - 1):
	# 	for y in range(0, i.height - 1):
	# 		px = i.get_pixel(x,y)
	# 		j=j+1

	# print j
	px = i.get_pixel(45,45)

	print 'Colour', px.encode('hex')
	print 'R', px[0].encode('hex')
	print 'G', px[1].encode('hex')
	print 'B', px[2].encode('hex')
	print 'A', px[3].encode('hex')


# Start the gtk event loop
Gtk.main()

