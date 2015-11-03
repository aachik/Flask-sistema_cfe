from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Preguntas
import json
import datetime


preguntas = Blueprint('preguntas', __name__ )

<<<<<<< HEAD
@preguntas.route('/todos')
def preguntas_todas():from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Preguntas
import json
import datetime

preguntas = Blueprint('preguntas', __name__ )

@preguntas.route('/todos')
def preguntas_todas():
	pass
=======
@preguntas.route('/todas')
def preguntas_all():
	preguntas = Preguntas.select()
	lista_preguntas = [Preguntas.to_json() for pregunta in preguntas]
	return json.dumps(lista_preguntas)

@preguntas.route('/<id>')
def pregunta_info(id):
	try:
		pregunta = Preguntas.select().where(Preguntas.id == id)
		return json.dumps(pregunta[0].to_json()), 200
	except:
		return "Error!", 404
>>>>>>> Alejandra

@preguntas.route('/nueva', methods=['POST'])
def pregunta_nuevo():
	try:
		Preguntas.create(
	    	competencia=request.form['competencia'], #este debe ser el ID de la competencia por cierto, es una foreignKey
	    	pregunta=request.form['pregunta'])
		return "OK!", 200
	except:
		return "Error!", 404

@preguntas.route('/<id>/borrar', methods=['DELETE'])
def pregunta_borrar(id):
	try:
		pregunta = Preguntas.select().where(Preguntas.id == id)
		if pregunta is not None:
			pregunta[0].delete()
			return "OK!", 200
		else:
			return "Error!", 404
	except:
		return "Error!", 404

<<<<<<< HEAD
@preguntas.route('/<int:id>/actualizar', methods=['PUT'])
def preguntas_actualizar(id):
	pass

	pass

@preguntas.route('/nueva', methods=['POST'])
def preguntas_nueva():
	pass
	
@preguntas.route('/<int:id>')
def preguntas_info(id):
	pass

@preguntas.route('/<int:id>/borrar', methods=['DELETE'])
def preguntas_borrar(id):
	pass

@preguntas.route('/<int:id>/actualizar', methods=['PUT'])
def preguntas_actualizar(id):
	pass

=======
@preguntas.route('/<id>/actualizar', methods=['PUT'])
def pregunta_actualizar(id):
	try:
		pregunta = Preguntas.update(
	    	competencia=request.form['competencia'], #aqui igual, esta es la ID de la competencia
	    	pregunta=request.form['pregunta']).where(Preguntas.id == id)
		Preguntas.execute()
		return "OK!", 200
	except:
		return "Error!", 404
>>>>>>> Alejandra
