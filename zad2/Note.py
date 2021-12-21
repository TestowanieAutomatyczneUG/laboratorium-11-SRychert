class Note:

    def __init__(self, name, note):
        if type(name) is not str:
            raise TypeError()
        else:
            if name == "":
                raise ValueError()
            else:
                self.__name = name

        if type(note) is float or type(note) is int:
            if 2 <= note <= 6:
                self.__note = note
            else:
                raise ValueError()
        else:
            raise TypeError()

    def get_name(self):
        return self.__name

    def get_note(self):
        return self.__note
