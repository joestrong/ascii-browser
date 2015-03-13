#!/usr/bin/python

from gi.repository import Gtk, WebKit, Gdk
from subprocess import call
import urllib.request

class BrowserWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Ascii Browser")
        self.set_default_size(500, 400)
        vert = Gtk.VBox()

        topBar = self.buildTopBar()
        vert.add(topBar)

        self.webview = WebKit.WebView()
        self.imageview = Gtk.Image()
        vert.add(self.imageview)

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
        uri = self.addressBar.get_text()
        self.getScreenshot(uri)

    def getScreenshot(self, uri):
        self.webview.load_uri(uri)
        #self.webview.wait_load()

        width, height = self.get_size()
        gdkwin = Gdk.get_default_root_window()
        pixbuf = Gdk.pixbuf_get_from_window(gdkwin, 0, 0, width, height)
        self.imageview.set_from_pixbuf(pixbuf)

win = BrowserWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
