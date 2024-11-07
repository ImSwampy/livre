line_number = 2  # Choose the line you want to read

with open("myfile.txt", "a") as file:
    print(file.writable())
    file.writelines(["123", "456", "789"])
