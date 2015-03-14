#!/usr/bin/python

from gi.repository import Gtk

import asciiview

class BrowserWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Ascii Browser")
        self.set_default_size(500, 400)
        self.vert = Gtk.VBox()
        topBar = self.buildTopBar()
        self.vert.add(topBar)

        self.webview = asciiview.AsciiView()
        self.vert.add(self.webview)
        self.add(self.vert)

    def buildTopBar(self):
        topBar = Gtk.HeaderBar()
        self.addressBar = Gtk.Entry()
        self.addressBar.set_text('http://www.google.com')
        button = Gtk.Button('Get Website')
        button.connect('clicked', self.request)
        topBar.pack_start(self.addressBar)
        topBar.pack_end(button)
        return topBar

    def request(self, widget):
        uri = self.addressBar.get_text()
        self.webview.get_url(uri)

win = BrowserWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
