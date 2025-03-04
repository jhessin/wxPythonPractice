#!/usr/bin/env python

"""
ZetCode wxPython tutorial

This program demonstrates a clipping operation
when drawing a star object.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""
import math

import wx
from math import hypot, sin, cos, pi


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        self.Bind(wx.EVT_PAINT, self.on_paint)

        self.SetTitle("Star")
        self.Centre()

    def on_paint(self, e):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen('#424242'))
        size_x, size_y = self.GetClientSize()
        dc.SetDeviceOrigin(math.floor(size_x / 2), math.floor(size_y / 2))

        points = (((0, 85), (75, 75), (100, 10), (125, 75), (200, 85),
                   (150, 125), (160, 190), (100, 150), (40, 190), (50, 125)))

        region = wx.Region(points)
        dc.SetDeviceClippingRegion(region)

        radius = hypot(size_x / 2, size_y / 2)
        angle = 0

        while angle < 2 * pi:
            x = radius * cos(angle)
            y = radius * sin(angle)
            dc.DrawLine((0, 0), (x, y))
            angle = angle + 2 * pi / 360

        dc.DestroyClippingRegion()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
