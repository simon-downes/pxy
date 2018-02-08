import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class MenuItem(Gtk.MenuItem):

	def __init__(self, name, label):
		self.name = name
		Gtk.MenuItem.__init__(self, label)

#
# Defines the menu structure
#
class MenuBar(Gtk.MenuBar):
	__gsignals__ = {
 		'menu_item_click': (GObject.SIGNAL_RUN_FIRST, None, (str,)),
	}

	# File
	# 	Open...
	# 	---
	# 	Exit
	# Image
	# 	Resize Canvas...
	# 	Resize Image...
	# 	---
	# 	Flip Horizontally
	# 	Flip Vertically
	# 	---
	# 	Rotate 90 Clockwise
	# 	Rotate 90 Anti-Clockwise
	# 	Rotate...
	# Effects
	# 	Grayscale
	# 		Average
	# 		Luma
	# 		Desaturate
	# 		---
	# 		Decompose Min
	# 		Decompose Max
	# 		---
	# 		Red Channel
	# 		Green Channel
	# 		Blue Channel
	# 		---
	# 		4 Shades
	# 		8 Shades
	# 		16 Shades
	# 	Blurs
	# 		Motion
	# 		Gaussian
	# 		Radial
	# 	Dither
	# 		...
	# 	Diffuse
	# 	Sharpen
	# 	Smooth
	# 	Gamma Correction
	# 	Edge Detect
	# 	Emboss

	def __init__(self):
		Gtk.MenuBar.__init__(self)

		self.append(FileMenu(self.on_item_click))
		self.append(ImageMenu(self.on_item_click))
		self.append(EffectsMenu(self.on_item_click))

	# catch the activate signals on menu items and dispatch a specific signal
	def on_item_click(self, item):
		self.emit('menu_item_click', item.name)

class FileMenu(Gtk.MenuItem):

	def __init__(self, on_item_click):
		Gtk.MenuItem.__init__(self, "File")

		submenu = Gtk.Menu()

		open = MenuItem('open_file', "Open...")
		open.connect("activate", on_item_click)
		submenu.append(open)

		submenu.append(Gtk.SeparatorMenuItem())

		exit = MenuItem('exit', "Exit")
		exit.connect("activate", on_item_click)
		submenu.append(exit)

		self.set_submenu(submenu)

class ImageMenu(Gtk.MenuItem):

	def __init__(self, on_item_click):
		Gtk.MenuItem.__init__(self, "Image")

		submenu = Gtk.Menu()

		item = MenuItem('resize_canvas', "Resize Canvas...")
		item.connect("activate", on_item_click)
		submenu.append(item)

		item = MenuItem('resize_image', "Resize Image...")
		item.connect("activate", on_item_click)
		submenu.append(item)

		submenu.append(Gtk.SeparatorMenuItem())

		item = MenuItem('hflip', "Flip Horizontally")
		item.connect("activate", on_item_click)
		submenu.append(item)

		item = MenuItem('vflip', "Flip Vertically")
		item.connect("activate", on_item_click)
		submenu.append(item)

		submenu.append(Gtk.SeparatorMenuItem())

		item = MenuItem('rotate', "Rotate 90 Clockwise")
		item.connect("activate", on_item_click)
		submenu.append(item)

		item = MenuItem('rotate_anti', "Rotate 90 Anti-Clockwise")
		item.connect("activate", on_item_click)
		submenu.append(item)

		item = MenuItem('rotate_custom', "Rotate...")
		item.connect("activate", on_item_click)
		submenu.append(item)

		self.set_submenu(submenu)

class EffectsMenu(Gtk.MenuItem):

	def __init__(self, on_item_click):
		Gtk.MenuItem.__init__(self, "Effects")

		submenu = Gtk.Menu()

		item = Gtk.MenuItem("Grayscale")

		grayscale = Gtk.Menu()

		subitem = MenuItem('grayscale_average', "Average")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		subitem = MenuItem('grayscale_luma', "Luma")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		subitem = MenuItem('grayscale_desaturate', "Desaturate")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		grayscale.append(Gtk.SeparatorMenuItem())

		subitem = MenuItem('grayscale_decompose_min', "Decompose Min")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		subitem = MenuItem('grayscale_decompose_max', "Decompose Max")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		grayscale.append(Gtk.SeparatorMenuItem())

		subitem = MenuItem('grayscale_red', "Red Channel")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		subitem = MenuItem('grayscale_green', "Green Channel")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		subitem = MenuItem('grayscale_blue', "Blue Channel")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		grayscale.append(Gtk.SeparatorMenuItem())

		subitem = MenuItem('grayscale_shades_4', "4 Shades")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		subitem = MenuItem('grayscale_shades_8', "8 Shades")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		subitem = MenuItem('grayscale_shades_16', "16 Shades")
		subitem.connect("activate", on_item_click)
		grayscale.append(subitem)

		item.set_submenu(grayscale)

		submenu.append(item)

		self.set_submenu(submenu)
