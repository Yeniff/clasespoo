import wx
import wx.grid
from datetime import datetime

class ClaseVentana(wx.Frame):
    grid = None
    empleados = []

    def __init__(self, *args, **kw):
        super(ClaseVentana, self).__init__(*args, **kw)

        self.pnl = wx.Panel(self)
        self.cuadro_texto ()
        self.boton()


        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.text_ctrl, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.my_btn, 0, wx.ALL | wx.CENTER, 5)
        self.tabla(sizer)
        #sizer.Add(self.grid, 0, wx.ALL | wx.EXPAND, 5)
        self.pnl.SetSizer(sizer)



    def boton(self):
        self.my_btn = wx.Button(self.pnl, label= 'Registrar')
        self.my_btn.Bind(wx.EVT_BUTTON, self.guardar)

    def cuadro_texto(self):
        self.text_ctrl = wx.TextCtrl(self.pnl)


    def tabla(self, main_sizer):
        self.list_ctrl = wx.ListCtrl(self.pnl, size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN)

        self.list_ctrl.InsertColumn(0, 'Empleado', width=140)
        self.list_ctrl.InsertColumn(1, 'Fecha Llegada', width=140)

        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

    def agregar(self):
        self.list_ctrl.ClearAll()
        self.list_ctrl.InsertColumn(0, 'Empleado', width=140)
        self.list_ctrl.InsertColumn(1, 'Fecha Llegada', width=140)

        for i, empleado in enumerate(self.empleados):
            self.list_ctrl.InsertItem(i, empleado['nombre'])
            self.list_ctrl.SetItem(i, 1, empleado['fecha'])

    def guardar(self, event):
        value = self.text_ctrl.GetValue()

        self.empleados.append({"nombre": value, "fecha": datetime.today().strftime('%Y-%m-%d')})

        self.agregar()
        print(self.empleados)


if __name__ == '__main__':

    app = wx.App()
    frm = ClaseVentana(None, title='Control de tiempos')
    frm.Show()
    app.MainLoop()
