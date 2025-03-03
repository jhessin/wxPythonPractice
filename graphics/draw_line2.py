#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we draw a line in a point event

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.Bind(wx.EVT_PAINT, self.on_paint)

        self.SetTitle('Line')
        self.Center()

    def on_paint(self, e: wx.PaintEvent):
        dc = wx.PaintDC(self)
        dc.DrawLine(50, 60, 190, 60)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
