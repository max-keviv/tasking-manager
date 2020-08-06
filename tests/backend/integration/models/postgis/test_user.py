from backend.models.postgis.user import User, UserRole, MappingLevel
from tests.backend.base import BaseTestCase


class TestUser(BaseTestCase):
    def setUp(self):
        super().setUp()
        test_user = User()
        test_user.role = UserRole.MAPPER.value
        test_user.id = 12
        test_user.mapping_level = MappingLevel.BEGINNER.value
        test_user.username = "mrtest"
        test_user.email_address = "test@test.com"

    def test_as_dto_will_not_return_email_if_not_owner(self):
        if self.skip_tests:
            return
        # Act
        user_dto = self.test_user.as_dto("mastertest")

        # Assert
        self.assertFalse(user_dto.email_address)

    def test_as_dto_will_not_return_email_if_owner(self):
        if self.skip_tests:
            return

        # Act
        user_dto = self.test_user.as_dto("mrtest")

        # Assert
        self.assertTrue(user_dto.email_address)
