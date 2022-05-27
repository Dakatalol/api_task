from faker import Faker


class Utils:



    @staticmethod
    def sort_user_by_first_name(list_of_users):
        """
        :param list_of_users: dict of users
        :return: returns sorted dict of users by name
        """
        return sorted(list_of_users, key=lambda x: x['first_name'])

    @staticmethod
    def generate_random_name():
        return Faker().name()

    @staticmethod
    def generate_random_job():
        return Faker().job()

