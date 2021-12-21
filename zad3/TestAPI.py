import unittest
from unittest.mock import MagicMock, patch, call
from API import API


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.temp = MagicMock()

    @patch("API.API.addFriend")
    def test_add_friend(self, mock):
        mock.return_value = {"Marek": ["Jarek"]}
        mock.addFriend("Marek", "Jarek")
        mock.addFriend.assert_called_with("Marek", "Jarek")

    def test_get_friends_list(self):
        self.temp.getFirendsList.side_effect = [
            ["Jarek", "Darek"],
            ["Mati", "Darek"],
        ]
        self.temp.getFriendsList("Marek")
        self.temp.getFriendsList.assert_called_with("Marek")
        self.temp.getFriendsList("Seba")
        self.temp.getFriendsList.assert_called_with("Seba")

    def test_make_friends(self):
        self.temp.makeFriends.return_value = {"Marek": ["Jarek"], "Jarek": ["Marek"]}
        self.temp.makeFirends("Marek", "Jarek")
        self.temp.makeFirends.assert_called_with("Marek", "Jarek")

    def test_are_friends(self):
        self.temp.areFriends.side_effect = [True, False, True]
        self.temp.areFriends("Maciek", "Paweł")
        self.temp.areFirends("Seba", "Mati")
        self.temp.areFirends("Ola", "Ala")
        self.temp.assert_has_calls([call.areFriends("Maciek", "Paweł"), call.areFirends("Seba", "Mati"),
                                    call.areFirends("Ola", "Ala")], any_order=True)

    def tearDown(self) -> None:
        self.temp = None
