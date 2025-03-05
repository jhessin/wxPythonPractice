#!/usr/bin/env python

"""
ZetCode wxPython tutorial

This program creates a ruler.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""

import wx

RW = 701  # ruler width
RM = 10  # ruler margin
RH = 80  # ruler height


class Example(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, size=(RW + 2 * RM, RH),
                          style=wx.FRAME_NO_TASKBAR | wx.NO_BORDER | wx.STAY_ON_TOP)
        self.font = wx.Font(7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_BOLD, False, 'Courier 10 Pitch')

        self.init_ui()

    def init_ui(self):

        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_right_down)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)

        self.Centre()
        self.Show(True)

    def on_paint(self, e):

        dc = wx.PaintDC(self)

        brush = wx.Brush(wx.Bitmap('granite.png'))
        dc.SetBrush(brush)
        dc.DrawRectangle(0, 0, RW + 2 * RM, RH)
        dc.SetFont(self.font)

        dc.SetPen(wx.Pen('#F8FF25'))
        dc.SetTextForeground('#F8FF25')

        for i in range(RW):

            if not (i % 100):

                dc.DrawLine(i + RM, 0, i + RM, 10)
                w, h = dc.GetTextExtent(str(i))
                dc.DrawText(str(i), int(i + RM - w / 2), 11)

            elif not (i % 20):

                dc.DrawLine(i + RM, 0, i + RM, 8)

            elif not (i % 2):

                dc.DrawLine(i + RM, 0, i + RM, 4)

    def on_left_down(self, e):

        x, y = self.ClientToScreen(e.GetPosition())
        ox, oy = self.GetPosition()

        dx = x - ox
        dy = y - oy

        self.delta = ((dx, dy))

    def on_mouse_move(self, e):

        if e.Dragging() and e.LeftIsDown():
            self.SetCursor(wx.Cursor(wx.CURSOR_HAND))

            x, y = self.ClientToScreen(e.GetPosition())
            fp = (x - self.delta[0], y - self.delta[1])
            self.Move(fp)

    def on_left_up(self, e):

        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))

    def on_right_down(self, e):

        self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
