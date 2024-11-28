#!/usr/bin/env python
"""
set_size.py
"""

import wx


class Example(wx.Frame):
    def __init__(self, parent, title, *args, **kw):
        super().__init__(parent, title=title, size=(350, 250), *args, **kw)


def main():
    app = wx.App()
    ex = Example(None, title="Sizing")
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
