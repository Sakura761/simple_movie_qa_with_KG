from tweet import Tweet
import time

from user import User

class Twitter(object):
    def __init__(self):
        self.users = dict()
        pass

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if (userId not in self.users.keys()):
            self.users[userId] = User(userId)
        user = self.users[userId]
        user.postTweet(userId,tweetId)

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        for i in range(-1,-10):
            try:
                res.append(self.users[userId].tweets[i])
            except(Exception):
                pass
        return res
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId not in self.users.keys():
            self.users[followeeId] = User(followeeId)
        
        user = self.users[followeeId]
        user.follow(followerId)
        print(user.fans)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """ 
        user = self.users[followeeId]
        user.unfollow(followerId)
        print(user.fans)
    # ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    # [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
twitter = Twitter()
twitter.postTweet(1,5)
print(twitter.getNewsFeed(1))
twitter.follow(1,2)
twitter.postTweet(2,6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1,2)
print(twitter.getNewsFeed(1))

        