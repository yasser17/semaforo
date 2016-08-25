# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Models.semana import Semana
from Models.Premio import Premio
import datetime


###########################################################################
## Class FrmPremio
###########################################################################

class FrmPremio(wx.Dialog):
    semana = None
    def __init__(self, parent, xsemana_id, xColor):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Nuevo Premio", pos=wx.DefaultPosition,
                           size=wx.Size(365, 205), style=wx.DEFAULT_DIALOG_STYLE)

        self.semana = Semana.query.get(xsemana_id)
        self.fecha = self.semana.fechaInicio
        self.color = xColor

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        bSizer23 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer23.Add(self.m_staticText10, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        comboFechaChoices = []
        self.comboFecha = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboFechaChoices, 0)
        self.comboFecha.SetItems(['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])
        self.comboFecha.SetSelection(0)
        bSizer23.Add(self.comboFecha, 0, wx.ALL, 5)

        self.lblFecha = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblFecha.Wrap(-1)
        self.lblFecha.SetLabel(self.semana.fechaInicio.strftime('%d/%m/%Y'))

        bSizer23.Add(self.lblFecha, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer18.Add(bSizer23, 0, wx.EXPAND, 5)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Ingrese número de pulsación", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer19.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtNumero = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          wx.SP_ARROW_KEYS, 0, 5000, 0)
        bSizer19.Add(self.txtNumero, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer18.Add(bSizer19, 0, 0, 5)

        bSizer20 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbldescripcion = wx.StaticText(self, wx.ID_ANY, u"Descripción", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbldescripcion.Wrap(-1)
        bSizer20.Add(self.lbldescripcion, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtDescripcion = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer20.Add(self.txtDescripcion, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer18.Add(bSizer20, 0, wx.EXPAND, 5)

        bSizer22 = wx.BoxSizer(wx.VERTICAL)

        self.lblMensaje = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblMensaje.Wrap(-1)
        bSizer22.Add(self.lblMensaje, 0, wx.ALL, 5)

        bSizer18.Add(bSizer22, 0, 0, 5)

        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnConfirmar = wx.Button(self, wx.ID_ANY, u"&Confirmar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer21.Add(self.btnConfirmar, 0, wx.ALL, 5)

        self.m_button18 = wx.Button(self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer21.Add(self.m_button18, 0, wx.ALL, 5)

        bSizer18.Add(bSizer21, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer18)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.comboFecha.Bind(wx.EVT_CHOICE, self.comboFechaOnChoice)
        self.btnConfirmar.Bind(wx.EVT_BUTTON, self.btnConfirmarOnButtonClick)
        self.m_button18.Bind(wx.EVT_BUTTON, self.m_button18OnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def comboFechaOnChoice(self, event):
        self.fecha = self.semana.fechaInicio + datetime.timedelta(days=int(self.comboFecha.GetSelection()))
        self.lblFecha.SetLabel(self.fecha.strftime('%d/%m/%Y'))

    def btnConfirmarOnButtonClick(self, event):
        if(self.txtNumero.GetValue() <= 0):
            self.lblMensaje.SetLabel(u'Debe seleccionar un valor mayor')
            return False
        p = None
        p = Premio.query.filter_by(semana_id=self.semana.id, fecha=self.fecha, numero=self.txtNumero.GetValue()).first()
        if(p is not None):
            self.lblMensaje.SetLabel(u'Ya existe un premio para ese día y número de pulsación')
            return False
        premio = Premio()
        premio.semana_id = self.semana.id
        premio.fecha = self.fecha
        premio.numero = self.txtNumero.GetValue()
        premio.color = self.color
        premio.descripcion = self.txtDescripcion.GetValue()
        premio.guardar()
        self.Close()

    def m_button18OnButtonClick(self, event):
        self.Close()