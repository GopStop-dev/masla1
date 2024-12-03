class Contact:
    def __init__(self, name: str, phone_number: str):
        self.__name = name
        self.__phone_number = phone_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if len(phone_number) == len("+998 99 123 45 67"):
            self.__phone_number = phone_number


obj = Contact("John", "+998 99 123 45 67")
print(obj.name)
print(obj.phone_number)

obj.name = "Alice"
print(obj.name)

obj.phone_number = "+998 99 223 45 78"
print(obj.phone_number)
