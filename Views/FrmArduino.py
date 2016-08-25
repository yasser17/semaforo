# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import serial
from multiprocessing import Pool


###########################################################################
## Class FrmArduino
###########################################################################

class FrmArduino(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(255, 259), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.btnRecibir = wx.Button(self, wx.ID_ANY, u"Esperar Señal", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.btnRecibir, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btnMandar = wx.Button(self, wx.ID_ANY, u"Enviar ", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.btnMandar, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        self.puerto = serial.Serial('COM4', 9600)

        # Connect Events
        self.btnRecibir.Bind(wx.EVT_BUTTON, self.btnRecibirOnButtonClick)
        self.btnMandar.Bind(wx.EVT_BUTTON, self.btnMandarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnRecibirOnButtonClick(self, event):
        pool = Pool(processes=1)
        pool.apply_async(self.esperar)

    def btnMandarOnButtonClick(self, event):
        event.Skip()


    def esperar(self):
        while (True):
            res = self.puerto.readline()
            print res