from writing_to_file import write_data

write_data()

# read the first line
f = open("data.txt", "r")
print(f.readline())
f.close()
