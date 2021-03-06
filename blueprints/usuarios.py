from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Usuario
import json
import datetime

usuarios = Blueprint('usuarios', __name__ )

@usuarios.route('/todos')
def usuarios_all():
	usuarios = Usuario.select()
	lista_usuarios = [usuario.to_json() for usuario in usuarios]
	return json.dumps(lista_usuarios)

@usuarios.route('/<rpe>')
def usuario_info(rpe):
	try:
		usuario = Usuario.select().where(Usuario.rpe == rpe)
		return json.dumps(usuario[0].to_json()), 200
	except:
		return "Error!", 404

@usuarios.route('/nuevo', methods=['POST'])
def usuario_nuevo():
	try:
		Usuario.nuevo(
	    	rpe=request.form['rpe'],
	    	nombre=request.form['nombre'],
	    	puesto=request.form['puesto'],
	    	departamento=request.form['departamento'],
	    	correo=request.form['correo'],
	    	zona=request.form['zona'])
		return "OK!", 200
	except:
		return "Error!", 404

@usuarios.route('/<rpe>/borrar', methods=['DELETE'])
def usuario_borrar(rpe):
	try:
		usuario = Usuario.select().where(Usuario.rpe == rpe)
		if usuario is not None:
			usuario[0].delete()
			return "OK!", 200
		else:
			return "Error!", 404
	except:
		return "Error!", 404

@usuarios.route('/<rpe>/actualizar', methods=['PUT'])
def usuario_actualizar(rpe):
	try:
		usuario = Usuario.update(
			rpe=request.form['rpe'],
	    	nombre=request.form['nombre'],
	    	puesto=request.form['puesto'],
	    	departamento=request.form['departamento'],
	    	correo=request.form['correo'],
	    	zona=request.form['zona']).where(Usuario.rpe == rpe)
		usuario.execute()
		return "OK!", 200
	except:
		return "Error!", 404