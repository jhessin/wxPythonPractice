#!/usr/bin/env python
"""
centering.py
"""

import wx


class Example(wx.Frame):
    def __init__(self, parent, title, *args, **kw):
        super().__init__(parent, title=title, size=(300, 300), *args, **kw)

        self.Center()


if __name__ == "__main__":
    app = wx.App()
    ex = Example(None, title="Centering")
    ex.Show()
    app.MainLoop()
# end main
