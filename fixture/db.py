import pymysql.cursors
from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.database = name #? database or name?
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit = True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list_g = []
        cursor = self.connection.cursor() #создаем курсор
        try: # блок для исполнения
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list_g.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close() #закрыли курсор
        return list_g

    def get_contact_list(self):
        list_c = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, nickname, company, address, home, mobile, work, fax, email, email2, email3, homepage FROM addressbook WHERE deprecated IS NULL")
            for row in cursor:
                (id, firstname, lastname, nickname, company, address, home, mobile, work, fax, email, email2, email3, homepage) = row
                list_c.append(Contact(id=str(id),firstname= firstname, lastname= lastname, homephone= home, workphone= work, mobilephone= mobile, fax= fax, email3= email3, email2= email2, email= email, address= address))
        finally:
            cursor.close()
        return list_c


    def destroy(self):
        self.connection.close()