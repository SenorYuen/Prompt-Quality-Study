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
        # Check if name is not empty and does not exceed 33 characters
        if name and len(name) <= 33:
            return name
        else:
            # If name is invalid, return None
            return None


    def _validate_sex(self, sex: str) -> str:
        """
        Validate the sex and return it. If sex is not Man, Woman, or UGM, set to None.
        :return: str, the validated sex or None if invalid
        """
        # Define valid sex options
        valid_sex_options = ["Man", "Woman", "UGM"]
        # Check if sex is in valid options
        if sex in valid_sex_options:
            return sex
        else:
            # If sex is invalid, return None
            return None


    def _validate_phoneNumber(self, phoneNumber: str) -> str:
        """
        Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
        :return: str, the validated phone number or None if invalid
        """
        # Check if phoneNumber is not empty and has exactly 11 digits
        if phoneNumber and phoneNumber.isdigit() and len(phoneNumber) == 11:
            return phoneNumber
        else:
            # If phoneNumber is invalid, return None
            return None