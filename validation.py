def is_leap_year(_year: int) -> bool:
	"""
	Function that checks passed year value for being a leap year (29 of February).
	"""
	if (_year % 400 == 0) and (_year % 100 == 0):
		return True
	elif (_year % 4 ==0) and (_year % 100 != 0):
		return True
	else:
		return False

def is_date(_field: str) -> bool:
	"""
	Validation of Date field type.
	Formats:	'DD.MM.YYYY' or 'YYYY-MM-DD'.
	"""
	# Data preparation
	field = _field.split('.')
	if len(field) != 3:
		field = _field.split('-')
		if len(field) != 3:
			return False
		field.reverse()
	if not (len(field[0]) == 2 and len(field[1]) == 2):
		return False
	
	try:
		day, month, year = [int(x) for x in field]
	except ValueError:
		return False

	# Type validation
	if year > 0:
		if 1 <= month <= 12:
			if month == 2:
				return 1 <= day <= 28 + int(is_leap_year(year))
			else:
				return 1 <= day <= 30 + int(month in [1, 3, 5, 7, 8, 10, 12])
			
	return False


def is_phone(_field: str) -> bool:
	"""
	Validation of Phone field type.
	Formats:	'+7 XXX XXX XX XX'.
	"""
	part_length = [3, 3, 2, 2]

	field = _field.split()
	if len(field) != 5:
		return False
	if field[0] != '+7':
		return False
	
	for i in range(1, 5):
		if len(field[i]) != part_length[i - 1]:
			return False

	return True


def is_email(_field: str) -> bool:
	"""
	Validation of Email field type.
	Formats:	'name@service.domain'.
	"""
	field = _field.split('@')
	if len(field) != 2:
		return False
	if (len(field[0]) == 0) or (len(field[1]) == 0):
		return False
	
	field = field[1].split('.')
	if len(field) != 2:
		return False
	if (len(field[0]) == 0) or (len(field[1]) == 0):
		return False
	
	return True


def get_field_type(_field: str) -> str:
	"""
	Validation of field type.
	If field is neither a Date, Phone or Email -> it is a Text.
	"""
	if is_date(_field):
		return 'date'
	elif is_phone(_field):
		return 'phone'
	elif is_email(_field):
		return 'email'
	return 'text'