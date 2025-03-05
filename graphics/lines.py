#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program draws various shapes on the window.

author: Jan Bodnar
website: www.zetcode.com
last modified: May 2018
"""

import wx
from math import hypot, sin, cos, pi


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.Bind(wx.EVT_PAINT, self.on_paint)

        self.SetTitle('Lines')
        self.Centre()

    def on_paint(self, e: wx.PaintEvent):
        dc = wx.PaintDC(self)
        size_x, size_y = self.GetClientSize()
        dc.SetPen(wx.Pen('#0000ff'))
        dc.SetDeviceOrigin(int(size_x / 2), int(size_y / 2))

        radius = hypot(size_x / 2, size_y / 2)
        angle = 0

        while angle < 2 * pi:
            x = int(radius * cos(angle))
            y = int(radius * sin(angle))
            dc.DrawLine(wx.Point(0, 0), wx.Point(x, y))
            angle = angle + 2 * pi / 360


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
