from collections import defaultdict
from heapq import *

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.following[userId].add(userId)

        for user in self.following[userId]:
            if self.tweets[user]:
                i = len(self.tweets[user]) - 1
                time, tweet = self.tweets[user][i]
                heappush(heap, (-time, tweet, user, i - 1))

        ans = []
        while heap and len(ans) < 10:
            _, tweet, user, i = heappop(heap)
            ans.append(tweet)
            if i >= 0:
                time, tweet = self.tweets[user][i]
                heappush(heap, (-time, tweet, user, i - 1))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)