#!/usr/bin/env python

"""
ZetCode wxPython tutorial

This example shows four types of message dialogs.

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
        panel = wx.Panel(self)

        hbox = wx.BoxSizer()
        sizer = wx.GridSizer(2, 2, 2, 2)

        btn1 = wx.Button(panel, label='Info')
        btn2 = wx.Button(panel, label='Error')
        btn3 = wx.Button(panel, label='Question')
        btn4 = wx.Button(panel, label='Alert')

        sizer.AddMany([btn1, btn2, btn3, btn4])

        hbox.Add(sizer, 0, wx.ALL, 15)
        panel.SetSizer(hbox)

        btn1.Bind(wx.EVT_BUTTON, self.show_message_1)
        btn2.Bind(wx.EVT_BUTTON, self.show_message_2)
        btn3.Bind(wx.EVT_BUTTON, self.show_message_3)
        btn4.Bind(wx.EVT_BUTTON, self.show_message_4)

        self.SetSize((300, 200))
        self.SetTitle('Message')
        self.Center()

    def show_message_1(self, _e: wx.Event):
        dial = wx.MessageDialog(self, 'Download completed', 'Info', wx.OK)
        dial.ShowModal()

    def show_message_2(self, _e: wx.Event):
        dial = wx.MessageDialog(self, 'Error loading file', 'Error', wx.OK | wx.ICON_ERROR)
        dial.ShowModal()

    def show_message_3(self, _e: wx.Event):
        dial = wx.MessageDialog(self, 'Are you sure you want to quit?', 'Question',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        dial.ShowModal()

    def show_message_4(self, _e: wx.Event):
        dial = wx.MessageDialog(self, 'Operation not allowed', 'Exclamation', wx.OK | wx.ICON_EXCLAMATION)
        dial.ShowModal()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
