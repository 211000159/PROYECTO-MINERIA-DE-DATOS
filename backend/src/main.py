from flask import Flask, jsonify, request
from .entities.entity import Session, engine, Base
from .entities.exam import Exam, Usuario, ExamSchema, UsuarioSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS
Base.metadata.create_all(engine)

@app.route('/exams', methods=['GET'])
def get_exams():
    session = Session()
    exam_objects = session.query(Exam).all()

    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    session.close()
    return jsonify(exams)

    
    
@app.route('/login1', methods=['POST'])
def login_get():
    # Obtener parámetros desde la URL
    email = request.args.get('email')
    password = request.args.get('password')

    # Validar que los campos no estén vacíos
    if not email or not password:
        return jsonify({'message': 'Por favor complete todos los campos.'}), 400

    # Crear una sesión para la consulta
    session = Session()
    try:
        # Consultar la base de datos para validar el usuario
        usuario = session.query(Usuario).filter_by(correo=email, contraseña=password).first()

        if usuario:
            return jsonify({'message': f'Inicio de sesiOn exitoso. Bienvenido {usuario.nombrecompleto}!'}), 200
        else:
            return jsonify({'message': 'Credenciales incorrectas.'}), 401
    except Exception as e:
        return jsonify({'message': f'Error en el servidor: {str(e)}'}), 500
   
        
        
        
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    session = Session()
    usuarios = session.query(Usuario).all()

    schema = UsuarioSchema(many=True)
    usuarios_serializados = schema.dump(usuarios)

    session.close()
    return jsonify(usuarios_serializados)

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

@app.route('/usuarios', methods=['POST'])
def add_usuario():
    posted_Usuario = UsuarioSchema(only=('id', 'username', 'contraseña', 'correo', 'nombrecompleto')).load(request.get_json())
    usuario = Usuario(**posted_Usuario, created_by="HTTP post request")  # Corregido aquí

    session = Session()
    session.add(usuario)
    session.commit()

    new_usuario = UsuarioSchema().dump(usuario)
    session.close()
    return jsonify(new_usuario), 201
