#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we use custom event ids.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

ID_MENU_NEW = wx.NewId()
ID_MENU_OPEN = wx.NewId()
ID_MENU_SAVE = wx.NewId()


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):

        self.create_menu_bar()
        self.CreateStatusBar()

        self.SetSize((350, 250))
        self.SetTitle('Custom ids')
        self.Center()

    def create_menu_bar(self):

        mb = wx.MenuBar()

        f_menu = wx.Menu()
        f_menu.Append(ID_MENU_NEW, 'New')
        f_menu.Append(ID_MENU_OPEN, 'Open')
        f_menu.Append(ID_MENU_SAVE, 'Save')

        mb.Append(f_menu, '&File')
        self.SetMenuBar(mb)

        self.Bind(wx.EVT_MENU, self.display_message, id=ID_MENU_NEW)
        self.Bind(wx.EVT_MENU, self.display_message, id=ID_MENU_OPEN)
        self.Bind(wx.EVT_MENU, self.display_message, id=ID_MENU_SAVE)

    def display_message(self, e: wx.MenuEvent):

        sb = self.GetStatusBar()

        eid = e.GetId()

        if eid == ID_MENU_NEW:
            msg = 'New menu item selected'
        elif eid == ID_MENU_OPEN:
            msg = 'Open menu item selected'
        elif eid == ID_MENU_SAVE:
            msg = 'Save menu item selected'

        sb.SetStatusText(msg)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
