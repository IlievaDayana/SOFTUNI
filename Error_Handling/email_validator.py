class NameTooShortError(Exception):
    """Raised when name is too short"""


class MustContainAtSymbolError(Exception):
    """Raised when no @ symbol"""


class InvalidDomainError(Exception):
    """Raised when domain is invalid"""


while True:
    read = input()
    if "@" not in read:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name, website = read.split("@")
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        elif ".com" in website:
            print("Email is valid")
        elif ".bg" in website:
            print("Email is valid")
        elif ".org" in website:
            print("Email is valid")
        else:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
