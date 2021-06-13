from datetime import datetime

import factory


class User:
    def __init__(self, uid, first_name, last_name, email):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return '<User: {} - {} {} ({})>'.format(self.uid, self.first_name, self.last_name, self.email)


class UserFactory(factory.Factory):
    class Meta:
        model = User

    uid = factory.Sequence(lambda n: n)
    # uid = factory.LazyFunction(datetime.now)
    first_name = 'John'
    last_name = 'Doe'
    email = factory.LazyAttribute(lambda obj: '{}.{}@email.com'.format(obj.first_name, obj.last_name))


class AdminFactory(UserFactory):
    uid = factory.Sequence(lambda n: "admin_" + str(n))


if __name__ == '__main__':
    john = UserFactory(first_name='Bob')
    print(john)
    print(UserFactory(last_name='Phish'))
    print(AdminFactory())
    print(UserFactory())
