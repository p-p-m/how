import collections


class Solution:
    """
    @param friends: people's friends
    @param user: the user's id
    @return: the person who most likely to know
    """
    def recommendFriends(self, friends, user):
        friends = self._to_dict(friends)
        user_friends = friends[user]
        counter = collections.Counter([])
        for user_friend in user_friends:
            counter.update([
                friend for friend in friends[user_friend]
                if friend not in user_friends and friend != user
            ])
        try:
            return min(counter.most_common(), key=lambda c: [-c[1], c[0]])[0]
        except (IndexError, ValueError):
            return -1

    def _to_dict(self, friends):
        friends_as_dict = {}
        for person, person_friends in enumerate(friends):
            friends_as_dict[person] = person_friends
        return friends_as_dict
