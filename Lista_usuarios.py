import wx
import wx.grid
import requests

class Usuarios(wx.Frame):
    grid = None
    empleados = []

    def __init__(self, *args, **kw):
        super(Usuarios, self).__init__(*args, **kw)

        self.pnl = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.tabla(sizer)
        self.pnl.SetSizer(sizer)

        self.consultar_usuarios()


    def tabla(self, main_sizer):
        self.list_ctrl = wx.ListCtrl(self.pnl, size=(-1, 500),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN)

        self.list_ctrl.InsertColumn(0, 'Id')
        self.list_ctrl.InsertColumn(1, 'Gender', width=100)
        self.list_ctrl.InsertColumn(2, 'Name', width=100)
        self.list_ctrl.InsertColumn(3, 'Email', width=100)
        self.list_ctrl.InsertColumn(4, 'Status', width=100)

        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 6)

    def agregar(self):
        self.list_ctrl.ClearAll()
        self.list_ctrl.InsertColumn(0, 'Id')
        self.list_ctrl.InsertColumn(1, 'Gender', width=100)
        self.list_ctrl.InsertColumn(2, 'Name', width=100)
        self.list_ctrl.InsertColumn(3, 'Email', width=100)
        self.list_ctrl.InsertColumn(4, 'Status', width=100)

        for i, empleado in enumerate(self.empleados):
            self.list_ctrl.InsertItem(i, empleado ['id'])
            self.list_ctrl.SetItem(i, 1, empleado['gender'])
            self.list_ctrl.SetItem(i, 2, empleado['name'])
            self.list_ctrl.SetItem(i, 3, empleado['email'])
            self.list_ctrl.SetItem(i, 4, empleado['status'])

    def guardar(self):
        self.agregar()
        print(self.empleados)

    def consultar_usuarios(self):
        r = requests.get('https://gorest.co.in/public/v1/users?page=15')
        usuarios =r.json()
        self.empleados = usuarios["data"]


        self.agregar()

if __name__ == '__main__':

    app = wx.App()
    frm = Usuarios(None, title='LISTADO DE USUARIOS')
    frm.Show()
    app.MainLoop()
