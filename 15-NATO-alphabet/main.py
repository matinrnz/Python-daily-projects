import pandas

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
alphabet_dict = {row['letter']: row['code'] for (index, row) in phonetic_alphabet.iterrows()}
# print(alphabet_dict)
# Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
result_dict = [alphabet_dict[letter] for letter in user_word]
print(result_dict)
