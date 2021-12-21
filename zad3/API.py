from FriendShips import FriendShips


class API:
    def __init__(self):
        self.methods = FriendShips()

    def getFriendsList(self, person):
        return self.methods.getFriendsList(person)

    def addFriend(self, person: str, friend: str):
        return self.methods.addFriend(person, friend)

    def makeFriends(self, person1: str, person2: str):
        return self.methods.makeFriends(person1, person2)

    def areFriends(self, person1, person2):
        return self.methods.areFriends(person1, person2)
