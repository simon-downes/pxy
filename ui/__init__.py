import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

import menu

class Commands():
	OPEN_FILE       = 1
	FLIP_HORIZONTAL = 2
	FLIP_VERTICAL   = 3

#
# This represents our main application window and the constituent parts of the UI
#
class MainWindow(Gtk.Window):
	__gsignals__ = {
		# signals emitted to inform the application of user requests from the ui

		'load_image': (GObject.SIGNAL_RUN_FIRST, None, (str,)),
		'exit': (GObject.SIGNAL_RUN_FIRST, None, ()),

		'hflip': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'vflip': (GObject.SIGNAL_RUN_FIRST, None, ()),

		'grayscale': (GObject.SIGNAL_RUN_FIRST, None, (str,)),

		'grayscale_average': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_luma': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_desaturate': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_decompose_min': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_decompose_max': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_red': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_green': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_blue': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_4': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_8': (GObject.SIGNAL_RUN_FIRST, None, ()),
		'grayscale_16': (GObject.SIGNAL_RUN_FIRST, None, ())

	}

	def __init__(self, width, height):
		Gtk.Window.__init__(self)

		# quit the gtk event loop (and therefore the app) when the window is closed/deleted
		self.connect("delete-event", Gtk.main_quit)

		# request an initial window size
		self.set_size_request(width, height)

		# create an image widget for showing our image
		self.img = Gtk.Image()

		vbox = Gtk.VBox(False, 2)

		mb = menu.MenuBar()

		mb.connect('menu_item_click', self.menu_item_click)
		# mb.connect('open_file', self.open_file)
		# mb.connect('exit', self.exit)

		vbox.pack_start(mb, False, False, 0)
		vbox.pack_start(Viewport(self.img), True, True, 0)
		vbox.pack_end(StatusBar(), False, False, 0)

		self.add(vbox)


	# update the image being viewed with the given pixbuf
	def update_image(self, pixbuf):
		self.img.set_from_pixbuf(pixbuf)

	# make everything visible
	def show(self):
		self.show_all()

	def menu_item_click(self, menubar, item):

		print item

		if item == 'open_file':
			self.open_file()

		elif item[0:9] == 'grayscale':
			self.emit('grayscale', item[10:])

		elif item in GObject.signal_list_names(MainWindow):
			self.emit(item)

	def open_file(self):

		# create a standard open FileChooserDialog with stock 'Cancel' and 'Open' buttons
		dialog = Gtk.FileChooserDialog("Open..",
			None,
			Gtk.FileChooserAction.OPEN,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

		# specify a filter for image files so user can't load any old file
		filter_text = Gtk.FileFilter()
		filter_text.set_name("Image files")
		filter_text.add_mime_type("image/gif")
		filter_text.add_mime_type("image/jpeg")
		filter_text.add_mime_type("image/png")
		dialog.add_filter(filter_text)

		# show the dialog
		response = dialog.run()

		# if user actually selects a file to open then emit the appropriate signal
		if response == Gtk.ResponseType.OK:
			self.emit("load_image", dialog.get_filename())

		# destroy/hide/dismiss the dialog
		dialog.destroy()

#
# Defines the structure of the status bar, an HBox instance with multiple Statusbar instances contained within
#
class StatusBar(Gtk.HBox):

	def __init__(self):
		Gtk.HBox.__init__(self,False, 2)

		sb1 = Gtk.Statusbar()
		context_id = sb1.get_context_id('status')
		message_id = sb1.push(context_id, 'Hello World')

		sb2 = Gtk.Statusbar()
		context_id = sb2.get_context_id('status')
		message_id = sb2.push(context_id, 'Hello Again')

		self.pack_start(sb1, False, False, 0)
		self.pack_start(sb2, False, False, 0)

# Viewport is a ScrolledWindow widget that contains the image being viewed and
# provides scrollbars automatically for when the image exceeds the window size
class Viewport(Gtk.ScrolledWindow):

	def __init__(self, img):
		Gtk.ScrolledWindow.__init__(self)

		# add the image to the viewport
		self.add_with_viewport(img)
