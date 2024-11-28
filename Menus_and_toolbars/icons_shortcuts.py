#!/usr/bin/env python
"""
ZetCode wxPython tutorial

In this example, we manually create a menu item.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

APP_EXIT = 1


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, "&Quit\tCtrl+Q")
        # qmi.SetBitmap(wx.Bitmap("exit.png"))
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        self.SetSize(350, 250)
        self.SetTitle("Icons and shortcuts")
        self.Center()

    def OnQuit(self, e):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
# end main
