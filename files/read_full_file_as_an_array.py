from writing_to_file import write_data

write_data()

# read each line as a list item
f = open("data.txt", "r")
print(f.readlines())
f.close()
