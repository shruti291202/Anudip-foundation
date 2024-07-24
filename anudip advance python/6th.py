file = open("story.txt", 'w')
file.write("The quick brown fox jumps over the lazy dog. \n")
file.write("INDIA is a diverse country with rich cultural heritage.\n")
file.write("Technology is advancing at an unprecedented pace.\n")
file.write("Hello sarthak, welcome to the python class.\n")
file.write("Tomorrow, we will explore more advanced topics.\n")
file.write("Taking small steps every day leads to big achievements.\n")
file.close()
file = open("story.txt", 'r')
count = 0
content = file.readlines()
for line in content:
    if line[0] == 'T':
        print(line, end='')
        count += 1

print("Number of lines starting with 'T':", count)
file.close()
