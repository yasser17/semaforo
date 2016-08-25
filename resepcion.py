import serial
from Models.Pulsacion import Pulsacion
from Models.Premio import Premio
from Models.Parametros import Parametros
import datetime
from sqlalchemy import desc
puerto = str(Parametros.query.first().puerto)

arduino = serial.Serial(puerto, 9600)
last = None
while True:
    res = arduino.readline()
    if(res == "pulsacion\r\n"):
        last = Pulsacion.query.filter_by(dia=datetime.datetime.now().strftime('%Y-%m-%d')).order_by(desc(Pulsacion.id)).first()
        if(last is not None):
            pul = last.pulsacion + 1
        else:
            pul = 1
        premio = None;
        premio = Premio.query.filter_by(fecha=datetime.datetime.now().strftime('%Y-%m-%d'), numero=pul).first();
        p = Pulsacion()
        if(premio):
            p.premio_id = premio.id
        p.dia = datetime.datetime.now()
        p.pulsacion = pul
        p.guardar()
        if(premio):
            C = premio.color
            arduino.write(str(C))
        else:
            arduino.write("P")
    else:
        print res
