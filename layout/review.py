#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we create review layout with wx.FlexGridSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
from wx import Panel, BoxSizer, FlexGridSizer


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.init_ui()
        self.Center()
        self.Show()

    def init_ui(self):
        panel: Panel = wx.Panel(self)

        hbox: BoxSizer = wx.BoxSizer(wx.HORIZONTAL)

        fgs: FlexGridSizer = wx.FlexGridSizer(3, 2, 9, 25)

        title = wx.StaticText(panel, label='Title')
        author = wx.StaticText(panel, label='Author')
        review = wx.StaticText(panel, label='Review')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        fgs.AddMany([
            title,
            (tc1, 1, wx.EXPAND),
            author,
            (tc2, 1, wx.EXPAND),
            (review, 1, wx.EXPAND),
            (tc3, 1, wx.EXPAND),
        ])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)


def main():
    app = wx.App()
    ex = Example(None, title='Review')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
