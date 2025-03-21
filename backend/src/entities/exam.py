

from sqlalchemy import Column, String, ForeignKey, Integer
from .entity import Entity, Base
from marshmallow import Schema, fields

class Exam(Entity, Base):
    __tablename__ = 'exams'
    id = Column(Integer, ForeignKey('entities.id'), primary_key=True)  # Clave foránea que referencia a 'entities'
    title = Column(String(100))  # Especifica la longitud del VARCHAR
    description = Column(String(255))  # Especifica la longitud del VARCHAR
    
    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
class Usuario(Base):
    __tablename__ = 'usuario'  # Nombre de la tabla existente en la base de datos

    id = Column(Integer, primary_key=True)  # Identificador principal
    username = Column(String(45))
    nombrecompleto = Column(String(45))  # Nombre del usuario
    correo = Column(String(45))  # Correo electrónico
    contraseña = Column(String(45))  # Rol del usuario
    
class UsuarioSchema(Schema):
    id = fields.Number()
    username = fields.Str()
    nombrecompleto = fields.Str()
    correo = fields.Str()
    contraseña = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
    
class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
    