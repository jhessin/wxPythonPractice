#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a checkbox widget.

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

        vbox = wx.BoxSizer(wx.HORIZONTAL)

        cb = wx.CheckBox(pnl, label='Show title')
        cb.SetValue(True)
        cb.Bind(wx.EVT_CHECKBOX, self.show_or_hide_title)

        vbox.Add(cb, flag=wx.TOP | wx.LEFT, border=30)

        pnl.SetSizer(vbox)

        self.SetTitle('wx.CheckBox')
        self.Center()

    def show_or_hide_title(self, e: wx.CommandEvent):

        sender = e.GetEventObject()
        is_checked = sender.GetValue()

        if is_checked:
            self.SetTitle('wx.CheckBox')
        else:
            self.SetTitle('')


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
