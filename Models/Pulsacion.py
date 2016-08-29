from Models.connector import db

class Pulsacion(db.Model):
    __tablename__ = 'pulsaciones'

    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.Date)
    pulsacion = db.Column(db.Integer)
    premio_id = db.Column(db.Integer)

    def guardar(self):
        db.session.add(self)
        db.session.commit()