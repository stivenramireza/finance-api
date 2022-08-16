from unittest import TestCase
from unittest.mock import Mock, patch

from fastapi import HTTPException

from src.services import auth_service
from src.middlewares.password_middleware import Password


class AuthServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.db = Mock()

    def tearDown(self) -> None:
        self.db = None

    @patch.object(Password, 'verify_password')
    @patch('src.services.user_service.get_user_by_username')
    def test_authenticate_user_raises_401_error(
        self, mock_get_user_by_username: Mock, mock_verify_password: Mock
    ) -> None:
        mock_get_user_by_username.return_value = {
            'id': 1,
            'name': 'Stiven Ramírez Arango',
            'password': 'stivenramireza',
        }
        mock_verify_password.return_value = False

        login_schema = {
            'username': 'stivenramireza',
            'password': 'stivenramireza',
        }

        with self.assertRaises(HTTPException):
            auth_service.authenticate_user(self.db, login_schema)
