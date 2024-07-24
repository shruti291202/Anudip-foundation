# Write content to the file
file = open("Myfile.txt", 'a')
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Hello , welcome to the python class.\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()

# Open the file in read mode
file = open('Myfile.txt', 'r')

# Read the content of the file
data = file.read()

# Initialize counters for vowels and consonants
count_V, count_C = 0, 0

# Iterate over each character in the file content
for char in data:
    if char.lower() in "aeiou":
        count_V += 1
    elif char.lower() in "bcdfghjklmnpqrstvwxyz":
        count_C += 1

# Print the counts
print("Number of vowels:", count_V)
print("Number of consonants:", count_C)

# Close the file
file.close()