from flask import Flask, jsonify, request
from .entities.entity import Session, engine, Base
from .entities.exam import Exam,Usuario, ExamSchema,UsuarioSchema

app = Flask(__name__)
Base.metadata.create_all(engine)

@app.route('/exams')
def get_exams():
    session = Session()
    exam_objects = session.query(Exam).all()

    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    session.close()
    return jsonify(exams)

@app.route('/usuarios')
def get_usuarios():
    session = Session()  # Abrir una sesión con la base de datos
    usuarios = session.query(Usuario).all()  # Consultar todos los usuarios

    schema = UsuarioSchema(many=True)  # Serializar los datos
    usuarios_serializados = schema.dump(usuarios)  # Convertir a JSON

    session.close()  # Cerrar la sesión
    return jsonify(usuarios_serializados)  # Devolver los datos como JSON

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/exams', methods=['POST'])
def add_exam():
    posted_exam = ExamSchema(only=('title', 'description')).load(request.get_json())

    exam = Exam(**posted_exam, created_by="HTTP post request")

    session = Session()
    session.add(exam)
    session.commit()

    new_exam = ExamSchema().dump(exam)
    session.close()
    return jsonify(new_exam), 201
