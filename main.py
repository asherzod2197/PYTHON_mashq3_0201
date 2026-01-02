def login_tekshir(login, parol):
    if login == "admin" and parol == "1234":
        return "Kirish muvaffaqiyatli"
    else:
        return "Login yoki parol xato"


print(login_tekshir("admin", "1234"))
print(login_tekshir("user", "1111"))
