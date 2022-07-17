def print_menu():
    return "Menu"


def modify(number):
    """
    puls one
    """
    number += 1


def nothing():
    """Later implement"""
    pass


def main():
    print(print_menu())

    gl_num = 2  # A global variable
    modify(gl_num)

    print(gl_num)


if __name__ == "__main__":
    main()
