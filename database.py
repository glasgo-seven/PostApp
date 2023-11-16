#	Use TinyDB as a Database.
from tinydb import TinyDB

DB_NAME = '../db.json'

FIELD_TYPES = [
	'date',
	'phone',
	'email',
	'text',
]

TEMPLATES = [
	{
		'name'		:	'Phone Number Form',

		'number'	:	'phone',
	},
	{
		'name'		:	'Note Form',

		'note'		:	'text',
	},
	{
		'name'		:	'Contact Form',

		'pochta'	:	'email',
		'telephone'	:	'phone',
	},
	{
		'name'		:	'Work Contact Form',

		'number'	:	'phone',
		'work email':	'email',
	},
	{
		'name'		:	'Email Message Form',

		'eMail'		:	'email',
		'message'	:	'text',
	},
	{
		'name'		:	'Blog Post Form',

		'date'		:	'date',
		'post'		:	'text',
	},
	{
		'name'		:	'Event Form',

		'date'		:	'date',
		'title'		:	'text',
	},
	{
		'name'		:	'Phone Message Form',

		'message'	:	'text',
		'number'	:	'phone',
	},
	{
		'name'		:	'Birthday Form',
		
		'birthday'	:	'date',
		'number'	:	'phone',
	},
	{
		'name'		:	'Blog Post with Author Form',

		'author'	:	'email',
		'date'		:	'date',
		'post'		:	'text',
	},

]


if __name__ == '__main__':
	# Init db
	with TinyDB(DB_NAME) as database:
		# Clean db entries
		database.truncate()

		# Add template data
		for item in TEMPLATES:
			database.insert(item)

		# Print db contents
		for item in database:
			print(item)
