#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we create a rename layout with wx.GridBagSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
from wx import Panel, GridBagSizer, StaticText, TextCtrl, Button


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.init_ui()
        self.Center()

    def init_ui(self):
        panel: Panel = wx.Panel(self)
        sizer: GridBagSizer = wx.GridBagSizer(4, 4)

        text: StaticText = wx.StaticText(panel, label='Rename To')
        sizer.Add(text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        tc: TextCtrl = wx.TextCtrl(panel)
        sizer.Add(tc, pos=(1, 0), span=(1, 5),
                  flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        button_ok: Button = wx.Button(panel, label='Ok', size=(90, 28))
        button_close: Button = wx.Button(panel, label='Close', size=(90, 28))
        sizer.Add(button_ok, pos=(3,3))
        sizer.Add(button_close, pos=(3,4), flag=wx.RIGHT | wx.BOTTOM, border=10)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizer(sizer)


def main():

    app = wx.App()
    ex = Example(None, title='Rename')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
