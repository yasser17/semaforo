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
from Models.Premio import Premio
from sqlalchemy import desc
import datetime

###########################################################################
## Class FrmRegistros
###########################################################################

class FrmRegistrosDiario(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Registros de Pulsaciones para el día " + str(datetime.datetime.now().date().strftime('%d/%m/%Y')), pos=wx.DefaultPosition,
                           size=wx.Size(481, 550), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer24 = wx.BoxSizer(wx.VERTICAL)

        self.list = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
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
        pulsaciones = Pulsacion.query.filter_by(dia=datetime.datetime.now().date()).order_by(desc(Pulsacion.id)).all()
        for p in pulsaciones:
            day = p.created_at.strftime('%d/%m/%Y')
            hora = p.created_at.strftime('%H:%M')
            numero = str(p.pulsacion)
            if(p.premio_id is not None):
                premio = Premio.query.get(p.premio_id)
                texto = premio.get_color()
            else:
                texto = ""
            self.list.AppendItem([day, hora, numero, texto])