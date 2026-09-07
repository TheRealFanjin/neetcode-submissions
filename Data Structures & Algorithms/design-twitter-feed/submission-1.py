import time
import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (-time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        tweets_out = []
        for account in self.following[userId]:
            tweets_copy = self.tweets[account][:]
            for i in range(10):
                if not tweets_copy:
                    break
                heapq.heappush(tweets, heapq.heappop(tweets_copy))
        
        tweets_copy = self.tweets[userId][:]
        for i in range(10):
            if not tweets_copy:
                break
            heapq.heappush(tweets, heapq.heappop(tweets_copy))
        
        for i in range(10):
            if not tweets:
                break
            tweets_out.append(heapq.heappop(tweets)[1])
        
        return tweets_out
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followeeId].add(followerId)
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followeeId].discard(followerId)
        self.following[followerId].discard(followeeId)
        
