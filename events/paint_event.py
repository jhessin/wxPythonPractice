#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we count paint events.

author Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):

    count: int = 0

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.Bind(wx.EVT_PAINT, self.on_paint)

        self.SetTitle('Paint events')
        self.SetSize((350, 250))
        self.Center()

    def on_paint(self, _e):
        self.count += 1
        dc = wx.PaintDC(self)
        # text = f"Number of paint events: {self.count}"
        text = f"{self.count} paint events generated"
        dc.Clear()
        dc.DrawText(text, 20, 20)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
