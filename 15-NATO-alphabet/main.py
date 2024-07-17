import pandas

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
alphabet_dict = {row['letter']: row['code'] for (index, row) in phonetic_alphabet.iterrows()}
# print(alphabet_dict)


# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        result_dict = [alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result_dict)


generate_phonetic()
