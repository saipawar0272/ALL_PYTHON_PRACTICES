#program which will validate the name of student,product and place name
#name must contain only single word or multiple word seprated by space only(only alphabets)
#name should not contain digits
#name should not contain special symbols


class NameValidError(BaseException):pass

class ZeroLengthError(Exception):pass