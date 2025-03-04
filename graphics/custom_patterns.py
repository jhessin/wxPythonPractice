#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program draws three rectangles with custom brush patterns

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

        self.SetTitle('Custom patterns')
        self.Centre()

    def on_paint(self, e: wx.PaintEvent):
        dc = wx.PaintDC(self)

        pen = wx.Pen('#c7c3c3')
        dc.SetPen(pen)

        brush1 = wx.Brush(wx.Bitmap('pattern1.png'))
        brush2 = wx.Brush(wx.Bitmap('pattern2.png'))
        brush3 = wx.Brush(wx.Bitmap('pattern3.png'))

        dc.SetBrush(brush1)
        dc.DrawRectangle(10, 15, 90, 60)

        dc.SetBrush(brush2)
        dc.DrawRectangle(130, 15, 90, 60)

        dc.SetBrush(brush3)
        dc.DrawRectangle(250, 15, 90, 60)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
