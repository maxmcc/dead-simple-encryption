import wx


class Calculator(wx.Frame):
    ''' Class for the top-level frame.

    1. Create a BoxSizer to hold main elements, and set it
    as the sizer for the frame.

    2. Create a TextCtrl for the display, and add it to the BoxSizer.
    see: http://www.wxpython.org/docs/api/wx.TextCtrl-class.html

    Remember that all Add() methods take a "flag" parameter. Play around
    with this to get the expanding / alignment right.
    see: http://www.wxpython.org/docs/api/wx.Sizer-class.html#Add

    3. Create a GridSizer for the buttons, and add it to the BoxSizer.

    4. Create all main buttons, add them to the GridSizer, and bind
    their events to the frame.

    5. Create the equals button, add it to the BoxSizer, and bind its
    event to the frame.

    6. Fit the window to the BoxSizer.
    see: http://www.wxpython.org/docs/api/wx.Sizer-class.html#Fit

    7. Create a handler for the button presses.
       a. Get the label of pressed button.
       b. If the label is "=":
          i. Get the contents of the TextCtrl display.
          ii. Use eval() to calculate the result.
              Note - in general eval() is unsafe, and you should be
              very careful about using it.
              see: http://lybniz2.sourceforge.net/safeeval.html
          iii. Show the result in the TextCtrl display.
       c. If the label is "C":
          Clear the contents of the TextCtrl display.
       d. Else:
          Add the button label text to the TextCtrl display.
    '''
    def __init__(self, *args, **keywords):

        wx.Frame.__init__(self, *args, **keywords)
        # box sizer
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(sizer)

        # text control
        self.display = wx.TextCtrl(self, -1, '', )
        sizer.Add(self.display, 0, wx.EXPAND)

        # grid sizer
        grid = wx.GridSizer(4, 4)
        sizer.Add(grid, 1, wx.EXPAND)

        # buttons
        btns = (('7', '8', '9', '/'),
                ('4', '5', '6', '*'),
                ('1', '2', '3', '-'),
                ('0', '.', 'C', '+'))
        for row in btns:
            for label in row:
                b = wx.Button(self, -1, label)
                self.Bind(wx.EVT_BUTTON, self.btn_Press, b)
                grid.Add(b, 0, wx.EXPAND, 0)

        # equals button
        equal = wx.Button(self, -1, '=')
        self.Bind(wx.EVT_BUTTON, self.btn_Press, equal)
        sizer.Add(equal, 0, wx.EXPAND, 0)

        # set sizer
        sizer.Fit(self)

    def btn_Press(self, event):
        val = event.GetEventObject().GetLabel()

        # equal
        if val == '=':
            current = self.display.GetValue()
            # check empty
            if current.strip():
                res = eval(current)
                self.display.SetValue(str(res))
            else:
                return

        # clear
        elif val == 'C':
            self.display.SetValue('')

        # keep adding to display
        else:
            self.display.SetValue(self.display.GetValue() + val)


def main():
    ''' Create an app instance and a top-level frame,
    then run the main loop.'''
    app = wx.App()
    frame = Calculator(parent=None, id=wx.ID_ANY, title="Calculator")
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
