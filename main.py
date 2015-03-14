#!/usr/bin/python

from gi.repository import Gtk

import topbar
import asciiview

class BrowserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ascii Browser")
        self.set_default_size(500, 400)
        self.vert = Gtk.VBox()

        self.topBar = topbar.TopBar()
        self.vert.add(self.topBar)
        self.topBar.button.connect('clicked', self.request)

        self.webview = asciiview.AsciiView()
        self.vert.add(self.webview)
        self.add(self.vert)

    def request(self, widget):
        uri = self.topBar.get_url()
        self.webview.get_url(uri)

win = BrowserWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()