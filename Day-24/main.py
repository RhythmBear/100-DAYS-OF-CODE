# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt", mode="r") as file:
    content = int(file.read())

    if content < 25:
        new_highscore = 25
        with open("my_file.txt", mode="w") as file:
            file.write(f"{new_highscore}")
            print("High Score Updated")
