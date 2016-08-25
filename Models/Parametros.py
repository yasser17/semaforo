from Models.connector import db

class Parametros(db.Model):
    __tablename__ = "parametros"

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)
    puerto = db.Column(db.String)

    def guardar(self):
        db.session.add(self)
        db.session.commit()