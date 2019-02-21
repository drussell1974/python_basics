from writing_to_file import write_data

write_data()

# read the whole document
f = open("data.txt", "r")
print(f.read())
f.close()

