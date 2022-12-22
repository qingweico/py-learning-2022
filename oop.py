class User:
    def __init__(self, no, name):
        # private: __field
        self.__no = no
        self.__name = name

    def to_string(self):
        print('{no : %s, name : %s}' % (self.__no, self.__name))


# user = User(1, "Maria")
# user.__name = "sd"
# user.to_string()
