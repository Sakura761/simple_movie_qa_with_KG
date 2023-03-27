from tweet import Tweet


class User():
    def __init__(self,userId) -> None:
        self.userId = userId
        self.fans = set()
        self.tweets = []
    def postTweet(self,userId, tweetId):
        tweet = Tweet(tweetId)
        self.tweets.append(tweetId)
    def follow(self,followerId):
        set.add(followerId)
    def unfollow(self,followerId):
        set.remove(followerId)