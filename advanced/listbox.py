#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a wx.ListBox widget.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):
    listbox: wx.ListBox

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):

        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel)
        hbox.Add(self.listbox, 9, wx.EXPAND | wx.ALL, 20)

        btn_panel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        new_btn = wx.Button(btn_panel, wx.ID_ANY, 'New', size=(90, 30))
        ren_btn = wx.Button(btn_panel, wx.ID_ANY, 'Rename', size=(90, 30))
        del_btn = wx.Button(btn_panel, wx.ID_ANY, 'Delete', size=(90, 30))
        clr_btn = wx.Button(btn_panel, wx.ID_ANY, 'Clear', size=(90, 30))

        self.Bind(wx.EVT_BUTTON, self.new_item, id=new_btn.GetId())
        self.Bind(wx.EVT_BUTTON, self.on_rename, id=ren_btn.GetId())
        self.Bind(wx.EVT_BUTTON, self.on_delete, id=del_btn.GetId())
        self.Bind(wx.EVT_BUTTON, self.on_clear, id=clr_btn.GetId())
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.on_rename)

        vbox.Add((-1, 20))
        vbox.Add(new_btn)
        vbox.Add(ren_btn, 0, wx.TOP, 5)
        vbox.Add(del_btn, 0, wx.TOP, 5)
        vbox.Add(clr_btn, 0, wx.TOP, 5)

        btn_panel.SetSizer(vbox)
        hbox.Add(btn_panel, 1, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.SetTitle('wx.ListBox')
        self.Center()

    def new_item(self, e: wx.Event):

        text = wx.GetTextFromUser('Enter a new item', 'Insert dialog')
        if text != '':
            self.listbox.Append(text)

    def on_rename(self, e: wx.Event):
        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser('Rename item', 'Rename dialog', text)

        if renamed != '':
            self.listbox.Delete(sel)
            item_id = self.listbox.Insert(renamed, sel)
            self.listbox.SetSelection(item_id)

    def on_delete(self, e: wx.Event):

        sel = self.listbox.GetSelection()
        if sel != -1:
            self.listbox.Delete(sel)

    def on_clear(self, e: wx.Event):
        self.listbox.Clear()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
