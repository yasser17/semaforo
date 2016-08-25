import datetime

from Models.connector import db


class Semana(db.Model):
    __tablename__ = 'semanas'
    id = db.Column(db.Integer, primary_key=True)
    fechaInicio = db.Column(db.DateTime)
    fechaFin = db.Column(db.DateTime)
    estado_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def modificar(self):
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

    def Estado(self):
        if (self.estado_id == 1):
            estado = "Pendiente"
        if (self.estado_id == 2):
            estado = "En Proceso"
        if (self.estado_id == 3):
            estado = "Finalizado"
        if (self.estado_id == 4):
            estado = "Cancelado"
        return estado