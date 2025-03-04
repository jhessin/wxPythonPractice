#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we draw six rectangles with different pens.

author: Jan Bodnar
website: www.zetcode.com
last modified: May 2018
"""

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.Bind(wx.EVT_PAINT, self.on_paint)

        self.SetTitle('Pens')
        self.Center()

    def on_paint(self, e: wx.PaintEvent):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
        dc.DrawRectangle(10, 15, 90, 60)

        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.DOT))
        dc.DrawRectangle(130, 15, 90, 60)

        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.LONG_DASH))
        dc.DrawRectangle(250, 15, 90, 60)

        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SHORT_DASH))
        dc.DrawRectangle(10, 105, 90, 60)

        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.DOT_DASH))
        dc.DrawRectangle(130, 105, 90, 60)

        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.TRANSPARENT))
        dc.DrawRectangle(250, 105, 90, 60)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
