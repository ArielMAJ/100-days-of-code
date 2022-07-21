#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_letter_path = "./Input/Letters/starting_letter.txt"
names_path = "./Input/Names/invited_names.txt"
output_path = "./Output/ReadyToSend/"

with open(starting_letter_path) as f:
    text = f.read()
with open(names_path) as f:
    names = f.read().split('\n')

old_word = "[name]"
# print()
for name in names:
    with open(output_path + f"letter_for_{name}.txt", 'w') as f:
        f.write(text.replace(old_word, name))
