import wx

class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        self.window.AppendText("%d file(s) dropped at (%d,%d):\n" % (len(filenames), x, y))
        for file in filenames:
            self.window.AppendText("%s\n" % file)
            

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Drop Target",size=(500,300))
        p = wx.Panel(self)

        label = wx.StaticText(p, -1, "Drop some files here:")
        text = wx.TextCtrl(p, -1, "",style=wx.TE_MULTILINE|wx.HSCROLL)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label, 0, wx.ALL, 5)
        sizer.Add(text, 1, wx.EXPAND|wx.ALL, 5)
        p.SetSizer(sizer)

        dt = MyFileDropTarget(text)
        text.SetDropTarget(dt)
        

app = wx.PySimpleApp()
frm = MyFrame()
frm.Show()
app.MainLoop()
