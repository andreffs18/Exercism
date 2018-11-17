def hey(phrase):
	# clean any whitespaces 
	phrase = phrase.strip()

	if not phrase:
		return 'Fine. Be that way!'
	
	is_upper = phrase.isupper()
	has_question_mark = phrase.endswith("?")

	if is_upper and has_question_mark:
		return 'Calm down, I know what I\'m doing!'

	if has_question_mark:
		return 'Sure.'

	if is_upper:
		return 'Whoa, chill out!'

	return 'Whatever.'
