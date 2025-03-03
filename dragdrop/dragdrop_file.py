#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we drag and drop files!

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class FileDrop(wx.FileDropTarget):
    window: wx.TextCtrl

    def __init__(self, window: wx.TextCtrl):

        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):

        for name in filenames:

            try:
                file = open(name, 'r')
                text = file.read()
                self.window.WriteText(text)

            except IOError as error:

                msg = f"Error opening file\n {str(error)}"
                dlg = wx.MessageDialog(None, msg)
                dlg.ShowModal()

                return False

            except UnicodeDecodeError as error:

                msg = f"Cannot open non ascii files\n {str(error)}"
                dlg = wx.MessageDialog(None, msg)
                dlg.ShowModal()

                return False
            finally:

                file.close()

        return True


class Example(wx.Frame):
    text: wx.TextCtrl

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        dt = FileDrop(self.text)

        self.text.SetDropTarget(dt)

        self.SetTitle('File drag and drop')
        self.Center()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
