#!/usr/bin/python

from gi.repository import Gtk, WebKit, Gdk
from subprocess import call
import urllib.request

class BrowserWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Ascii Browser")
        self.set_default_size(500, 400)
        self.vert = Gtk.VBox()

        topBar = self.buildTopBar()
        self.vert.add(topBar)

        self.webview = WebKit.WebView()
        self.imageview = Gtk.Image()
        self.vert.add(self.webview)
        self.vert.add(self.imageview)

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
        self.getScreenshot(uri)

    def getScreenshot(self, uri):
        self.webview.load_uri(uri)

        width = self.webview.get_allocation().width
        height = self.webview.get_allocation().height
        gdkwin = self.webview.get_window()
        pixbuf = Gdk.pixbuf_get_from_window(gdkwin, 0, 0, width, height)
        self.imageview.set_from_pixbuf(pixbuf)

win = BrowserWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
