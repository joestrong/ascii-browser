#!/usr/bin/python

from gi.repository import Gtk
from subprocess import call

class BrowserWindow(Gtk.Window):

    textarea = Gtk.TextView()

    def __init__(self):
        Gtk.Window.__init__(self, title="Ascii Browser")
        vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        horiz = Gtk.Box()
        textbox = Gtk.Entry()
        button = Gtk.Button('Get Website')
        button.connect('clicked', self.request)
        horiz.add(textbox)
        horiz.add(button)
        vert.add(horiz)
        vert.add(self.textarea)
        self.add(vert)

    def request(self, widget):
        result = self.getWebData()
        self.textarea.text = result

    def getWebData(self):
        result = call(["curl", "http://www.google.com"])
        return result

win = BrowserWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()