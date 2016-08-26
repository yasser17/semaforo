# -*- coding: utf-8 -*-

import serial
import wx
import wx.xrc

from Models.Pulsacion import Pulsacion
from Models.Premio import Premio
from Models.Parametros import Parametros
from Models.semana import Semana
import datetime
from sqlalchemy import desc

def recepcion():
    puerto = str(Parametros.query.first().puerto)

    semanas = Semana.query.all()
    for s in semanas:
        if(s.fechaInicio < datetime.datetime.now().date()):
            s.estado_id = 1
        if(s.fechaInicio <= datetime.datetime.now().date() and s.fechaFin >= datetime.datetime.now().date()):
            s.estado_id = 2
        if(s.fechaFin < datetime.datetime.now().date()):
            s.estado_id = 3
        s.guardar();

    try:
        arduino = serial.Serial(puerto, 9600)
        last = None
        while True:
            res = arduino.readline()
            if(res == "pulsacion\r\n"):
                last = Pulsacion.query.filter_by(dia=datetime.datetime.now().date().strftime('%Y-%m-%d')).order_by(desc(Pulsacion.id)).first()
                if(last is not None):
                    pul = last.pulsacion + 1
                else:
                    pul = 1
                premio = None;
                premio = Premio.query.filter_by(fecha=datetime.datetime.now().date().strftime('%Y-%m-%d'), numero=pul).first();
                p = Pulsacion()
                if(premio):
                    p.premio_id = premio.id
                p.dia = datetime.datetime.now().date()
                p.pulsacion = pul
                p.guardar()
                if(premio):
                    C = premio.color
                    arduino.write(str(C))
                else:
                    arduino.write("P")
            else:
                print res
    except:
        print "No se puede conectar el dispositivo"