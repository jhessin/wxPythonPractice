#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we draw using different joins and caps.

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

        self.SetTitle('Joins and caps')
        self.Center()

    def on_paint(self, e: wx.PaintEvent):
        dc = wx.PaintDC(self)

        pen = wx.Pen('#4c4c4c', 10, wx.SOLID)

        pen.SetJoin(wx.JOIN_MITER)
        dc.SetPen(pen)
        dc.DrawRectangle(15, 15, 80, 50)

        pen.SetJoin(wx.JOIN_BEVEL)
        dc.SetPen(pen)
        dc.DrawRectangle(125, 15, 80, 50)

        pen.SetJoin(wx.JOIN_ROUND)
        dc.SetPen(pen)
        dc.DrawRectangle(235, 15, 80, 50)

        pen.SetCap(wx.CAP_BUTT)
        dc.SetPen(pen)
        dc.DrawLine(30, 150, 150, 150)

        pen.SetCap(wx.CAP_PROJECTING)
        dc.SetPen(pen)
        dc.DrawLine(30, 190, 150, 190)

        pen.SetCap(wx.CAP_ROUND)
        dc.SetPen(pen)
        dc.DrawLine(30, 230, 150, 230)

        pen2 = wx.Pen('#4c4c4c', 1, wx.SOLID)
        dc.SetPen(pen2)
        dc.DrawLine(30, 130, 30, 250)
        dc.DrawLine(150, 130, 150, 250)
        dc.DrawLine(155, 130, 155, 250)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
