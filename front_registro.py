import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="GymOS")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        self.nombre = wx.TextCtrl(panel)
        self.contraseña = wx.TextCtrl(panel)

        my_sizer.Add(wx.StaticText(panel, label="Nombre:"))
        my_sizer.Add(self.nombre, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(wx.StaticText(panel, label="Contraseña: "))
        my_sizer.Add(self.contraseña, 0, wx.ALL | wx.EXPAND, 5)

        my_btn = wx.Button(panel, label="Press Me")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)

        self.Show()

    def on_press(self, event):
        valueNombre = self.nombre.GetValue()
        valueContraseña = self.contraseña.GetValue()

        if not valueContraseña and not valueNombre:
            print("Campos vacios")
        elif not valueNombre:
            print("Falta el nombre")
        elif not valueContraseña:
            print("Falta contraseña")


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
