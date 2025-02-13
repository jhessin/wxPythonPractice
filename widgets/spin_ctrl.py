#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a spin control.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):
    celsius: wx.StaticText
    sc: wx.SpinCtrl

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        pnl = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        st1 = wx.StaticText(pnl, label='Convert Fahrenheit temperature to Celsius')
        sizer.Add(st1, pos=(0, 0), span=(1, 2), flag=wx.ALL, border=15)

        st2 = wx.StaticText(pnl, label='Fahrenheit:')
        sizer.Add(st2, pos=(1, 0), flag=wx.ALL | wx.ALIGN_CENTER, border=15)

        self.sc = wx.SpinCtrl(pnl, value='0')
        self.sc.SetRange(-459, 1000)

        sizer.Add(self.sc, pos=(1, 1), flag=wx.ALIGN_CENTER)

        st3 = wx.StaticText(pnl, label='Celsius:')
        sizer.Add(st3, pos=(2, 0), flag=wx.ALL | wx.ALIGN_RIGHT, border=15)

        self.celsius = wx.StaticText(pnl, label='')
        sizer.Add(self.celsius, pos=(2, 1), flag=wx.ALL, border=15)

        compute_button = wx.Button(pnl, label='Compute')
        compute_button.SetFocus()
        sizer.Add(compute_button, pos=(3, 0), flag=wx.ALIGN_RIGHT | wx.TOP, border=30)

        close_button = wx.Button(pnl, label='Close')
        sizer.Add(close_button, pos=(3, 1), flag=wx.ALIGN_LEFT | wx.TOP, border=30)

        compute_button.Bind(wx.EVT_BUTTON, self.on_compute)
        # self.sc.Bind(wx.EVT_SPIN, self.on_compute)
        close_button.Bind(wx.EVT_BUTTON, self.on_close)

        pnl.SetSizer(sizer)

        self.SetTitle('wx.SpinCtrl')
        self.Center()

    def on_compute(self, e: wx.SpinEvent):
        fahr = self.sc.GetValue()
        cels = round((fahr - 32) * 5 / 9.0, 2)
        self.celsius.SetLabel(str(cels))

    def on_close(self, e: wx.Event):
        self.Close(True)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
