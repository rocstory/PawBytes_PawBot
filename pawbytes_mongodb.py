import db_key

import pymongo
from pymongo import MongoClient


cluster = MongoClient(db_key.DB_KEY)
db = cluster["PawBytes"]


def get_pawpal_tagnames():
    collection = db["pawpals"]
    pawpals = collection.find({})
    tagnames = []
    for pawpal in pawpals:
        tagnames.append([pawpal['tagname'], str(pawpal['_id'])])
    return tagnames

def add_etreat_to_db(tweet_id, user, tweet_text, pawid_list):
    collection = db["etreats"]
    # Create etreat here
    etreat = {
            "text": tweet_text,
            "sender": user,
            "palsmentioned": pawid_list, 
            "tweetid": tweet_id
        }
    collection.insert_one(etreat)

def save_last_seen_tweet(last_seen_tweet):
    collection = db['lastreadtweet']
    collection.insert_one({'tweetid':last_seen_tweet})

def get_last_seen_id():
    collection = db["lastreadtweet"]
    recentTweet = collection.find({}).sort([('_id', -1 )]).limit(1)

    tweetid = None
    for tweet in recentTweet:
        tweetid = tweet['tweetid']
    return tweetid