def checked_lenght(username):
    if 3 <= len(username) <= 16:
        return True
    else:
        return False


def checked_symbols(username: str):
    for usernames in username:

        if not (usernames.isalnum() or usernames == "-" or usernames == "_"):  # if usernames.isalnum() and usernames
            # != "-" and usernames != "_"
            return False
    else:
        return True


def checked_spaces(username):
    if " " in username:
        return False
    else:
        return True


def is_valid(username):
    if checked_lenght(username) and checked_symbols(username) and checked_spaces(username):
        return True
    else:
        return False


names = input().split(", ")

for name in names:

    if is_valid(name):
        print(name)
