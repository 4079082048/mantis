import poplib
import email
import quopri
import time


class MailHelper:
    def __init__(self,app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            num = pop.stat()[0]
            if num > 0:
                for n in range(num):
                    msglines = pop.retr(n + 1)[1]
                    msgtext = '\n'.join(map(lambda x: x.decode('utf-8'), msglines))
                    msg  = email.message_from_string(msgtext)
                    subject = msg.get('Subject')  # Сохраняем результат в переменную subject
                    # Выводим значение переменной subject на печать
                    print(subject)
                    if msg.get('Subject') == subject:
                        pop.dele(n+1)
                        pop.quit()
                        return quopri.decodestring(msg.get_payload()).decode('utf-8')

            pop.quit()
            time.sleep(10)
        return None