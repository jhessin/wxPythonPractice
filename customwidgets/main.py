#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a Hyperlink using our custom widget.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
from wx.lib.stattext import GenStaticText
from hyperlink import Link


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        st = GenStaticText(panel, label='Go to web site:')
        st.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Verdana'))
        hbox.Add(st, flag=wx.LEFT, border=20)

        link_wid = Link(panel, label='ZetCode', url='http://www.zetcode.com')
        hbox.Add(link_wid, flag=wx.LEFT, border=20)

        vbox.Add(hbox, flag=wx.TOP, border=30)
        panel.SetSizer(vbox)

        self.SetTitle('A Hyperlink')
        self.Centre()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
