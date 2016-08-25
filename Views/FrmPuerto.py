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
## Class FrmPuerto
###########################################################################

class FrmPuerto(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Puerto", pos=wx.DefaultPosition, size=wx.Size(383, 105),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer34 = wx.BoxSizer(wx.VERTICAL)

        bSizer35 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Indique puerto donde se encuetra el dispositivo",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        bSizer35.Add(self.m_staticText17, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txtpuerto = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtpuerto.SetValue(Parametros.query.first().puerto)
        bSizer35.Add(self.txtpuerto, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer34.Add(bSizer35, 0, wx.EXPAND, 5)

        self.btnGuardar = wx.Button(self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer34.Add(self.btnGuardar, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer34)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btnGuardar.Bind(wx.EVT_BUTTON, self.btnGuardarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnGuardarOnButtonClick(self, event):
        puerto = self.txtpuerto.GetValue()
        p = Parametros.query.first()
        if(puerto != ''):
            p.puerto = puerto
            p.guardar()
            self.Close()


