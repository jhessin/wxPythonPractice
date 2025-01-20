#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this code example, we create a button widget.

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
        close_button = wx.Button(pnl, label='Close', pos=(20, 20))

        close_button.Bind(wx.EVT_BUTTON, self.on_close)

        self.SetSize((350, 250))
        self.SetTitle('wx.Button')
        self.Center()

    def on_close(self, e: wx.Event):

        self.Close(True)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
