try:
    num = (1/int(input("number:")))
except ZeroDivisionError:
    print("wrong")
except Exception as result:
    print(result)
else:
    print("else part")  # no exception
finally:
    print("final")  # always do

print("!!")

def input_password():
    password = input("pwd: ")

    if len(password) >= 8:
        return password

    ex = Exception("too short")
    raise ex


input_password()