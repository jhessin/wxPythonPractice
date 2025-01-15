#!/usr/bin/env python

"""
ZetCode wxPython tutorial

This example shows a simple message box.

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
        wx.CallLater(3000, self.show_message)

        self.SetSize((300, 200))
        self.SetTitle('Message box')
        self.Center()

    def show_message(self):
        wx.MessageBox('Download completed', 'Info',
                      wx.OK | wx.ICON_INFORMATION)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
