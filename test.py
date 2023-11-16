#	Use requests for making POST requests to the Web App.
import requests

#	As for running the Web App locally the URL for POST will be this.
POST_URL	= f'http://localhost:5000/get_form'


TEST_DATA = [
	#	Phone Number Form
	[
		{
			'number'	:	'+7 909 909 99 00',
		},
		'Phone Number Form',
	],
	[
		'number=+7 909 909 99 00',
		'Phone Number Form',
	],
	[
		{
			'number'	:	'+7 (909) 909 99 00',
		},
		'{\n  "number": "text"\n}\n',
	],
	[
		{
			'number'	:	'8 909 909 99 00',
		},
		'{\n  "number": "text"\n}\n',
	],
	[
		{
			'number'	:	'+79099099900',
		},
		'{\n  "number": "text"\n}\n',
	],
	[
		{
			'number'	:	'+7 909 909',
		},
		'{\n  "number": "text"\n}\n',
	],
	
	#	Note Form
	[
		{
			'note'		:	'THIS IS A NOTE~!!!',
		},
		'Note Form',
	],
	[
		{
			'nota'		:	'THIS IS A NOT-A~!!!',
		},
		'{\n  "nota": "text"\n}\n',
	],
	[
		{
			'note'		:	'THIS IS A NOTE~!!!',
			'nota'		:	'THIS IS A NOT-A~!!!',
		},
		'Note Form',
	],
	
	#	Contact Form
	[
		{
			'pochta'		:	'test@test.com',
			'telephone'		:	'+7 909 909 99 00',
		},
		'Contact Form',
	],
	[
		{
			'email'			:	'test@test.com',
			'telephone'		:	'+7 909 909 99 00',
		},
		'{\n  "email": "email",\n  "telephone": "phone"\n}\n',
	],
	[
		{
			'pochta'		:	'test@test.com',
			'telephone'		:	'+79099099900',
		},
		'{\n  "pochta": "email",\n  "telephone": "text"\n}\n',
	],
	[
		{
			'pochta'		:	'@test.com',
			'telephone'		:	'+7 909 909 99 00',
		},
		'{\n  "pochta": "text",\n  "telephone": "phone"\n}\n',
	],
	[
		'pochta=@test.com&telephone=+7 909 909 99 00',
		'{\n  "pochta": "text",\n  "telephone": "phone"\n}\n',
	],
	[
		{
			'pochta'		:	'test@test.com',
			'telephone'		:	'+7 909 909 99 00',
			'text'			:	'Lorem Ipsum',
		},
		'Contact Form',
	],
	
	#	Work Contact Form
	[
		{
			'number'		:	'+7 909 909 99 00',
			'work email'	:	'work@test.com',
		},
		'Work Contact Form',
	],
	[
		{
			'number'		:	'+7 909 909 99 00',
			'work email'	:	'@test.com',
		},
		'Phone Number Form',
	],
	[
		{
			'number'		:	'+7(909)909 99 00',
			'work email'	:	'test@test.com',
		},
		'{\n  "number": "text",\n  "work email": "email"\n}\n',
	],
	[
		{
			'work email'	:	'test@test.com',
			'work number'	:	'+7 909 909 99 00',
		},
		'{\n  "work email": "email",\n  "work number": "phone"\n}\n',
	],
	[
		{
			'number'		:	'+7 909 909 99 00',
			'work email'	:	'test@test.com',
			'employee'		:	'Adam Adams',
		},
		'Work Contact Form',
	],

	#	Email Message Form
	[
		{
			'eMail'		:	'test@test.com',
			'message'	:	'Hello!',
		},
		'Email Message Form',
	],
	[
		{
			'eMail'		:	'@test.com',
			'message'	:	'Hello!',
		},
		'{\n  "eMail": "text",\n  "message": "text"\n}\n',
	],
	[
		{
			'Mail'		:	'test@test.com',
			'text'		:	'Hello!',
		},
		'{\n  "Mail": "email",\n  "text": "text"\n}\n',
	],
	
	#	Blog Post Form
	[
		{
			'date'		:	'22.11.1122',
			'post'		:	'Hello!',
		},
		'Blog Post Form',
	],
	[
		{
			'date'		:	'1122-11-22',
			'post'		:	'Hello!',
		},
		'Blog Post Form',
	],
	[
		{
			'date'		:	'11/12/1122',
			'post'		:	'Hello!',
		},
		'{\n  "date": "text",\n  "post": "text"\n}\n',
	],
	[
		{
			'data'		:	'11.12.1122',
			'post'		:	'Hello!',
		},
		'{\n  "data": "date",\n  "post": "text"\n}\n',
	],
	[
		{
			'date'		:	'11.12.1122',
			'post'		:	'Hello!',
			'birth'		:	'11.12.1122',
		},
		'Blog Post Form',
	],
	
	#	Event Form
	[
		{
			'date'		:	'11.12.1122',
			'title'		:	'Party!',
		},
		'Event Form',
	],
	[
		{
			'date'		:	'11.12.1122',
			'titles'	:	'Party!',
		},
		'{\n  "date": "date",\n  "titles": "text"\n}\n',
	],
	
	#	Phone Message Form
	[
		{
			'message'	:	'Meet me!',
			'number'	:	'+7 909 909 99 00',
		},
		'Phone Message Form',
	],
	[
		{
			'message'	:	'Meet me!',
			'author'	:	'Adam',
			'number'	:	'+7 909 909 99 00',
		},
		'Phone Message Form',
	],
	[
		{
			'messages'	:	'Meet me!',
			'number'	:	'+7 909 909 99 00',
		},
		'Phone Number Form',
	],
	[
		{
			'message'	:	'Meet me!',
			'number'	:	'+7 909 9099900',
		},
		'{\n  "message": "text",\n  "number": "text"\n}\n',
	],
	
	#	Birthday Form
	[
		{
			'birthday'	:	'22.11.1122',
			'number'	:	'+7 909 909 99 00',
		},
		'Birthday Form',
	],
	[
		{
			'date'	:	'22.11.1122',
			'number'	:	'+7 909 909 99 00',
		},
		'Phone Number Form',
	],
	[
		{
			'birthday'	:	'22/11/1122',
			'number'	:	'+7 909 909 99 00',
		},
		'Phone Number Form',
	],
	[
		{
			'birthday'	:	'22.11.1122',
			'number'	:	'+7 909 909 99 00',
			'nameday'	:	'2000-01-01'
		},
		'Birthday Form',
	],
	
	#	Blog Post with Author Form
	[
		{
			'author'	:	'author@blog.com',
			'date'		:	'22.11.1122',
			'post'		:	'I love cats!',
		},
		'Blog Post with Author Form',
	],
	[
		{
			'author'	:	'author',
			'date'		:	'22.11.1122',
			'post'		:	'I love cats!',
		},
		'Blog Post Form',
	],
	[
		{
			'author'	:	'author@blog.com',
			'date'		:	'22/11/1122',
			'post'		:	'I love cats!',
		},
		'{\n  "author": "email",\n  "date": "text",\n  "post": "text"\n}\n',
	],
	[
		{
			'author'	:	'author',
			'date'		:	'22.11.1122',
			'post'		:	'I love cats!',
			'title'		:	'Who loves cats?',
		},
		'Blog Post Form',
	],
	[
		{
			'author'	:	'author',
			'date'		:	'22/11/1122',
			'post'		:	'I love cats!',
			'title'		:	'Who loves cats?',
		},
		'{\n  "author": "text",\n  "date": "text",\n  "post": "text",\n  "title": "text"\n}\n',
	],
	[
		'author=author&date=22/11/1122&post=I love cats!&title=Who loves cats?',
		'{\n  "author": "text",\n  "date": "text",\n  "post": "text",\n  "title": "text"\n}\n',
	],
]


#	OUTPUT formatting
COLOR_RED		= '\x1b[31m'
COLOR_GREEN		= '\x1b[32m'
COLOR_RESET		= '\x1b[0m'
SIGN_CORRECT	= '✅'
SIGN_WRONG		= '❌'

def send_test_forms() -> None:
	"""
	Function that sends all the Test data to the Web App and compares it to the expected output.
	"""
	test_number = 0
	for form, answer in TEST_DATA:
		test_number += 1

		if type(form) is str:
			POST = requests.post(POST_URL, data = form).text
		else:
			POST = requests.post(POST_URL, json = form).text

		print(f'{test_number}. ' + '-' * 32, f'\nINPUT:\n{form}', f'\nOUTPUT:\n{POST}', f'\nEXPECTED:\n{answer}')

		if POST != answer:
			print(f'RESULT: {SIGN_WRONG} {COLOR_RED}WRONG{COLOR_RESET}:\t"{POST}" != "{answer}"\n')
		else:
			print(f'RESULT: {SIGN_CORRECT} {COLOR_GREEN}Correct{COLOR_RESET}')

if __name__ == '__main__':
	send_test_forms()
