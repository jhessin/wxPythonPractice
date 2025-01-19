#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this code example, we create a custom dialog.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class ChangeDepthDialog(wx.Dialog):

    def __init__(self, *args, **kwargs):
        super(ChangeDepthDialog, self).__init__(*args, **kwargs)

        self.init_ui()
        self.SetSize((250, 200))
        self.SetTitle('Change Color Depth')

    def init_ui(self):

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sb = wx.StaticBox(pnl, label='Colors')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(wx.RadioButton(pnl, label='256 Colors', style=wx.RB_GROUP))
        sbs.Add(wx.RadioButton(pnl, label='16 Colors'))
        sbs.Add(wx.RadioButton(pnl, label='2 Colors'))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.RadioButton(pnl, label='Custom'))
        hbox1.Add(wx.TextCtrl(pnl), flag=wx.LEFT, border=5)
        sbs.Add(hbox1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(self, label='Ok')
        close_button = wx.Button(self, label='Close')
        hbox2.Add(ok_button)
        hbox2.Add(close_button, flag=wx.LEFT, border=5)

        vbox.Add(pnl, proportion=1,
                 flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        ok_button.Bind(wx.EVT_BUTTON, self.on_close)
        close_button.Bind(wx.EVT_BUTTON, self.on_close)

    def on_close(self, e: wx.Event):
        self.Destroy()