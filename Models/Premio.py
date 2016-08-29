from Models.connector import db

class Premio(db.Model):
    __tablename__ = 'premios'

    id = db.Column(db.Integer, primary_key=True)
    semana_id = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)
    numero = db.Column(db.Integer)
    color = db.Column(db.String)
    descripcion = db.Column(db.String)
    obsequiado = db.Column(db.DateTime)

    def get_dia(self):
        if (self.fecha.weekday() == 0):
            dia = "Lunes"
        if (self.fecha.weekday() == 1):
            dia = "Martes"
        if (self.fecha.weekday() == 2):
            dia = "Miercoles"
        if (self.fecha.weekday() == 3):
            dia = "Jueves"
        if (self.fecha.weekday() == 4):
            dia = "Viernes"
        if (self.fecha.weekday() == 5):
            dia = "Sabado"
        if (self.fecha.weekday() == 6):
            dia = "Domingo"
        return dia

    def get_color(self):
        if(self.color == "V"):
            return "Verde"
        if(self.color == "A"):
            return "Amarillo"
        if(self.color == "R"):
            return "Rojo"

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def modificar(self):
        db.session.commit()

    def borrar(self):
        db.session.delete(self)
        db.session.commit()