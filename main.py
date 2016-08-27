# -*- coding: utf-8 -*-
#####################################################
#
# 	Aplicación Semáforo 
#	Yasser Mussa <yasser.mussa@gmail.com.>
#	Cel. 091336302
#
#####################################################

import wx

from Views.FrmMain import FrmMain

#puerto = serial.Serial('COM4', 9600)

if __name__ == "__main__":
    app = wx.App(False)
    frame = FrmMain(None)
    frame.Show()
    app.MainLoop()
