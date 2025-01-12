#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we create buttons with standard ids.

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
        pnl = wx.Panel(self)
        grid = wx.GridSizer(2)

        grid.AddMany([
            (wx.Button(pnl, wx.ID_CANCEL), 0, wx.TOP | wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_DELETE), 0, wx.TOP, 9),
            (wx.Button(pnl, wx.ID_SAVE), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_EXIT)),
            (wx.Button(pnl, wx.ID_STOP), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_NEW)),
        ])

        self.Bind(wx.EVT_BUTTON, self.on_quit_app, id=wx.ID_EXIT)

        pnl.SetSizer(grid)
        self.SetTitle('Standard ids')
        self.Center()

    def on_quit_app(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
