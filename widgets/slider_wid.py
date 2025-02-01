#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a slider control.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):
    txt: wx.StaticText

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        pnl = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        sld = wx.Slider(pnl, value=200, minValue=150, maxValue=500, style=wx.SL_HORIZONTAL)

        sld.Bind(wx.EVT_SCROLL, self.on_slider_scroll)
        sizer.Add(sld, pos=(0, 0), flag=wx.ALL | wx.EXPAND, border=25)

        self.txt = wx.StaticText(pnl, label='200')
        sizer.Add(self.txt, pos=(0, 1), flag=wx.TOP | wx.RIGHT, border=25)

        sizer.AddGrowableCol(0)
        pnl.SetSizer(sizer)

        self.SetTitle('wx.Slider')
        self.Center()

    def on_slider_scroll(self, e: wx.CommandEvent):
        obj: wx.Slider = e.GetEventObject()
        val = obj.GetValue()

        self.txt.SetLabel(str(val))


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
