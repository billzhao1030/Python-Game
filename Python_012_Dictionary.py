# kind of hash table?

dictionary = {
    "age": 20,
    "name": "bill",
    "gender": "male"
}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

print(dictionary["age"])

dictionary.update({("age", 19)})
print(dictionary)

# list with dict
student_list = [{
    "age": 20,
    "name": "bill",
    "gender": "male"
}, {
    "age": 19,
    "name": "tom",
    "gender": "male"
}]
