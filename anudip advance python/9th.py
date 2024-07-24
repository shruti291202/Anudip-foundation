# Write content to the file
file = open("notes.txt", 'w')
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Hello python .\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()

# Open the file in read mode
file = open('notes.txt', 'r')

# Read the content of the file
data = file.readlines()

# Iterate over each line in the file content
for line in data:
    # Split the line into words and check if it has more than 5 words
    if len(line.split()) > 5:
        print(line.strip())

# Close the file
file.close()