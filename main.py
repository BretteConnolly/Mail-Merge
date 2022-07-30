PLACEHOLDER = "name" #appears on original letter template

#list of names
with open ("mail-merge-project-start/Input/Names/invited_names.txt") as names_file:
  names = names_file.readlines() 

with open ("mail-merge-project-start/Input/Letters/starting_letter.txt") as letter_file: #letter template
  letter_contents = letter_file.read()
  for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) #replaces the "name" placeholder with the person's name
    with open (f"mail-merge-project-start/Input/Output/ReadyToSend/{stripped_name}.txt", "w") as completed_letter:
      completed_letter.write(new_letter) #creates a new letter for each person