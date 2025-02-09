#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a help window with wx.html.HtmlWindow.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx
import wx.html as html


class Example(wx.Frame):
    panel_right: wx.Panel
    panel_left: wx.Panel
    splitter: wx.SplitterWindow

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        toolbar: wx.ToolBar = self.CreateToolBar()
        toolbar.AddTool(1, 'Exit', wx.Bitmap('exit.png'))
        toolbar.AddTool(2, 'Help', wx.Bitmap('help.png'))
        toolbar.Realize()

        self.splitter = wx.SplitterWindow(self)
        self.panel_left = wx.Panel(self.splitter, wx.ID_ANY, style=wx.BORDER_SUNKEN)

        self.panel_right = wx.Panel(self.splitter)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        header = wx.Panel(self.panel_right, wx.ID_ANY)

        header.SetBackgroundColour('#6f6a59')
        header.SetForegroundColour('white')

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        st = wx.StaticText(header, wx.ID_ANY, 'Help')
        font: wx.Font = st.GetFont()
        font.SetFamily(wx.FONTFAMILY_ROMAN)
        font.SetPointSize(11)
        st.SetFont(font)

        hbox.Add(st, 1, wx.TOP | wx.BOTTOM | wx.LEFT, 8)

        close_btn = wx.BitmapButton(header, wx.ID_ANY, wx.Bitmap('closebutton.png',
                                                                 wx.BITMAP_TYPE_PNG), style=wx.NO_BORDER)
        close_btn.SetBackgroundColour('#6f6a59')

        hbox.Add(close_btn, 0, wx.TOP | wx.BOTTOM, 8)
        header.SetSizer(hbox)

        vbox2.Add(header, 0, wx.EXPAND)

        help_win = html.HtmlWindow(self.panel_right, style=wx.NO_BORDER)
        help_win.LoadPage('help.html')

        vbox2.Add(help_win, 1, wx.EXPAND)

        self.panel_right.SetSizer(vbox2)
        self.panel_left.SetFocus()

        self.splitter.SplitVertically(self.panel_left, self.panel_right)
        self.splitter.Unsplit()

        self.Bind(wx.EVT_BUTTON, self.close_help, id=close_btn.GetId())
        self.Bind(wx.EVT_TOOL, self.on_close, id=1)
        self.Bind(wx.EVT_TOOL, self.on_help, id=2)

        self.panel_left.Bind(wx.EVT_KEY_DOWN, self.on_key_pressed)
        self.panel_left.SetFocus()

        self.CreateStatusBar()

        self.SetTitle('Help')
        self.Center()

    def on_close(self, e: wx.Event):
        self.Close()

    def on_help(self, e: wx.Event):
        self.splitter.SplitVertically(self.panel_left, self.panel_right)
        self.panel_left.SetFocus()

    def close_help(self, e: wx.Event):
        self.splitter.Unsplit()
        self.panel_left.SetFocus()

    def on_key_pressed(self, e: wx.KeyEvent):
        keycode = e.GetKeyCode()
        print(keycode)

        if keycode == wx.WXK_F1:
            self.splitter.SplitVertically(self.panel_left, self.panel_right)
            self.panel_left.SetFocus()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
