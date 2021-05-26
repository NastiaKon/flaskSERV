from password_enc import enc_password


class Users:
    users = []

    def get_users(self):
        return self.users

    def set_users(self, login, password, date=None):
        self.users.append({'login': login, 'password': enc_password(password), 'registration date': date})
        return list(filter(lambda user: user['login'] == login, self.users))
