#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this code example, we create three toggle button widgets.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
from wx import Panel


class Example(wx.Frame):
    c_pnl: Panel
    col: wx.Colour

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):

        pnl = wx.Panel(self)

        self.col = wx.Colour(0, 0, 0)

        rtb = wx.ToggleButton(pnl, label='red', pos=(20, 25))
        gtb = wx.ToggleButton(pnl, label='green', pos=(20, 60))
        btb = wx.ToggleButton(pnl, label='blue', pos=(20, 100))

        self.c_pnl = wx.Panel(pnl, pos=(150, 20), size=(110, 110))
        self.c_pnl.SetBackgroundColour(self.col)

        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_red)
        gtb.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_green)
        btb.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_blue)

        self.SetSize((350, 250))
        self.SetTitle('Toggle buttons')
        self.Center()

    def toggle_red(self, e: wx.Event):
        obj: wx.ToggleButton = e.GetEventObject()
        is_pressed = obj.GetValue()

        green = self.col.Green()
        blue = self.col.Blue()

        if is_pressed:
            self.col.Set(255, green, blue)
        else:
            self.col.Set(0, green, blue)

        self.c_pnl.SetBackgroundColour(self.col)
        self.c_pnl.Refresh()

    def toggle_green(self, e: wx.Event):
        obj: wx.ToggleButton = e.GetEventObject()
        is_pressed = obj.GetValue()

        red = self.col.Red()
        blue = self.col.Blue()

        if is_pressed:
            self.col.Set(red, 255, blue)
        else:
            self.col.Set(red, 0, blue)

        self.c_pnl.SetBackgroundColour(self.col)
        self.c_pnl.Refresh()

    def toggle_blue(self, e: wx.Event):
        obj: wx.ToggleButton = e.GetEventObject()
        is_pressed = obj.GetValue()

        red = self.col.Red()
        green = self.col.Green()

        if is_pressed:
            self.col.Set(red, green, 255)
        else:
            self.col.Set(red, green, 0)

        self.c_pnl.SetBackgroundColour(self.col)
        self.c_pnl.Refresh()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
