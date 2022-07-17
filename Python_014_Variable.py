gl_num = 1  # add a gl_ indicate the global variable


def add_one(number):
    print(id(number))
    number += 1
    print(id(number))


def really_add_one():
    global gl_num
    gl_num += 1


def something_pre_defined(a = 1): # should be in the end of variable list
    return a + 2


def multiple_variable_func(num, *args, **kwargs):
    """

    :param num:
    :param args: can receive the tuple => *tuple
    :param kwargs: can receive the dict (apart first) => **dict
    :return:
    """
    pass


print(id(gl_num))
add_one(gl_num)

########
str_name = "bill"
print(id(str_name))
str_name = "tom"
print(id(str_name))

print(id(gl_num))
gl_num = 2
print(id(gl_num))
