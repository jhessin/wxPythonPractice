#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this code example, we create three toggle button widgets.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):

        pnl = wx.Panel(self)
