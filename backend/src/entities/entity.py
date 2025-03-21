# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Asegúrate de tener pymysql instalado: pip install pymysql
db_url = 'localhost:3306'  # Asegúrate de que el puerto sea el correcto para MySQL
db_name = 'usuarios'
db_user = 'root'  # Eliminado espacio en blanco innecesario
db_password = 'ROOT'
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Entity(Base):  # Asegúrate de heredar de Base
    __tablename__ = 'entities'  # Define el nombre de la tabla

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String(100))  # Especifica la longitud del VARCHAR

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
 
