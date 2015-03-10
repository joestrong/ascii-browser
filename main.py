#!/usr/bin/python

from gi.repository import Gtk
from subprocess import call
import urllib.request

class BrowserWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Ascii Browser")
        self.set_default_size(500, 400)
        vert = Gtk.VBox()

        topBar = self.buildTopBar()
        vert.add(topBar)

        self.textarea = Gtk.Label()
        self.textarea.set_text("Blank")
        vert.add(self.textarea)

        self.add(vert)

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
        result = self.getWebData(self.addressBar.get_text())
        self.textarea.set_text(result)

    def getWebData(self, url):
        result = urllib.request.urlopen(url)
        html = result.read()
        html = str(html)
        return html

win = BrowserWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()