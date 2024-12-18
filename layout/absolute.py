#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example, we lay out widgets using absolute positioning.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
from wx import Panel, StaticBitmap


class Example(wx.Frame):
    rotunda: StaticBitmap
    bardejov: StaticBitmap
    mincol: StaticBitmap
    panel: Panel

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(350, 300))

        self.InitUI()
        self.Center()

    def InitUI(self):
        self.panel = wx.Panel(self)

        self.panel.SetBackgroundColour('gray')

        self.LoadImages()

        self.mincol.SetPosition((20, 20))
        self.bardejov.SetPosition((40, 160))
        self.rotunda.SetPosition((170, 50))

    def LoadImages(self):
        self.mincol = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap('mincol.jpg', wx.BITMAP_TYPE_ANY))
        self.bardejov = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap('bardejov.jpg', wx.BITMAP_TYPE_ANY))
        self.rotunda = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap('rotunda.jpg', wx.BITMAP_TYPE_ANY))


def main():
    app = wx.App()
    ex = Example(None, title='Absolute Positioning')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
