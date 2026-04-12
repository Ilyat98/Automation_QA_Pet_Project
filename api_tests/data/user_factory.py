from faker import Faker

fake = Faker()

class UserFactory:
    @staticmethod
    def user():
        return {
            "name": fake.name(),
            "job": fake.job()
        }