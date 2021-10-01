import wx


class Ventana(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='BIENVENIDO')
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(65, 65))
        my_btn = wx.Button(panel, label='CERRAR', pos=(100, 150))

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = Ventana()
    app.MainLoop()
