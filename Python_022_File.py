file = open("README","a")


extra = "some content!!"
file.write(extra)



file.close()

file = open("README")

while True:
    text = file.readline()

    if not text:
        break

    print(text, end="")