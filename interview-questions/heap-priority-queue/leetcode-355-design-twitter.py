# 355. Design Twitter
# Medium
#    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
#
#    Implement the Twitter class:
#
#        Twitter() Initializes your twitter object.
#        void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
#        List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
#        void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
#        void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
#
#     
#
#    Example 1:
#
#    Input
#    ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
#    [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
#    Output
#    [null, null, [5], null, null, [6, 5], null, [5]]
#
#    Explanation
#    Twitter twitter = new Twitter();
#    twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
#    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
#    twitter.follow(1, 2);    // User 1 follows user 2.
#    twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
#    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
#    twitter.unfollow(1, 2);  // User 1 unfollows user 2.
#    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
#
#     
#
#    Constraints:
#
#        1 <= userId, followerId, followeeId <= 500
#        0 <= tweetId <= 104
#        All the tweets have unique IDs.
#        At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
#
#

import heapq

class UserData:
    def __init__(self, uid):
        self.tweets=[]
        self.follows=set([uid])
    def __repr__(self):
        return f"follows: {self.follows} tweets: {self.tweets}"

class Twitter:

    def __init__(self):
        self.ctime = 0
        self.users = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        udata = self.users.setdefault(userId, UserData(userId) )
        self.ctime += 1
        udata.tweets.append( (tweetId, self.ctime) )

    def getNewsFeed(self, userId: int) -> List[int]:

        user = self.users.get(userId)
        if not user:
            return []

        follow_heap = []
        for followed_uid in user.follows:
            user_data = self.users.get(followed_uid)
            if len(user_data.tweets) != 0:
                tweet = user_data.tweets[-1]
                entry = (-tweet[1], tweet[0], followed_uid, 1)
                heapq.heappush(follow_heap, entry)

        ret = []


        for idx in range(0, 10):
            if len(follow_heap) == 0:
                break

            entry = heapq.heappop(follow_heap)
            ret.append(entry[1])

            user_data = self.users.get(entry[2])
            tweet_idx = entry[3] + 1
            if tweet_idx <= len(user_data.tweets):
                tweet = user_data.tweets[ - tweet_idx ]
                heapq.heappush(follow_heap, (-tweet[1], tweet[0], entry[2], tweet_idx)  )


        return ret


    def follow(self, followerId: int, followeeId: int) -> None:
        udata = self.users.setdefault(followerId, UserData(followerId) )
        self.users.setdefault(followeeId, UserData(followeeId) )

        udata.follows.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        udata = self.users.get(followerId)
        if udata and followeeId in udata.follows:
            udata.follows.remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
