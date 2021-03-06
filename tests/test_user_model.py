import unittest
from app.models import User, Role, AnonymousUser, Permission


class MyTestCase(unittest.TestCase):
    def test_password_setter(self):
        user = User(password='cat')
        self.assertTrue(user.password_hash is not None)

    def test_no_password_getter(self):
        user = User(password='cat')
        with self.assertRaises(AttributeError):
            _ = user.password

    def test_password_verification(self):
        user = User(password='cat')
        self.assertTrue(user.verify_password('cat'))
        self.assertFalse(user.verify_password('dog'))

    def test_password_salts_are_random(self):
        user1 = User(password='cat')
        user2 = User(password='cat')
        self.assertTrue(user1.password_hash != user2.password_hash)

    def test_roles_and_permissions(self):
        Role.init()
        user = User(email='john@example.com', password='cat')
        self.assertTrue(user.can(Permission.WRITE_ARTICLES))
        self.assertFalse(user.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        user = AnonymousUser()
        self.assertFalse(user.can(Permission.FOLLOW))


if __name__ == '__main__':
    unittest.main()
