# TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt", mode="r") as letter_data:
    letter = letter_data.read()

# for each name in invited_names.txt
with open("Input/Names/invited_names.txt", mode="r")as names_data:
    names = names_data.readlines()
    # Remove newline characters
    names_list = [name.strip() for name in names]

for name in names_list:
    # Create a file name.
    filename = f"../__MACOSX/Mail Merge Project Start/Output/ReadyToSend/{name}-letter.txt"
    # Replace the [name] placeholder with the actual name.
    new_letter = letter.replace("[name]", name)
    # Save the letters in the folder "ReadyToSend".
    with open(filename, mode="w") as file:
        file.write(new_letter)
print("Files created successfully.")
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
