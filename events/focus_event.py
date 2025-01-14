#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we work with wx.FocusEvent.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class MyWindow(wx.Panel):

    def __init__(self, parent):
        super(MyWindow, self).__init__(parent)

        self.color = '#b3b3b3'

        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_SET_FOCUS, self.on_set_focus)
        self.Bind(wx.EVT_KILL_FOCUS, self.on_kill_focus)

    def on_paint(self, _e: wx.PaintEvent):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen(self.color))
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)

    def on_size(self, _e: wx.SizeEvent):
        self.Refresh()

    def on_set_focus(self, _e: wx.FocusEvent):
        self.color = '#ff0000'
        self.Refresh()

    def on_kill_focus(self, _e: wx.FocusEvent):
        self.color = '#b3b3b3'
        self.Refresh()


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([
            (MyWindow(self), 0, wx.EXPAND | wx.TOP | wx.LEFT, 9),
            (MyWindow(self), 0, wx.EXPAND | wx.TOP | wx.RIGHT, 9),
            (MyWindow(self), 0, wx.EXPAND | wx.BOTTOM | wx.LEFT, 9),
            (MyWindow(self), 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT, 9),
        ])

        self.SetSizer(grid)

        self.SetSize((350, 250))
        self.SetTitle('Focus event')
        self.Center()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
