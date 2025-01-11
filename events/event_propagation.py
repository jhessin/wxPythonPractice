#!/usr/bin/env python

"""
ZetCode wxPython tutorial

This example demonstrates event propagation.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class MyPanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        super(MyPanel, self).__init__(*args, **kwargs)

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

    def on_button_clicked(self, evt: wx.Event):
        print('event reached panel class')
        evt.Skip()


class MyButton(wx.Button):
    def __init__(self, *args, **kwargs):
        super(MyButton, self).__init__(*args, **kwargs)

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

    def on_button_clicked(self, evt: wx.Event):
        print('event reached button class')
        evt.Skip()


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        mpnl = MyPanel(self)

        MyButton(mpnl, label='Ok', pos=(15, 15))

        self.Bind(wx.EVT_BUTTON, self.on_button_clicked)

        self.SetTitle('Propagate event')
        self.Center()

    def on_button_clicked(self, e: wx.Event):
        print('event reached frame class')
        e.Skip()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
