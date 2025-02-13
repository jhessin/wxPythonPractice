#!/usr/bin/env python

"""
ZetCode wxPython tutorial

This example creates a checked
menu item.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):
    statusbar: wx.StatusBar
    shtl: wx.MenuItem
    shst: wx.MenuItem
    toolbar: wx.ToolBar

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        viewMenu = wx.Menu()

        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar', 'Show Statusbar', kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 'Show toolbar', kind=wx.ITEM_CHECK)

        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        self.toolbar = self.CreateToolBar()
        # self.toolbar.AddTool(1, '', wx.Bitmap('texit.png'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        self.SetSize((450, 350))
        self.SetTitle('Check menu item')
        self.Center()

    def ToggleStatusBar(self, e):
        if self.shst.IsChecked():
            self.statusbar.Show(True)
            self.SetStatusBar(self.statusbar)
        else:
            self.statusbar.Show(False)
            self.SetStatusBar(None)

    def ToggleToolBar(self, e):
        if self.shtl.IsChecked():
            self.toolbar.Show(True)
            self.SetToolBar(self.toolbar)
        else:
            self.toolbar.Show(False)
            self.SetToolBar(None)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
