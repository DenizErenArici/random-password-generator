import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

chosen_letters=[]
chosen_symbols=[]
chosen_numbers=[]

random_index_letter=[]
random_index_symbols=[]
random_index_numbers=[]
for i in range(0,nr_letters):
    random_index_letter.append(random.randint(0,len(letters)-1))
for j in range(0,nr_numbers):
    random_index_numbers.append(random.randint(0,len(numbers)-1))
for k in range(0,nr_symbols):
    random_index_symbols.append(random.randint(0,len(symbols)-1))

for index_letter in random_index_letter:
    chosen_letters.append(letters[index_letter])
for index_number in random_index_numbers:
    chosen_numbers.append(numbers[index_number])
for index_symbol in random_index_symbols:
    chosen_symbols.append(symbols[index_symbol])

characters=[]
characters.extend(chosen_letters)
characters.extend(chosen_numbers)
characters.extend(chosen_symbols)
def shuffle(characters):
    characters_length = len(characters)
    for i in range(characters_length - 1, 0, -1):
        j = random.randint(0, i)
        characters[i], characters[j] = characters[j], characters[i]
shuffle(characters)
print(f'Your password is: {"".join(characters)} ')
