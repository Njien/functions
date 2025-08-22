def check_password_strength(password = input("Enter Password:\n>>> ")):
	letters = "abcdefghijklmnopqrstuvwxyz"
	numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
	is_number = False
	is_letter = False
	for number in numbers:
		if number in password:
			is_number = True

	for letter in letters:
		if letter in password:
			is_letter = True

	if len(password) > 10 and is_number and is_letter:
		return "Strong"
	elif len(password) >= 6 and len(password) <= 10:
		return "Medioum"
	elif len(password) < 6:
		return "Weak"

print(check_password_strength())
	
