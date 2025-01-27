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
    sb: wx.StatusBar

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
        slider.Bind(wx.EVT_ENTER_WINDOW, self.on_widget_enter)

        self.sb = self.CreateStatusBar()

        self.SetSize((250, 230))
        self.SetTitle('wx.Statusbar')
        self.Center()
        self.Show(True)

    def on_widget_enter(self, e: wx.CommandEvent):
        name = e.GetEventObject().GetClassName()
        self.sb.SetStatusText(name + ' widget')
        e.Skip()


def main():
    app = wx.App()
    ex = Example(None)
    app.MainLoop()


if __name__ == '__main__':
    main()
