#!/usr/bin/python

from gi.repository import Gtk

class TopBar(Gtk.HeaderBar):

    def __init__(self):
        Gtk.HeaderBar.__init__(self)

        self.addressBar = Gtk.Entry()
        self.addressBar.set_text('http://www.google.com')

        self.button = Gtk.Button('Get Website')

        self.pack_start(self.addressBar)
        self.pack_end(self.button)

    def get_url(self):
    	return self.addressBar.get_text()