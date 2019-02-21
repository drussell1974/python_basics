def write_data():
    f = open("data.txt", "w")
    f.write("Hello, World!")
    f.write("Appended text")
    f.write("\nA new line")
    f.write("\nAnother new line")

    f.close()


write_data()
