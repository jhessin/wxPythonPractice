#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we drag and drop text data.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

from pathlib import Path
import os
import wx


class MyTextDropTarget(wx.TextDropTarget):
    object: wx.ListCtrl

    def __init__(self, object: wx.ListCtrl):
        wx.TextDropTarget.__init__(self)
        self.object = object

    def OnDropText(self, x, y, data):
        self.object.InsertItem(0, data)
        return True


class Example(wx.Frame):
    dir_wid: wx.GenericDirCtrl
    lc1: wx.ListCtrl
    lc2: wx.ListCtrl

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        splitter1 = wx.SplitterWindow(self, style=wx.SP_3D)
        splitter2 = wx.SplitterWindow(splitter1, style=wx.SP_3D)

        home_dir = str(Path.home())

        self.dir_wid = wx.GenericDirCtrl(splitter1, dir=home_dir,
                                         style=wx.DIRCTRL_DIR_ONLY)

        self.lc1 = wx.ListCtrl(splitter2, style=wx.LC_LIST)
        self.lc2 = wx.ListCtrl(splitter2, style=wx.LC_LIST)

        dt = MyTextDropTarget(self.lc2)
        self.lc2.SetDropTarget(dt)

        self.Bind(wx.EVT_LIST_BEGIN_DRAG, self.on_drag_init, id=self.lc1.GetId())

        tree: wx.TreeCtrl = self.dir_wid.GetTreeCtrl()

        splitter2.SplitHorizontally(self.lc1, self.lc2, 150)
        splitter1.SplitVertically(self.dir_wid, splitter2, 200)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_select, id=tree.GetId())

        self.on_select(0)

        self.SetTitle('Drag and drop text')
        self.Center()

    def on_select(self, _e: wx.ListEvent):

        file_list: list[str] = os.listdir(self.dir_wid.GetPath())

        self.lc1.ClearAll()
        self.lc2.ClearAll()

        for i in range(len(file_list)):
            if file_list[i][0] != '.':
                self.lc1.InsertItem(0, file_list[i])

    def on_drag_init(self, e: wx.ListEvent):
        text = self.lc1.GetItemText(e.GetIndex())
        tdo = wx.TextDataObject(text)
        tds = wx.DropSource(self.lc1)

        tds.SetData(tdo)
        tds.DoDragDrop(True)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
