text = input()
vowels = {'a', 'o', 'u', 'e', 'i'}
no_vowels_text = [char for char in text if char.lower() not in vowels]
print(''.join(no_vowels_text))