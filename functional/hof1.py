
def gmail_func(username, domain="gmail.com"):
    return f"{username}@{domain}"

def hot_mail(username , domain = "hotmail.com"):
    return f"{username}@{domain}"

def build_mail(username , email_func):
    return email_func(username)

print(build_mail("harshu" , gmail_func))
print(build_mail("keerthivasan" , hot_mail))