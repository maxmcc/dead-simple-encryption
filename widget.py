import wx

class Console(wx.Frame):

    def __init__(self, *args, **keywords):

        wx.Frame.__init__(self, *args, **keywords)
        # box sizer
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(sizer)

        # encryption
        encrypt = wx.Button(self, -1, 'Encrypt')
        self.Bind(wx.EVT_BUTTON, self.btn_Press, encrypt)
        sizer.Add(encrypt, 0, wx.EXPAND, 0)

        decrypt = wx.Button(self, -1, 'Decrypt')
        self.Bind(wx.EVT_BUTTON, self.btn_Press, decrypt)
        sizer.Add(decrypt, 0, wx.EXPAND, 0)

        # set sizer
        sizer.Fit(self)

    def btn_Press(self, event):
        val = event.GetEventObject().GetLabel()


def main():
    ''' Create an app instance and a top-level frame,
    then run the main loop.'''
    app = wx.App()
    frame = Console(parent=None, id=wx.ID_ANY, title="Dead Simple Encryption", size=wx.Size(200,200))
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()

