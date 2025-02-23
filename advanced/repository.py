#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a checklist control widget

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin

packages = [
    ('abiword', '5.8M', 'base'),
    ('adie', '145k', 'base'),
    ('airsnort', '71k', 'base'),
    ('ara', '717k', 'base'),
    ('arc', '139k', 'base'),
    ('asc', '5.8M', 'base'),
    ('ascii', '74k', 'base'),
    ('ash', '74k', 'base'),
]


class CheckListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):

    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        ListCtrlAutoWidthMixin.__init__(self)


class Example(wx.Frame):
    log: wx.TextCtrl
    list: CheckListCtrl

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        left_panel = wx.Panel(panel)
        right_panel = wx.Panel(panel)

        self.log = wx.TextCtrl(right_panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.list = CheckListCtrl(right_panel)
        self.list.EnableCheckBoxes()
        self.list.InsertColumn(0, 'Package', width=140)
        self.list.InsertColumn(1, 'Size')
        self.list.InsertColumn(2, 'Repository')

        idx = 0

        for i in packages:
            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])
            idx += 1

        vbox2 = wx.BoxSizer(wx.VERTICAL)

        sel_btn = wx.Button(left_panel, label='Select All')
        des_btn = wx.Button(left_panel, label='Deselect All')
        app_btn = wx.Button(left_panel, label='Apply')

        self.Bind(wx.EVT_BUTTON, self.on_select_all, id=sel_btn.GetId())
        self.Bind(wx.EVT_BUTTON, self.on_deselect_all, id=des_btn.GetId())
        self.Bind(wx.EVT_BUTTON, self.on_apply, id=app_btn.GetId())

        vbox2.Add(sel_btn, 0, wx.TOP | wx.BOTTOM, 5)
        vbox2.Add(des_btn, 0, wx.BOTTOM, 5)
        vbox2.Add(app_btn)

        left_panel.SetSizer(vbox2)

        vbox.Add(self.list, 4, wx.EXPAND | wx.TOP, 3)
        vbox.Add((-1, 10))
        vbox.Add(self.log, 1, wx.EXPAND)
        vbox.Add((-1, 10))

        right_panel.SetSizer(vbox)

        hbox.Add(left_panel, 0, wx.EXPAND | wx.RIGHT, 5)
        hbox.Add(right_panel, 1, wx.EXPAND)
        hbox.Add((3, -1))

        panel.SetSizer(hbox)

        self.SetTitle('Repository')
        self.Center()

    def on_select_all(self, e):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i)

    def on_deselect_all(self, e):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i, False)

    def on_apply(self, e):

        num = self.list.GetItemCount()

        for i in range(num):
            if i == 0: self.log.Clear()

            if self.list.IsItemChecked(i):
                self.log.AppendText(self.list.GetItemText(i) + '\n')


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
