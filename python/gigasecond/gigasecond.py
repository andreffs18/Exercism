from datetime import timedelta
def add_gigasecond(birth_date):
	gigasecond = 1000000000
	return birth_date + timedelta(seconds=gigasecond)
