#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program draws eight rectangles filled with different brushes.

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

        self.SetTitle('Brushes')
        self.Centre()

    def on_paint(self, e: wx.PaintEvent):
        dc = wx.PaintDC(self)

        brush = wx.Brush('#4c4c4c')

        brush.SetStyle(wx.BRUSHSTYLE_CROSS_HATCH)
        dc.SetBrush(brush)
        dc.DrawRectangle(10, 15, 90, 60)

        brush.SetStyle(wx.BRUSHSTYLE_SOLID)
        dc.SetBrush(brush)
        dc.DrawRectangle(130, 15, 90, 60)

        brush.SetStyle(wx.BRUSHSTYLE_BDIAGONAL_HATCH)
        dc.SetBrush(brush)
        dc.DrawRectangle(250, 15, 90, 60)

        brush.SetStyle(wx.BRUSHSTYLE_CROSSDIAG_HATCH)
        dc.SetBrush(brush)
        dc.DrawRectangle(10, 105, 90, 60)

        brush.SetStyle(wx.BRUSHSTYLE_FDIAGONAL_HATCH)
        dc.SetBrush(brush)
        dc.DrawRectangle(130, 105, 90, 60)

        brush.SetStyle(wx.BRUSHSTYLE_HORIZONTAL_HATCH)
        dc.SetBrush(brush)
        dc.DrawRectangle(250, 105, 90, 60)

        brush.SetStyle(wx.BRUSHSTYLE_VERTICAL_HATCH)
        dc.SetBrush(brush)
        dc.DrawRectangle(10, 195, 90, 60)

        brush.SetStyle(wx.BRUSHSTYLE_TRANSPARENT)
        dc.SetBrush(brush)
        dc.DrawRectangle(130, 195, 90, 60)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
