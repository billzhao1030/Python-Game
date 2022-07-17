# List is like Array (but can store different type of data)

str_list = [25, 41, 15]

print(str_list[1]) # We could see is like array
print("List have %d numbers" % len(str_list));


print(str_list)
str_list.sort()
print(str_list)

str_list.pop()
print(str_list)

str_list.append(90)
print(str_list)

str_list.append("bill")
print(str_list)

str_list.remove(90)
print(str_list)

del str_list[1] # Clear from memory
print(str_list)