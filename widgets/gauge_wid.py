#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this code example,
we create a gauge widget.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

TASK_RANGE = 50


class Example(wx.Frame):
    text: wx.StaticText
    btn1: wx.Button
    btn2: wx.Button
    btn3: wx.Button
    gauge: wx.Gauge
    timer: wx.Timer
    count: int = 0

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):

        self.timer = wx.Timer(self, 1)
        self.count = 0

        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        self.gauge = wx.Gauge(pnl, range=TASK_RANGE, size=(250, -1))
        self.btn1 = wx.Button(pnl, wx.ID_OK)
        self.btn2 = wx.Button(pnl, wx.ID_STOP)
        self.text = wx.StaticText(pnl, label='Task to be done')

        self.Bind(wx.EVT_BUTTON, self.on_ok, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.on_stop, self.btn2)

        hbox1.Add(self.gauge, proportion=1, flag=wx.ALIGN_CENTER)
        hbox2.Add(self.btn1, proportion=1, flag=wx.RIGHT, border=10)
        hbox2.Add(self.btn2, proportion=1)
        hbox3.Add(self.text, proportion=1)

        vbox.Add((0, 30))

        vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTER)
        vbox.Add(hbox3, proportion=1, flag=wx.ALIGN_CENTER)

        pnl.SetSizer(vbox)

        self.SetTitle('wx.Gauge')
        self.Center()

    def on_timer(self, e: wx.CommandEvent):

        self.count += 1
        self.gauge.SetValue(self.count)

        if self.count == TASK_RANGE:
            self.timer.Stop()
            self.text.SetLabel('Task Completed')

    def on_ok(self, e: wx.CommandEvent):

        if self.count >= TASK_RANGE:
            return

        self.timer.Start(100)
        self.text.SetLabel('Task in Progress')

    def on_stop(self, e: wx.CommandEvent):

        if self.count == 0 or self.count >= TASK_RANGE or not self.timer.IsRunning():
            return

        self.timer.Stop()
        self.text.SetLabel('Task Interrupted')


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
