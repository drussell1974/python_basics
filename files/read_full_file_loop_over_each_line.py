from writing_to_file import write_data

write_data()

# loop over each line
f = open("data.txt", "r")
for line in f:
    print(line)
