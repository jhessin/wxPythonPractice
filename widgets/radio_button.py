#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a wx.RadioButton

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):
    sb: wx.StatusBar

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        pnl = wx.Panel(self)

        self.rb1 = wx.RadioButton(pnl, label='Value A', pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(pnl, label='Value B', pos=(10, 30))
        self.rb3 = wx.RadioButton(pnl, label='Value C', pos=(10, 50))

        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.set_val)
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.set_val)
        self.rb3.Bind(wx.EVT_RADIOBUTTON, self.set_val)

        self.sb = self.CreateStatusBar(3)

        self.sb.SetStatusText("True", 0)
        self.sb.SetStatusText("False", 1)
        self.sb.SetStatusText("False", 2)

        self.SetSize((210, 210))
        self.SetTitle('wx.RadioButton')
        self.Center()
        self.Show(True)

    def set_val(self, e: wx.CommandEvent):
        state1 = str(self.rb1.GetValue())
        state2 = str(self.rb2.GetValue())
        state3 = str(self.rb3.GetValue())

        self.sb.SetStatusText(state1, 0)
        self.sb.SetStatusText(state2, 1)
        self.sb.SetStatusText(state3, 2)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
