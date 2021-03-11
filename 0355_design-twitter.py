"""
设计推特

链接：https://leetcode-cn.com/problems/design-twitter

设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，

能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户

示例:
Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);


"""
import heapq
import unittest
from datetime import datetime
from typing import Dict, List, Optional, Set


class Tweet:
    def __init__(self, tid: int, create_at: float):
        self.tid: int = tid
        self.create_at: float = create_at
        self.next: Optional[Tweet] = None


class User:
    def __init__(self, uid: int):
        self.uid: int = uid
        self.following: Set[int] = set()
        self.tweet: Optional[Tweet] = None
        # 关注自己。
        self.follow(uid)

    def post_tweet(self, tid: int) -> None:
        tweet = Tweet(tid, datetime.now().timestamp())
        tweet.next = self.tweet
        self.tweet = tweet

    def follow(self, uid: int) -> None:
        self.following.add(uid)

    def unfollow(self, uid: int) -> None:
        if uid != self.uid and uid in self.following:
            self.following.remove(uid)


class Twitter:
    def __init__(self):
        self.uid2user: Dict[int, User] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.uid2user:
            self.uid2user[userId] = User(userId)

        user = self.uid2user[userId]
        user.post_tweet(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.uid2user:
            return []

        # 将该用户的所有关注者的 tweet 放入 heap。
        user = self.uid2user[userId]
        heap = []
        for uid in user.following:
            f_user = self.uid2user[uid]
            tweet = f_user.tweet
            while tweet:
                heap.append(tweet)
                tweet = tweet.next

        # 取堆中时间戳最大的 10 个 tweet。
        return [t.tid for t in heapq.nlargest(10, heap, key=lambda t: t.create_at)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.uid2user:
            self.uid2user[followerId] = User(followerId)
        if followeeId not in self.uid2user:
            self.uid2user[followeeId] = User(followeeId)

        user = self.uid2user[followerId]
        user.follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.uid2user:
            user = self.uid2user[followerId]
            user.unfollow(followeeId)


class TestSolution(unittest.TestCase):
    def test_twitter(self) -> None:
        t = Twitter()
        t.postTweet(1, 5)
        self.assertListEqual([5], t.getNewsFeed(1))
        t.follow(1, 2)
        t.postTweet(2, 6)
        self.assertListEqual([5, 6], t.getNewsFeed(1))
        t.unfollow(1, 2)
        self.assertListEqual([5], t.getNewsFeed(1))


if __name__ == "__main__":
    unittest.main()
