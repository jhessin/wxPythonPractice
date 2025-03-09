#!/usr/bin/python

"""
ZetCode wxPython tutorial

This is a Hyperlink widget.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
from wx.lib.stattext import GenStaticText
import webbrowser


class Link(GenStaticText):
    font1: wx.Font
    font2: wx.Font
    url: str

    def __init__(self, *args, url='', **kwargs):
        super(Link, self).__init__(*args, **kwargs)

        self.url = url

        self.font1 = wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, True, 'Verdana')
        self.font2 = wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Verdana')

        self.SetFont(self.font2)
        self.SetForegroundColour('#0000ff')

        self.Bind(wx.EVT_MOUSE_EVENTS, self.on_mouse_event)
        self.Bind(wx.EVT_MOTION, self.on_mouse_event)

    def set_url(self, url: str):
        self.url = url

    def on_mouse_event(self, e: wx.MouseEvent):

        if e.Moving():
            self.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            self.SetFont(self.font1)
        elif e.LeftUp():
            webbrowser.open_new_tab(self.url)
        else:
            self.SetCursor(wx.NullCursor)
            self.SetFont(self.font2)

        e.Skip()
