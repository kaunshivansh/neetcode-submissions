
class Twitter {

    private static int timestamp = 0;

    private Map<Integer, Set<Integer>> followMap;
    private Map<Integer, Tweet> tweetMap;

    public Twitter() {
        followMap = new HashMap<>();
        tweetMap = new HashMap<>();
    }

    public void postTweet(int userId, int tweetId) {
        Tweet tweet = new Tweet(tweetId, timestamp++);

        tweet.next = tweetMap.get(userId);
        tweetMap.put(userId, tweet);
    }

    public List<Integer> getNewsFeed(int userId) {

        List<Integer> res = new ArrayList<>();

        followMap.putIfAbsent(userId, new HashSet<>());
        followMap.get(userId).add(userId);

        PriorityQueue<Tweet> maxHeap =
            new PriorityQueue<>((a, b) -> b.time - a.time);

        for (int followee : followMap.get(userId)) {
            if (tweetMap.containsKey(followee)) {
                maxHeap.offer(tweetMap.get(followee));
            }
        }

        while (!maxHeap.isEmpty() && res.size() < 10) {
            Tweet curr = maxHeap.poll();
            res.add(curr.id);

            if (curr.next != null) {
                maxHeap.offer(curr.next);
            }
        }

        return res;
    }

    public void follow(int followerId, int followeeId) {
        followMap.putIfAbsent(followerId, new HashSet<>());
        followMap.get(followerId).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        if (followMap.containsKey(followerId)
                && followeeId != followerId) {
            followMap.get(followerId).remove(followeeId);
        }
    }

    private static class Tweet {
        int id;
        int time;
        Tweet next;

        Tweet(int id, int time) {
            this.id = id;
            this.time = time;
        }
    }
}