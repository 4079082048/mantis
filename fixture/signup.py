from selenium.webdriver.common.by import By
import re

class SignupHelper:
    def __init__(self,app):
        self.app =app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.base_url + "/signup_page.php")
        wd.find_element(By.NAME, "username").send_keys(username)
        wd.find_element(By.NAME, "email").send_keys(email)
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        mail = self.app.mail.get_mail(username, password, "") #"Mantis Bug Tracker"
        url = self.extract_confirmation_url(mail)
        wd.get(url)

        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.NAME, "password_confirm").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, 'input[value="Update User"]').click()

    def extract_confirmation_url(self, text):
        if text is None:
            return None  # Возвращаем None, если текст не задан
        #match = re.search(r"http://[^s]*", text)
        match = re.search(r'//localhost[^s]*"', text)
        return match.group(0) if match else None

    #def extract_confirmation_url(self, text):
    #    match = re.search("http://.*$", text, re.MULTILINE)
    #    if match:
    #        return match.group(0)
    #    else:
    #        raise ValueError("Confirmation URL not found in the email text.")




     #def extract_confirmation_url3(self, text):
        #   re.search("http://.*$", text, re.MULTILINE).group(0)
        #   re.search("//localhost.*$", text, re.MULTILINE).group(0)