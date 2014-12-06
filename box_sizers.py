import wx

class exampleframe(wx.Frame):
	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent)
		self.Show()
		
		text = wx.TextCtrl(self)
		button_hi = wx.Button(self, label="hi")
		button_bi = wx.Button(self, label="bi")
		
		wrap_sizer = wx.BoxSizer(wx.VERTICAL)
		text_sizer = wx.BoxSizer(wx.HORIZONTAL)
		button_sizer = wx.BoxSizer(wx.HORIZONTAL)
		
		button_sizer.Add(button_hi, 0, wx.CENTER| wx.EXPAND | wx.RIGHT, 15)
		button_sizer.Add(button_bi, 0, wx.CENTER | wx.EXPAND)
		
		text_sizer.Add(text, 1, wx.EXPAND | wx.CENTER | wx.ALL)
		
		wrap_sizer.Add(text_sizer,1,wx.EXPAND | wx.CENTER | wx.ALL, 10)
		wrap_sizer.Add(button_sizer,0, wx.CENTER | wx.ALL, 10)
		
		self.SetSizer(wrap_sizer)
		wrap_sizer.Fit(self)
		
app = wx.App()
window = exampleframe(None)
app.MainLoop()
	