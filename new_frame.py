"""
Create a simple window with no widgets."
"""

import wx

app = wx.App() #top level widgets

window = wx.Frame(None, -1, "Blank Window") #parent, id, title

window.Show() #show the window

app.MainLoop() #always requires a loop.