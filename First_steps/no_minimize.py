#!/usr/bin/env python
"""
    no_minimize.py
"""

import wx

app = wx.App()
frame = wx.Frame(
    None,
    style=wx.MAXIMIZE_BOX
    | wx.RESIZE_BORDER
    | wx.SYSTEM_MENU
    | wx.CAPTION
    | wx.CLOSE_BOX,
)
frame.Show()

app.MainLoop()
