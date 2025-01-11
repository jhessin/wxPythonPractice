#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we use automatic ids
with wx.ID_ANY.

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
        exitButton = wx.Button(pnl, wx.ID_ANY, 'Exit', (10, 10))

        self.Bind(wx.EVT_BUTTON, self.on_exit, id=exitButton.GetId())

        self.SetTitle('Automatic ids')
        self.Center()

    def on_exit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
