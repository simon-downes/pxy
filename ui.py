import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject

#
# This represents our main application window and the constituent parts of the UI
#
class MainWindow(Gtk.Window):
	__gsignals__ = {
		'load_image': (GObject.SIGNAL_RUN_FIRST, None, (str,))
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
		
		mb = MenuBar()

		mb.connect('open_image', self.open_image)

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

	def open_image(self, object, img_path):
		print img_path
		self.emit("load_image", img_path)

class MenuBar(Gtk.MenuBar):
	__gsignals__ = {
		'open_image': (GObject.SIGNAL_RUN_FIRST, None, (str,))
	}

	def __init__(self):
		Gtk.MenuBar.__init__(self)

		filemenu = Gtk.Menu()
		filem = Gtk.MenuItem("File")
		filem.set_submenu(filemenu)

		open = Gtk.MenuItem("Open...")
		open.connect("activate", self.on_open_click)
		filemenu.append(open)

		filemenu.append(Gtk.SeparatorMenuItem())

		exit = Gtk.MenuItem("Exit")
		exit.connect("activate", Gtk.main_quit)
		filemenu.append(exit)

		self.append(filem)

	def on_open_click(self, widget):
		dialog = Gtk.FileChooserDialog("Open..",
			None,
			Gtk.FileChooserAction.OPEN,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		
		filter_text = Gtk.FileFilter()
		filter_text.set_name("Image files")
		filter_text.add_mime_type("image/gif")
		filter_text.add_mime_type("image/jpeg")
		filter_text.add_mime_type("image/png")
		dialog.add_filter(filter_text)

		response = dialog.run()

		if response == Gtk.ResponseType.OK:
			self.emit("open_image", dialog.get_filename())

		dialog.destroy()

class StatusBar(Gtk.Statusbar):

	def __init__(self):
		Gtk.Statusbar.__init__(self)

		context_id = self.get_context_id('status')
		message_id = self.push(context_id, 'Hello World')


# viewpoer is a scrolled window widget that contains the image being viewed and
# provides scrollbars automatically for when the image exceeds the window size
class Viewport(Gtk.ScrolledWindow):

	def __init__(self, img):
		Gtk.ScrolledWindow.__init__(self)

		# add the image to the viewport
		self.add_with_viewport(img)
