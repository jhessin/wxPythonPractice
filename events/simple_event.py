#!/usr/bin/env python

"""
ZetCode wxPython tutorial

This is a wx.MoveEvent event demonstration

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
        wx.StaticText(self, label='x: ', pos=(10, 10))
        wx.StaticText(self, label='y: ', pos=(10, 30))

        self.st1 = wx.StaticText(self, label='', pos=(30, 10))
        self.st2 = wx.StaticText(self, label='', pos=(30, 30))

        self.Bind(wx.EVT_MOVE, self.on_move)

        self.SetSize((350, 250))
        self.SetTitle('Move event')
        self.Center()

    def on_move(self, e: wx.MoveEvent):
        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
