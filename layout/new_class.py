#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we create a new class layout with wx.GridBagSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
from wx import Panel, GridBagSizer, StaticText
from wx.lib.sized_controls import border


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.init_ui()
        self.Center()

    def init_ui(self):

        panel: Panel = wx.Panel(self)

        sizer: GridBagSizer = wx.GridBagSizer(5, 5)

        text1: StaticText = wx.StaticText(panel, label='Java Class')
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('exec.png'))
        sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT, border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5), flag=wx.EXPAND|wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label='Name')
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)

        text3 = wx.StaticText(panel, label='Package')
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)

        button1 = wx.Button(panel, label='Browse...')
        sizer.Add(button1, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)

        text4 = wx.StaticText(panel, label='Extends')
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)

        combo = wx.ComboBox(panel)
        sizer.Add(combo, pos=(4, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)

        button2 = wx.Button(panel, label='Browse...')
        sizer.Add(button2, pos=(4, 4), flag=wx.TOP|wx.RIGHT, border=5)

        sb = wx.StaticBox(panel, label='Optional Attributes')

        box_sizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        box_sizer.Add(wx.CheckBox(panel, label='Public'),
                     flag=wx.LEFT|wx.TOP, border=5)
        box_sizer.Add(wx.CheckBox(panel, label='Generate Default Constructor'),
                     flag=wx.LEFT, border=5)
        box_sizer.Add(wx.CheckBox(panel, label='Generate Main Method'),
             flag=wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(box_sizer, pos=(5, 0), span=(1, 5),
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=10)

        button3 = wx.Button(panel, label='Help')
        sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)

        button4 = wx.Button(panel, label='Ok')
        sizer.Add(button4, pos=(7, 3))

        button5 = wx.Button(panel, label='Cancel')
        sizer.Add(button5, pos=(7, 4), span=(1, 1),
                  flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)


def main():

    app = wx.App()
    ex = Example(None, title='Create Java Class')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()