#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program draws various shapes on the window.

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

        self.SetTitle('Shapes')
        self.Centre()

    def on_paint(self, e: wx.PaintEvent):
        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush('#777'))
        dc.SetPen(wx.Pen('#777'))

        dc.DrawEllipse(20, 20, 90, 60)
        dc.DrawRoundedRectangle(130, 20, 90, 60, 10)
        dc.DrawArc(240, 40, 340, 40, 290, 20)

        dc.DrawRectangle(20, 120, 80, 50)
        dc.DrawPolygon(((130, 140), (180, 170), (180, 140), (220, 110), (140, 100)))
        dc.DrawSpline(((240, 170), (280, 170), (285, 110), (325, 110)))

        dc.DrawLines(((20, 260), (100, 260), (20, 210), (100, 210)))
        dc.DrawCircle(170, 230, 35)
        dc.DrawRectangle(250, 200, 60, 60)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
