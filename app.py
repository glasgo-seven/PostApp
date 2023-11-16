#	Use Flask for creating a Web App - Place where POST requasts will be send.
from flask import Flask, request, json

#	Use TinyDB as a Database.
from tinydb import TinyDB

#	validation.py contains methods for validating field types.
import validation


APP_NAME	: str	= "POST receiver App"
APP			: Flask	= Flask(APP_NAME)

DB_NAME		: str		= 'db.json'
DATABASE	: TinyDB	= TinyDB(DB_NAME)

APP_HOST	: str	= '0.0.0.0'
APP_PORT	: int	= 5000


def find_template(_form : dict) -> str | dict:
	"""
	Function that compares Form Templates from Database
	to the passed POST Form.
	"""

	template_name	: str = None
	template_fields	: int = 0

	#	Make a dictionary with {field_name : field_type} pairs.
	typed_form = {}
	for field in _form:
		typed_form[field] = validation.get_field_type(_form[field])

	#	Search for a suitable Template.
	for template in DATABASE:
		#	Use len(template) - 1 for extra 'name' field in Template.
		#	It should be less or equal to len(typed_form) so every field in Template
		#		will be present in Form.
		if (len(template) - 1) <= len(typed_form):
			comparison = 0	#	Stores the amount of identical fields in Template and Form.

			for field in template:
				if not field == 'name':
					#	Try to access the same field in Template and Form.
					#	If successful:	add to comparison value;
					#	Else:			no longer check current Template.
					try:
						if template[field] == typed_form[field]:
							comparison += 1
					except KeyError:
						break
			
			#	If all field of the Template are found in the Form
			#	AND
			#	Current Template hold more identical fields then the previous suitable Template
			if (comparison == (len(template) - 1)) and (comparison > template_fields):
				#	Save the Template name
				template_name = template['name']
				template_fields = comparison
	
	return template_name if template_name != None else typed_form


@APP.route('/')
def index() -> None:
	return '<h1>Server is OnLine!</h1>'

@APP.route('/get_form', methods=['POST'])
def get_form() -> str | dict:
	"""
	Function that process POST requests to '/get_form' URL.
	"""
	#	If INPUT is already a structured JSON.
	if request.is_json:
		data = json.loads(request.data)
	#	Else INPUT is considered to be a STR of stucture "key1=value1&key2=value2".
	else:
		#	Create a Dictionary from STR contents.
		data = {}
		for pair in request.data.decode().split('&'):
			key, value = pair.split('=')
			data[key] = value
	
	return find_template(data)


if __name__ == '__main__':
	APP.run(debug=True, host=APP_HOST, port=APP_PORT)
