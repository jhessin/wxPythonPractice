#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we draw a line on the frame window after a while.

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
        # wx.CallLater(2000, self.draw_line)
        wx.FutureCall(2000, self.draw_line)

        self.SetTitle('Line')
        self.Center()

    def draw_line(self):
        dc = wx.ClientDC(self)
        dc.DrawLine(50, 60, 190, 60)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
