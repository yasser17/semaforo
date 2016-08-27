# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class FrmAbout
###########################################################################

class FrmAbout(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Semáforo", pos=wx.DefaultPosition,
                           size=wx.Size(529, 234), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        bSizer37 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"Aplicación Sorteo", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText18.Wrap(-1)
        self.m_staticText18.SetFont(wx.Font(20, 74, 90, 90, False, "Sans"))

        bSizer37.Add(self.m_staticText18, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer36.Add(bSizer37, 0, wx.EXPAND, 5)

        bSizer38 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"Aplicación para promoción de empresa COSALCO ", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        bSizer38.Add(self.m_staticText20, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"Desarrollado por Yasser Mussa", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        bSizer38.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, u"Correo Electrónico: yasser.mussa@gmail.com",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        bSizer38.Add(self.m_staticText22, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"Celular: 091336302", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText23.Wrap(-1)
        bSizer38.Add(self.m_staticText23, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer36.Add(bSizer38, 1, wx.EXPAND, 5)

        bSizer39 = wx.BoxSizer(wx.VERTICAL)

        self.btnSalir = wx.Button(self, wx.ID_ANY, u"&Salir", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer39.Add(self.btnSalir, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer36.Add(bSizer39, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer36)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btnSalir.Bind(wx.EVT_BUTTON, self.btnSalirOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnSalirOnButtonClick(self, event):
        self.Close()