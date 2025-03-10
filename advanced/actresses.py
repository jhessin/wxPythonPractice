#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a simple wx.ListCtrl widget.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

data = [
    ('Jessica Alba', 'Pomona', '1981'),
    ('Sigourney Weaver', 'New York', '1949'),
    ('Angelina Jolie', 'Los Angeles', '1975'),
    ('Natalie Portman', 'Jerusalem', '1981'),
    ('Rachel Weiss', 'London', '1971'),
    ('Scarlett Johansson', 'New York', '1984'),
]


class Example(wx.Frame):
    list: wx.ListCtrl

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self)

        self.list = wx.ListCtrl(panel, wx.ID_ANY, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'name', width=140)
        self.list.InsertColumn(1, 'place', width=130)
        self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

        idx = 0

        for i in data:
            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])
            idx += 1

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.SetTitle('Actresses')
        self.Center()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
