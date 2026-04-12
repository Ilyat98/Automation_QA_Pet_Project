import pymysql


class DBClient:

    def __init__(self):
        self.connection = pymysql.connect(
            host="mysql",
            user="test_user",
            password="test_password",
            database="test_db",
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_user_by_email(self, email):

        with self.connection.cursor() as cursor:
            query = "SELECT * FROM users WHERE email=%s"
            cursor.execute(query, (email,))
            return cursor.fetchone()

    def close(self):
        self.connection.close()

    def create_user(self, email):
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO users (email) VALUES (%s)"
                cursor.execute(query, (email,))
                self.connection.commit()
        except Exception as e:
            raise AssertionError(f"DB insert failed: {e}")

    def delete_user(self, email):
        with self.connection.cursor() as cursor:
            query = "DELETE FROM users WHERE email=%s"
            cursor.execute(query, (email,))
            self.connection.commit()