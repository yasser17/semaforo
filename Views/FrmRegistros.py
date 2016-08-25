# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from Models.Pulsacion import Pulsacion
from sqlalchemy import desc

###########################################################################
## Class FrmRegistros
###########################################################################

class FrmRegistros(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Registros de Pulsaciones", pos=wx.DefaultPosition,
                           size=wx.Size(481, 550), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer24 = wx.BoxSizer(wx.VERTICAL)

        self.list = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.list.AppendTextColumn(u'Fecha', width=80)
        self.list.AppendTextColumn(u'Hora', width=100)
        self.list.AppendTextColumn(u'Número', width=80)
        self.list.AppendTextColumn(u'Premio', width=150)
        bSizer24.Add(self.list, 1, wx.ALL | wx.EXPAND, 5)

        bSizer25 = wx.BoxSizer(wx.VERTICAL)

        self.btnClose = wx.Button(self, wx.ID_ANY, u"&Salir", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer25.Add(self.btnClose, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer24.Add(bSizer25, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer24)
        self.Layout()

        self.Centre(wx.BOTH)
        self.listar()

        # Connect Events
        self.btnClose.Bind(wx.EVT_BUTTON, self.btnCloseOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnCloseOnButtonClick(self, event):
        self.Close()

    def listar(self):
        self.list.DeleteAllItems()
        pulsaciones = Pulsacion.query.order_by(desc(Pulsacion.id)).all()
        for p in pulsaciones:
            day = p.created_at.strftime('%d/%m/%Y')
            hora = p.created_at.strftime('%H:%M')
            numero = str(p.pulsacion)
            self.list.AppendItem([day, hora, numero, ''])