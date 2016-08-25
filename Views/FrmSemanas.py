# -*- coding: utf-8 -*-


import wx
import wx.xrc
import wx.dataview
from Views.FrmSemana import FrmSemana
from Controllers.SemanasController import SemanasController
from Views.FrmPremios import FrmPremios
from Models.semana import Semana
from Models.Premio import Premio


###########################################################################
## Class FrmSemanas
###########################################################################

class FrmSemanas(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Semanas", pos=wx.DefaultPosition, size=wx.Size(707, 429),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.list = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 350), 0)
        self.list.AppendTextColumn(u'Id', width=100)
        self.list.AppendTextColumn(u'Fecha Inicio', width=120)
        self.list.AppendTextColumn(u'Fecha Fin', width=120)
        self.list.AppendTextColumn(u'Estado', width=380)
        bSizer3.Add(self.list, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnAgregar = wx.Button(self, wx.ID_ANY, u"&Agregar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.btnAgregar, 0, wx.ALL, 5)

        self.btnModificar = wx.Button(self, wx.ID_ANY, u"&Modificar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.btnModificar, 0, wx.ALL, 5)

        self.btnEliminar = wx.Button(self, wx.ID_ANY, u"&Eliminar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.btnEliminar, 0, wx.ALL, 5)

        self.btnPremios = wx.Button(self, wx.ID_ANY, u"Definir &Premios", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.btnPremios, 0, wx.ALL, 5)

        self.btnSalir = wx.Button(self, wx.ID_ANY, u"&Salir", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.btnSalir, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 1, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        self.cargarList()

        # Connect Events
        self.btnAgregar.Bind(wx.EVT_BUTTON, self.btnAgregarOnButtonClick)
        self.btnModificar.Bind(wx.EVT_BUTTON, self.btnModificarOnButtonClick)
        self.btnEliminar.Bind(wx.EVT_BUTTON, self.btnEliminarOnButtonClick)
        self.btnPremios.Bind(wx.EVT_BUTTON, self.btnPremiosOnButtonClick)
        self.btnSalir.Bind(wx.EVT_BUTTON, self.btnSalirOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnAgregarOnButtonClick(self, event):
        mfrm = FrmSemana(None, None)
        mfrm.ShowModal()
        mfrm.Destroy()
        self.cargarList()

    def btnModificarOnButtonClick(self, event):
        if(self.list.GetSelectedRow() >= 0):
            id = self.list.GetValue(self.list.GetSelectedRow(), 0)
            mfrm = FrmSemana(None, id)
            mfrm.ShowModal()
            mfrm.Destroy()
            self.cargarList()


    def btnEliminarOnButtonClick(self, event):
        if(self.list.GetSelectedRow() >= 0):
            id = self.list.GetValue(self.list.GetSelectedRow(), 0)
            semana = Semana.query.get(id)
            premio = None
            premio = Premio.query.filter_by(semana_id=semana.id).first()
            if(premio is None):
                semana.eliminar()
            self.cargarList()

    def btnPremiosOnButtonClick(self, event):
        if(self.list.GetSelectedRow() >= 0):
            id = self.list.GetValue(self.list.GetSelectedRow(), 0)
            mfrm = FrmPremios(None, id)
            mfrm.ShowModal()
            mfrm.Destroy()

    def btnSalirOnButtonClick(self, event):
        self.Close()

    def cargarList(self):
        semanas = Semana.query.order_by(Semana.fechaInicio)
        self.list.DeleteAllItems()
        for s in semanas:
            fecha = s.fechaInicio.strftime('%d/%m/%Y')
            fechaFin = s.fechaFin.strftime('%d/%m/%Y')
            if (s.estado_id == 1):
                estado = "Pendiente"
            if (s.estado_id == 2):
                estado = "En Proceso"
            if (s.estado_id == 3):
                estado = "Finalizado"
            if (s.estado_id == 4):
                estado = "Cancelado"
            self.list.AppendItem([str(s.id), fecha, fechaFin, estado])