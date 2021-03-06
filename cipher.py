from string import ascii_lowercase, ascii_uppercase


def get_new_letter(letter_case, letter, step):
	new_index = letter_case.index(letter) + step
	if new_index > len(letter_case) - 1 or new_index < 0:
		new_index = (letter_case.index(letter) + step ) % len(letter_case)
	new_letter = letter_case[new_index]
	return new_letter


def next_letter(letter, step):
	"""
	'A' -> 'B'
	'a' -> 'b'
	'Z' -> 'A'
	'z' -> 'a'
	"""

	if letter in ascii_uppercase:
		new_letter = get_new_letter(ascii_uppercase, letter, step)
	elif letter in ascii_lowercase:
		new_letter = get_new_letter(ascii_lowercase, letter, step)
	else:
		new_letter = letter
	return new_letter


def prev_letter(letter, step):
	"""
	'B' -> 'A'
	'b' -> 'a'
	'A' -> 'Z'
	'a' -> 'z'
	"""

	if letter in ascii_uppercase:
		new_letter = get_new_letter(ascii_uppercase, letter, -step)
	elif letter in ascii_lowercase:
		new_letter = get_new_letter(ascii_lowercase, letter, -step)
	else:
		new_letter = letter
	return new_letter


def encode(text, step):
	"""
	"Hello world" -> "Ifmmp xpsme"
	"""
	encoded_text = ''
	for letter in text:
		encoded_text += next_letter(letter, step)
	return encoded_text


def decode(text, step):
	"""
	"Ifmmp xpsme" -> "Hello world" 
	"""
	decoded_text = ''
	for letter in text:
		decoded_text += prev_letter(letter, step)
	return decoded_text


def main():
	# check
	text = 'Hello world'
	step = 1
	encoded_text = encode(text, step)
	print(encoded_text)
	decoded_text = decode(encoded_text, step)
	print(decoded_text)


if __name__ == '__main__':
	main()