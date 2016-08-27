# -*- coding: utf-8 -*-

import wx
import wx.xrc
import wx.dataview
from Models.semana import Semana
from Views.FrmPremio import FrmPremio
from Models.Premio import Premio
from Models.Pulsacion import Pulsacion


###########################################################################
## Class FrmPremios
###########################################################################

class FrmPremios(wx.Dialog):
    semana = None
    def __init__(self, parent, xsemana_id):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Premios", pos=wx.DefaultPosition, size=wx.Size(847, 560),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.semana = Semana.query.get(xsemana_id)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Premios para semana: " + self.semana.fechaInicio.strftime('%d/%m/%Y') + ' a ' + self.semana.fechaFin.strftime('%d/%m/%Y'), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(16, 74, 90, 90, False, "Arial"))

        bSizer9.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer8.Add(bSizer9, 0, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Premios para color Verde", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer11.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.listVerde = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
        self.listVerde.AppendTextColumn(u'Día', width=80)
        self.listVerde.AppendTextColumn(u'Número', width=80)
        self.listVerde.AppendTextColumn(u'Descripción', width=120)
        verde = wx.Colour(1,255,112)
        self.listVerde.SetBackgroundColour(verde)
        bSizer11.Add(self.listVerde, 1, wx.ALL | wx.EXPAND, 5)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnAdd1 = wx.Button(self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.btnAdd1, 0, wx.ALL, 5)

        self.btnRemove1 = wx.Button(self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.btnRemove1, 0, wx.ALL, 5)

        bSizer11.Add(bSizer15, 0, wx.EXPAND, 5)

        bSizer10.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Premios para color Amarillo", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer13.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.listAmarillo = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
        self.listAmarillo.AppendTextColumn(u'Día', width=80)
        self.listAmarillo.AppendTextColumn(u'Número', width=80)
        self.listAmarillo.AppendTextColumn(u'Descripción', width=120)
        amarillo = wx.Colour(255, 220, 0)
        self.listAmarillo.SetBackgroundColour(amarillo)
        bSizer13.Add(self.listAmarillo, 1, wx.ALL | wx.EXPAND, 5)

        bSizer151 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnAdd2 = wx.Button(self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer151.Add(self.btnAdd2, 0, wx.ALL, 5)

        self.btnRemove2 = wx.Button(self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer151.Add(self.btnRemove2, 0, wx.ALL, 5)

        bSizer13.Add(bSizer151, 0, wx.EXPAND, 5)

        bSizer10.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Premios para color Rojo", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer14.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.listRojo = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
        self.listRojo.AppendTextColumn(u'Día', width=80)
        self.listRojo.AppendTextColumn(u'Número', width=80)
        self.listRojo.AppendTextColumn(u'Descripción', width=120)
        rojo = wx.Colour(255, 65, 54)
        self.listRojo.SetBackgroundColour(rojo)
        bSizer14.Add(self.listRojo, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1511 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnAdd3 = wx.Button(self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1511.Add(self.btnAdd3, 0, wx.ALL, 5)

        self.btnRemove3 = wx.Button(self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1511.Add(self.btnRemove3, 0, wx.ALL, 5)

        bSizer14.Add(bSizer1511, 0, wx.EXPAND, 5)

        bSizer10.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer8.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer22 = wx.BoxSizer(wx.VERTICAL)

        self.btnSalir = wx.Button(self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer22.Add(self.btnSalir, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer8.Add(bSizer22, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer8)
        self.Layout()

        self.Centre(wx.BOTH)

        self.cargarListas()

        # Connect Events
        self.btnAdd1.Bind(wx.EVT_BUTTON, self.btnAdd1OnButtonClick)
        self.btnRemove1.Bind(wx.EVT_BUTTON, self.btnRemove1OnButtonClick)
        self.btnAdd2.Bind(wx.EVT_BUTTON, self.btnAdd2OnButtonClick)
        self.btnRemove2.Bind(wx.EVT_BUTTON, self.btnRemove2OnButtonClick)
        self.btnAdd3.Bind(wx.EVT_BUTTON, self.btnAdd3OnButtonClick)
        self.btnRemove3.Bind(wx.EVT_BUTTON, self.btnRemove3OnButtonClick)
        self.btnSalir.Bind(wx.EVT_BUTTON, self.btnSalirOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def btnAdd1OnButtonClick(self, event):
        mfrm = FrmPremio(None, self.semana.id, 'V')
        mfrm.ShowModal()
        mfrm.Destroy()
        self.cargarListas()

    def btnRemove1OnButtonClick(self, event):
        if(self.listVerde.GetSelectedRow() >= 0):
            premio = self.Verdes[self.listVerde.GetSelectedRow()]
            pulsacion = None
            pulsacion = Pulsacion.query.filter_by(dia=premio.fecha, pulsacion=premio.numero).first()
            if (pulsacion is None):
                premio.borrar()
                self.cargarListas()
            else:
                wx.MessageBox("No se puede eliminar", "Semaforo", wx.OK | wx.ICON_ERROR)

    def btnAdd2OnButtonClick(self, event):
        mfrm = FrmPremio(None, self.semana.id, 'A')
        mfrm.ShowModal()
        mfrm.Destroy()
        self.cargarListas()

    def btnRemove2OnButtonClick(self, event):
        if (self.listAmarillo.GetSelectedRow() >= 0):
            premio = self.Amarillos[self.listAmarillo.GetSelectedRow()]
            pulsacion = None
            pulsacion = Pulsacion.query.filter_by(dia=premio.fecha, pulsacion=premio.numero).first()
            if (pulsacion is None):
                premio.borrar()
                self.cargarListas()
            else:
                wx.MessageBox("No se puede eliminar", "Semaforo", wx.OK | wx.ICON_ERROR)

    def btnAdd3OnButtonClick(self, event):
        mfrm = FrmPremio(None, self.semana.id, 'R')
        mfrm.ShowModal()
        mfrm.Destroy()
        self.cargarListas()

    def btnRemove3OnButtonClick(self, event):
        if (self.listRojo.GetSelectedRow() >= 0):
            premio = self.Rojos[self.listRojo.GetSelectedRow()]
            pulsacion = None
            pulsacion = Pulsacion.query.filter_by(dia=premio.fecha,pulsacion=premio.numero).first()
            if(pulsacion is None):
                premio.borrar()
                self.cargarListas()
            else:
                wx.MessageBox("No se puede eliminar", "Semaforo", wx.OK | wx.ICON_ERROR)

    def btnSalirOnButtonClick(self, event):
        self.Close()

    def cargarListas(self):
        #CARGANDO LISTA VERDE
        self.Verdes = {}
        self.Amarillos = {}
        self.Rojos = {}
        premiosVerde = Premio.query.filter_by(color='V', semana_id=self.semana.id).order_by(Premio.fecha).order_by(Premio.numero).all()
        self.listVerde.DeleteAllItems()
        countV = 0
        for p in premiosVerde:
            self.Verdes[countV] = p
            self.listVerde.AppendItem([p.get_dia(), str(p.numero), p.descripcion])
            countV = countV + 1

        #CARGANDO LISTA AMARILLA
        premiosAmarillo = Premio.query.filter_by(color='A', semana_id=self.semana.id).order_by(Premio.fecha).order_by(Premio.numero).all()
        countA = 0
        self.listAmarillo.DeleteAllItems()
        for p in premiosAmarillo:
            self.Amarillos[countA] = p
            self.listAmarillo.AppendItem([p.get_dia(), str(p.numero), p.descripcion])
            countA = countA + 1

        #CARGANDO LISTA ROJA
        premiosRojo = Premio.query.filter_by(color='R', semana_id=self.semana.id).order_by(Premio.fecha).order_by(Premio.numero).all()
        countR = 0
        self.listRojo.DeleteAllItems()
        for p in premiosRojo:
            self.Rojos[countR] = p
            self.listRojo.AppendItem([p.get_dia(), str(p.numero), p.descripcion])
            countR = countR + 1