import unittest
from assertpy import assert_that
from FriendShips import FriendShips


class TestFriendShips(unittest.TestCase):
    def setUp(self):
        self.temp = FriendShips()

    def test_add_friend(self):
        self.temp.addFriend("Marek", "Jarek")
        assert_that(self.temp.rel).is_equal_to({"Marek": ["Jarek"]})

    def test_add_friend_again(self):
        self.temp.addFriend("Marek", "Jarek")
        self.assertRaises(Exception, self.temp.addFriend, "Marek", "Jarek")

    def test_add_friends(self):
        self.temp.addFriend("Marek", "Jarek"), self.temp.addFriend("Marek", "Darek")
        assert_that(self.temp.rel).is_equal_to({"Marek": ["Jarek", "Darek"]})

    def test_add_firends_different(self):
        self.temp.addFriend("Marek", "Jarek"), self.temp.addFriend("Marek", "Darek")
        self.temp.addFriend("Seba", "Mati")
        assert_that(self.temp.rel).is_equal_to({"Marek": ["Jarek", "Darek"], "Seba": ["Mati"]})

    def test_add_firends_different_more(self):
        self.temp.addFriend("Marek", "Jarek"), self.temp.addFriend("Marek", "Darek")
        self.temp.addFriend("Seba", "Mati"), self.temp.addFriend("Seba", "Kacper")
        assert_that(self.temp.rel).is_equal_to({"Marek": ["Jarek", "Darek"], "Seba": ["Mati", "Kacper"]})

    def test_get_friends_empty(self):
        assert_that(self.temp.getFriendsList("Marek")).is_equal_to([])

    def test_get_friends_one(self):
        self.temp.rel = {
            "Marek": ["Jarek", "Darek"],
            "Seba": ["Mati"]
        }
        assert_that(self.temp.getFriendsList("Marek")).is_equal_to(["Jarek", "Darek"])

    def test_get_friends_two(self):
        self.temp.rel = {
            "Marek": ["Jarek", "Darek"],
            "Seba": ["Mati"]
        }
        assert_that(self.temp.getFriendsList("Seba")).is_equal_to(["Mati"])

    def test_are_friends_true(self):
        self.temp.rel = {
            "Seba": ["Mati", "Kacper", "Aleks"],
            "Mati": ["Seba", "Igor"]
        }

        assert_that(self.temp.areFriends("Mati", "Seba")).is_true()

    def test_are_friends_true2(self):
        self.temp.rel = {
            "Seba": ["Mati", "Kacper", "Aleks"],
            "Mati": ["Seba", "Igor"]
        }
        assert_that(self.temp.areFriends("Kacper", "Seba")).is_true()

    def test_are_friends_false(self):
        self.temp.rel = {
            "Seba": ["Mati", "Kacper", "Aleks"],
            "Mati": ["Seba", "Igor"]
        }
        assert_that(self.temp.areFriends("Igor", "Seba")).is_false()

    def tearDown(self) -> None:
        self.temp = None
