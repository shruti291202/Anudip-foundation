# Write content to the file
file = open("file.txt", 'w')
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()

# Open the file in read mode
file = open('file.txt', 'r')

# Read the content of the file
data = file.read()

# Split the content into words
words = data.split()

# Initialize the counter for words starting with 'i'
count_i = 0

# Iterate over the words and count those starting with 'i'
for word in words:
    if word[0].lower() == 'i':
        count_i += 1
        print(word)

# Print the count
print("Number of words starting with 'i':", count_i)

# Close the file
file.close()