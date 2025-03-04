#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we draw nine coloured rectangles on the window.

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

        self.SetTitle('Colours')
        self.Center()

    def on_paint(self, e: wx.PaintEvent):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen('#d4d4d4'))

        dc.SetBrush(wx.Brush('#c56c00'))
        dc.DrawRectangle(10, 15, 90, 60)

        dc.SetBrush(wx.Brush('#1ac500'))
        dc.DrawRectangle(130, 15, 90, 60)

        dc.SetBrush(wx.Brush('#539e47'))
        dc.DrawRectangle(250, 15, 90, 60)

        dc.SetBrush(wx.Brush('#004fc5'))
        dc.DrawRectangle(10, 105, 90, 60)

        dc.SetBrush(wx.Brush('#c50024'))
        dc.DrawRectangle(130, 105, 90, 60)

        dc.SetBrush(wx.Brush('#9e4757'))
        dc.DrawRectangle(250, 105, 90, 60)

        dc.SetBrush(wx.Brush('#5f3b00'))
        dc.DrawRectangle(10, 195, 90, 60)

        dc.SetBrush(wx.Brush('#4c4c4c'))
        dc.DrawRectangle(130, 195, 90, 60)

        dc.SetBrush(wx.Brush('#785f36'))
        dc.DrawRectangle(250, 195, 90, 60)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
