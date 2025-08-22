def count_vowels(text = input("Enter text:\n>>> ").lower(), vowels="aeiou"):
	number_vowels = 0
	for char in text:
	
		if char in vowels:
			number_vowels += 1
	return number_vowels
print(count_vowels())

