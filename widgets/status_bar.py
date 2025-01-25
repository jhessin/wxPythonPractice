#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we do something awesome.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""
from random import choices

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):

        pnl = wx.Panel(self)

        button = wx.Button(pnl, label='Button', pos=(20, 20))
        text = wx.CheckBox(pnl, label='CheckBox', pos=(20, 90))
        combo = wx.ComboBox(pnl, pos=(120, 22), choices=['Python', 'Ruby'])
        slider = wx.Slider(pnl, 5, 6, 1, 10, (120, 90), (110, -1))
        
        pnl.Bind(wx.EVT_ENTER_WINDOW, self.on_widget_enter)
        button.Bind(wx.EVT_ENTER_WINDOW, self.on_widget_enter)
        text.Bind(wx.EVT_ENTER_WINDOW, self.on_widget_enter)
        combo.Bind(wx.EVT_ENTER_WINDOW, self.on_widget_enter)

    def on_widget_enter(self, e: wx.CommandEvent):
        pass


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
