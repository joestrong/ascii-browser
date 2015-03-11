#!/usr/bin/python

from gi.repository import Gtk, WebKit
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
        vert.add(self.webview)

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
        url = self.addressBar.get_text()
        #result = self.getWebData(url)
        self.webview.load_uri(url)

    def getWebData(self, url):
        result = urllib.request.urlopen(url)
        html = result.read()
        result.close()
        html = html.decode()
        return html

win = BrowserWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
