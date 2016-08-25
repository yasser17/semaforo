# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.calendar
import datetime
from Models.semana import Semana


###########################################################################
## Class FrmSemana
###########################################################################

class FrmSemana(wx.Dialog):
    semana = None;
    def __init__(self, parent, xSemana):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Semana", pos=wx.DefaultPosition, size=wx.Size(275, 300),
                           style=wx.DEFAULT_DIALOG_STYLE)
        if(xSemana != None):
            self.semanaId  = xSemana
            self.semana = Semana.query.get(self.semanaId)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Seleccione Fecha", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer6.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.calendario = wx.calendar.CalendarCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                   wx.DefaultSize, wx.calendar.CAL_SHOW_HOLIDAYS)
        if(xSemana != None):
            dia = self.semana.fechaInicio.day
            mes = self.semana.fechaInicio.month
            year = self.semana.fechaInicio.year
            fecha = wx.DateTimeFromDMY(dia, mes -1, year)
            self.calendario.SetDate(fecha)

        bSizer6.Add(self.calendario, 0, wx.ALL, 5)

        self.error = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.error.Wrap(-1)
        bSizer6.Add(self.error, 0, wx.ALL, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.btnAceptar = wx.Button(self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.btnAceptar, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer6.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btnAceptar.Bind(wx.EVT_BUTTON, self.btnAceptarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btnAceptarOnButtonClick(self, event):
        fecha = self.calendario.GetDate()
        Obj = fecha.Format('%m/%d/%y')
        ObjFecha = datetime.datetime.strptime(Obj, '%m/%d/%y')
        #if(ObjFecha < datetime.datetime.now()):
        #    self.error.SetLabel(u'La fecha no puede ser anterior a la actual')
        #    return False
        if(ObjFecha.weekday() != 0):
            self.error.SetLabel(u'Debe selecionar un lunes como fecha')
            return False
        existe = None
        existe = Semana.query.filter_by(fechaInicio=ObjFecha).first()
        if(existe is not None):
            self.error.SetLabel(u'Esa fecha ya fue seleccionada')
            return False

        if(self.semana != None):
            self.semana.fechaInicio = ObjFecha
            self.semana.fechaFin = ObjFecha + datetime.timedelta(days=6)
            self.semana.modificar()
        else:
            s = Semana()
            s.fechaInicio = ObjFecha
            s.fechaFin = ObjFecha + datetime.timedelta(days=6)
            s.estado_id = 1
            s.guardar()
        self.Close()
