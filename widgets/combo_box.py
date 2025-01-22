#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a combo box

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):
    st: wx.StaticText

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        pnl = wx.Panel(self)

        distros = ['Ubuntu', 'Arch', 'Fedora', 'Debian', 'Mint']
        cb = wx.ComboBox(pnl, pos=(50, 30), choices=distros, style=wx.CB_READONLY)

        self.st = wx.StaticText(pnl, label='', pos=(50, 140))
        cb.Bind(wx.EVT_COMBOBOX, self.on_select)

        self.SetSize((250, 230))
        self.SetTitle('wx.ComboBox')
        self.Center()
        self.Show(True)

    def on_select(self, e: wx.CommandEvent):

        i = e.GetString()
        self.st.SetLabel(i)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
