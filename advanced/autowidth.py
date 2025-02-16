#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we use wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin
with a wx.ListBox.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
import wx.lib.mixins.listctrl

data = [
    ('Jessica Alba', 'Pomona', '1981'),
    ('Sigourney Weaver', 'New York', '1949'),
    ('Angelina Jolie', 'Los Angeles', '1975'),
    ('Natalie Portman', 'Jerusalem', '1981'),
    ('Rachel Weiss', 'London', '1971'),
    ('Scarlett Johansson', 'New York', '1984'),
]


class AutoWidthListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin):

    def __init__(self, parent, *args, **kwargs):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
        wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin.__init__(self)


class Example(wx.Frame):
    list: AutoWidthListCtrl

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self)

        self.list = AutoWidthListCtrl(panel)
        self.list.InsertColumn(0, 'name', width=140)
        self.list.InsertColumn(1, 'place', width=130)
        self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

        for idx in range(0, len(data)):
            i = data[idx]
            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])

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
