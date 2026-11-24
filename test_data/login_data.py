login_test_date = [
    ("john", "demo", True, None),
    ("wronguser", "wrongpwd", False, "he username and password could not be verified."),
    ("john", "wrongpwd", False, "he username and password could not be verified."),
    ("","", False, "Please enter a username and password."),
]