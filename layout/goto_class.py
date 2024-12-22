#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we create a Go To class layout with wx.BoxSizer.

author: Jan Bodnar
website. www.zetcode.com
last modified: July 2020
"""

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.init_ui()
        self.Center()

    def init_ui(self):

        panel = wx.Panel(self)

        font: wx.Font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)

        vbox