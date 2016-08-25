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


###########################################################################
## Class FrmPulsaciones
###########################################################################

class FrmPulsaciones(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(708, 454), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.list = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.list, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.btnAceptar = wx.Button(self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.btnAceptar, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        bSizer7.Add(bSizer8, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        self.btnAceptar.Bind(wx.EVT_BUTTON, self.btnAceptarOnButtonClick)

    def __del__(self):
        pass

    def btnAceptarOnButtonClick(self, event):
        self.Close()
