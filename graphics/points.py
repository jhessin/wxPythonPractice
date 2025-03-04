#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program draws one thousand points randomly on the window.

author: Jan Bodnar
website: www.zetcode.com
last modified: May 2018
"""

import wx
import random


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.Bind(wx.EVT_PAINT, self.on_paint)

        self.SetTitle('Points')
        self.Centre()

    def on_paint(self, e: wx.PaintEvent):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen('RED'))

        for i in range(1000):
            w, h = self.GetSize()
            x = random.randint(1, w - 1)
            y = random.randint(1, h - 1)
            dc.DrawPoint(x, y)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
