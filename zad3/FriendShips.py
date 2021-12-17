class FriendShips:
    def __init__(self):
        self.rel = {}

    def getFriendsList(self, person):
        if person in self.rel.keys():
            return self.rel[person]
        else:
            return []

    def addFriend(self, person: str, friend: str):
        person_list = [friend]
        if person in self.rel.keys():
            if friend in self.rel[person]:
                raise Exception(f'{friend} is already friend to {person}!')
            person_list = [*self.rel[person], friend]
        self.rel.update({person: person_list})
        return self.rel[person]

    def makeFriends(self, person1: str, person2: str):
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)
        return self.rel

    def areFriends(self, person1, person2):
        is_friend = False
        if person2 in self.rel.keys():
            for friend in self.rel[person2]:
                if friend == person1: is_friend = True
        return is_friend
