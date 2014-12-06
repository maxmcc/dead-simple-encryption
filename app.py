import wx

class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        self.window.AppendText("%d file(s) dropped at (%d,%d):\n" % (len(filenames), x, y))
        files = []
        for file in filenames:
            self.window.AppendText("%s\n" % file)
            files.append(file)

class Frame(wx.Frame):

    def __init__(self, *args, **keywords):

        wx.Frame.__init__(self, None, title="Drop Target",size=(500,300))
        p = wx.Panel(self)

        label = wx.StaticText(p, -1, "Drop some files here:")
        text = wx.TextCtrl(p, -1, "",style=wx.TE_MULTILINE|wx.HSCROLL)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label, 0, wx.ALL, 5)
        sizer.Add(text, 1, wx.EXPAND|wx.ALL, 5)
                # encryption
        encrypt = wx.Button(self, -1, 'Encrypt')
        self.Bind(wx.EVT_BUTTON, self.btn_Press, encrypt)
        sizer.Add(encrypt, 2, wx.EXPAND, 5)

        decrypt = wx.Button(self, -1, 'Decrypt')
        self.Bind(wx.EVT_BUTTON, self.btn_Press, decrypt)
        sizer.Add(decrypt, 3, wx.EXPAND, 5)

        p.SetSizerAndFit(sizer)
        self.Fit()

        dt = MyFileDropTarget(text)
        text.SetDropTarget(dt)



    def btn_Press(self, event):
        val = event.GetEventObject().GetLabel()




def main():
    ''' Create an app instance and a top-level frame,
    then run the main loop.'''
    app = wx.App()
    frame = Frame(parent=None, id=wx.ID_ANY, title="Dead Simple Encryption", size=wx.Size(200,200))
    frame.Show(True)
    app.MainLoop()



if __name__ == "__main__":
    main()

