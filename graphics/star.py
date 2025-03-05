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

        points = ((wx.Point(0, 85), wx.Point(75, 75), wx.Point(100, 10), wx.Point(125, 75), wx.Point(200, 85),
                   wx.Point(150, 125), wx.Point(160, 190), wx.Point(100, 150), wx.Point(40, 190), wx.Point(50, 125)))

        region = wx.Region(points)
        dc.SetDeviceClippingRegion(region)

        radius = hypot(size_x / 2, size_y / 2)
        angle = 0

        while angle < 2 * pi:
            x = math.floor(radius * cos(angle))
            y = math.floor(radius * sin(angle))
            dc.DrawLine(wx.Point(0, 0), wx.Point(x, y))
            angle = angle + 2 * pi / 360

        dc.DestroyClippingRegion()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
