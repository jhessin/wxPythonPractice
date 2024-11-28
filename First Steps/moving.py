#!/usr/bin/env python
"""
moving.py
"""

import wx


class Example(wx.Frame):
    def __init__(self, parent, title, *args, **kw):
        super().__init__(parent, title=title, size=(300, 200), *args, **kw)

        self.Move(800, 250)
        # self.Maximize()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None, title="Moving")
    ex.Show()
    app.MainLoop()
# end main
