#!/usr/bin/env python

import wx

"""
ZetCode wxPython tutorial

In this example we veto an event.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):

        self.Bind(wx.EVT_CLOSE, self.on_close_window)

        self.SetTitle('Event veto')
        self.Center()

    def on_close_window(self, e: wx.CloseEvent):
        dial = wx.MessageDialog(None, 'Are you sure you want to quit?', 'Question',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            e.Veto()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
