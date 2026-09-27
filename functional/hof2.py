
def email_builder(domain):
    def build_mail(username):
        return f"{username}@{domain}"
    return build_mail

gmail = email_builder("gmail.com")
hotmail=email_builder("hotmail.com")

print(gmail("Keerthivasan"))
print(hotmail("Harshitha"))