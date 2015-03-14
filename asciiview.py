#!/usr/bin/python

from gi.repository import Gtk, Gdk, WebKit

class AsciiView(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self)

        self.webview = WebKit.WebView()
        self.webview.connect("notify::load-status", self.render_image)
        self.add(self.webview)

        self.imageview = Gtk.Image()
        self.add(self.imageview)

    def get_url(self, uri):
        self.webview.load_uri(uri)

    def render_image(self, web_view, property_type):
        if(web_view.get_load_status() == WebKit.LoadStatus.FINISHED):
            width = self.webview.get_allocation().width
            height = self.webview.get_allocation().height
            gdkwin = self.webview.get_window()

            pixbuf = Gdk.pixbuf_get_from_window(gdkwin, 0, 0, width, height)
            self.imageview.set_from_pixbuf(pixbuf)