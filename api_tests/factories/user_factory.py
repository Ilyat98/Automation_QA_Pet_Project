from faker import Faker

fake = Faker()


class UserFactory:

    @staticmethod
    def create_user():

        return {
            "name": fake.name(),
            "job": fake.job()
        }

    @staticmethod
    def update_user():

        return {
            "name": fake.name(),
            "job": fake.job()
        }