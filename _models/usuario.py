import datetime
from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash
from peewee import *

DATABASE = SqliteDatabase('../sistema_cfe.db')


class Usuario(UserMixin, Model):
    rpe = CharField(unique=True)
    nombre = CharField(max_length=100)
    puesto = CharField(max_length=100)
    departamento = CharField(max_length=100)
    correo = CharField(unique=True)
    #registro = DateTimeField(default=datetime.datetime.now)
    #admin = BooleanField(default=False)
    zona = CharField(max_length=20)

    class Meta:
        database = DATABASE
        #order_by = ('-registro',)

    @classmethod
    def nuevo(cls, rpe, nombre, puesto, departamento, correo, admin=False):
        try:
            cls.create(
                rpe=rpe,
                nombre=nombre,
                puesto=puesto,
                departamento=departamento,
                correo=correo,
                #admin=admin
            )
        except IntegrityError:
            raise ValueError("El usuario ya existe")

    def __repr__(self):
        return '{}'.format(self.nombre)

    def to_json(self):
        return {
            "rpe": self.rpe,
            "nombre": self.nombre,
            "puesto": self.puesto,
            "departamento": self.departamento,
            "correo": self.correo,
            #"admin": self.admin,
            "zona": self.zona
        }

    def evaluan(self):
        return (
            Usuario.select().join(
                PermisoEvaluar, on=PermisoEvaluar.evaluado).where(
                PermisoEvaluar.evaluador == self)
        )

    def evalua(self):
        return (
            Usuario.select().join(
                Evalua, on=Evalua.evaluador).where(
                Evalua.evaluado == self)
        )

    def superiores(self):
        puesto = Jerarquia.get(Jerarquia.nombre**self.puesto)
        return (
            Usuario.select().where(Usuario.puesto**puesto.superior)
        )

#
# sin tomar encuenta la zona o el departamento todavia
#

    def subordinados(self):
        puesto = Jerarquia.get(Jerarquia.superior**self.puesto)
        return (
            Usuario.select().where(Usuario.puesto**puesto.nombre)
        )