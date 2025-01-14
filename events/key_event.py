#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we work with wx.KeyEvent.

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
        pnl.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        pnl.SetFocus()

        self.SetSize((350, 250))
        self.SetTitle('Key event')
        self.Center()

    def on_key_down(self, e: wx.KeyEvent):
        key = e.GetKeyCode()

        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox('Are you sure you want to quit?', 'Question', wx.YES_NO | wx.NO_DEFAULT, self)

            if ret == wx.YES:
                self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
