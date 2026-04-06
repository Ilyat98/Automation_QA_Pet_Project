import pymysql


class DBClient:

    def __init__(self):
        self.connection = pymysql.connect(
        host="mysql",
        user="test_user",
        password="test_password",
        database="test_db")

    def get_user_by_email(self, email):

        with self.connection.cursor() as cursor:
            query = "SELECT * FROM users WHERE email=%s"
            cursor.execute(query, (email,))
            return cursor.fetchone()

    def close(self):
        self.connection.close()