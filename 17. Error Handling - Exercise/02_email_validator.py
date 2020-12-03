class NameTooShortError(Exception):
    """ Raised when username is 4 symbols or less """
    def __init__(self, message="Name must be more than 4 characters"):
        self.message = message
        super(NameTooShortError, self).__init__(message)


class MustContainAtSymbolError(Exception):
    """ Raised when @ symbol is missing """
    def __init__(self, message="Email must contain @"):
        self.message = message
        super(MustContainAtSymbolError, self).__init__(message)


class InvalidDomainError(Exception):
    """ Raised when the domain is invalid """
    def __init__(self, message="Domain must be one of the following: .com, .bg, .org, .net"):
        self.message = message
        super(InvalidDomainError, self).__init__(message)


def get_username(email):
    at_index = email.index("@")
    username = email[:at_index]
    return username


def validate_domain(email):
    valid_domains = ("com", "bg", "net", "org")
    domain = email.split(".")[-1]
    if domain not in valid_domains:
        raise InvalidDomainError()


def validate_username(email):
    username = get_username(email)
    if len(username) <= 4:
        raise NameTooShortError()


def validate_at_symbol(email):
    if "@" not in email:
        raise MustContainAtSymbolError()


line = input()
while not line == "End":
    email = line

    validate_at_symbol(email)
    validate_username(email)
    validate_domain(email)

    print("Email is valid")
    line = input()