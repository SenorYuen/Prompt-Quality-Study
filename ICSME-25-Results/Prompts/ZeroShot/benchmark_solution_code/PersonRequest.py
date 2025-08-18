'''
# This class validates input personal information data and sets invalid fields to None based to specific rules.

class PersonRequest:
    def __init__(self, name: str, sex: str, phoneNumber: str):
        """
        Initialize PersonRequest object with the provided information.
        """
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phoneNumber = self._validate_phoneNumber(phoneNumber)


    def _validate_name(self, name: str) -> str:
        """
        Validate the name and return it. If name is empty or exceeds 33 characters in length, set to None.
        :return: str, the validated name or None if invalid
        """


    def _validate_sex(self, sex: str) -> str:
        """
        Validate the sex and return it. If sex is not Man, Woman, or UGM, set to None.
        :return: str, the validated sex or None if invalid
        """

    def _validate_phoneNumber(self, phoneNumber: str) -> str:
        """
        Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
        :return: str, the validated phone number or None if invalid
        """

'''


class PersonRequest:
    def __init__(self, name: str, sex: str, phoneNumber: str):
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phoneNumber = self._validate_phoneNumber(phoneNumber)

    def _validate_name(self, name: str) -> str:
        if not name:
            return None
        if len(name) > 33:
            return None
        return name

    def _validate_sex(self, sex: str) -> str:
        if sex not in ["Man", "Woman", "UGM"]:
            return None
        return sex

    def _validate_phoneNumber(self, phoneNumber: str) -> str:
        if not phoneNumber:
            return None
        if len(phoneNumber) != 11 or not phoneNumber.isdigit():
            return None
        return phoneNumber


