# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Models.Parametros import Parametros

###########################################################################
## Class FrmCambioPass
###########################################################################

class FrmPassword(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Cambio Contraseña", pos=wx.DefaultPosition,
                           size=wx.Size(355, 201), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        bSizer29 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"Contraseña Anterior", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText13.Wrap(-1)
        bSizer29.Add(self.m_staticText13, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtpassAnt = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TE_PASSWORD)
        bSizer29.Add(self.txtpassAnt, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer28.Add(bSizer29, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer30 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"Nueva Contraseña", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        bSizer30.Add(self.m_staticText14, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtpassNuevo = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PASSWORD)
        bSizer30.Add(self.txtpassNuevo, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer28.Add(bSizer30, 0, wx.EXPAND, 5)

        bSizer31 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"Repita Contraseña", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText15.Wrap(-1)
        bSizer31.Add(self.m_staticText15, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtRepPass = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TE_PASSWORD)
        bSizer31.Add(self.txtRepPass, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer28.Add(bSizer31, 0, wx.EXPAND, 5)

        bSizer33 = wx.BoxSizer(wx.VERTICAL)

        self.lblMensaje = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblMensaje.Wrap(-1)
        bSizer33.Add(self.lblMensaje, 0, wx.ALL, 5)

        bSizer28.Add(bSizer33, 0, wx.EXPAND, 5)

        bSizer32 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnAceptar = wx.Button(self, wx.ID_ANY, u"&Aceptar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer32.Add(self.btnAceptar, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.btnClose = wx.Button(self, wx.ID_ANY, u"&Salir", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer32.Add(self.btnClose, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        bSizer28.Add(bSizer32, 1, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer28)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btnAceptar.Bind(wx.EVT_BUTTON, self.btnAceptarOnButtonClick)
        self.btnClose.Bind(wx.EVT_BUTTON, self.btnCloseOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnAceptarOnButtonClick(self, event):
        anterior = str(self.txtpassAnt.GetValue())
        nueva = str(self.txtpassNuevo.GetValue())
        repeticion = str(self.txtRepPass.GetValue())

        p = Parametros.query.first()

        if(str(p.password) != anterior):
            self.lblMensaje.SetLabel(u'No coincide contraseña anterior')

        if(nueva != repeticion):
            self.lblMensaje.SetLabel(u'No coinciden las contraseñas')

        if(nueva == ''):
            self.lblMensaje.SetLabel(u'El campo contraseña no puede estar vacío')

        if(len(nueva) < 5):
            self.lblMensaje.SetLabel(u'Contraseña muy corta')

        p.password = hash(nueva)
        p.guardar()
        self.Close()

    def btnCloseOnButtonClick(self, event):
        self.Close()
