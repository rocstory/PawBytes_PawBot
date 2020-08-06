import tweepy
import twitter_key
import pawbytes_mongodb as db
import twitter_bot_exceptions as bot_except
import re 
import time

# ** NOTE **  Place restrictions on how many tweets are sent out.
# think about putting a tweet limit per hour or so.

pawpal_dict = dict()

def retrieve_last_seen_id():
    # Try to open file
    try:
        last_seen_id = db.get_last_seen_id() 
        return last_seen_id
    except: 
        pass

def store_last_seen_id(last_seen_id):
    db.save_last_seen_tweet(last_seen_id)

def get_mentioned_tweets():
    # Try to get tweets from user
    try:
        # Get the saved tweet id
        last_seen_tweet = int(retrieve_last_seen_id())
        # print("last seen tweet", last_seen_tweet)
        tweets = twitter_key.api.mentions_timeline(last_seen_tweet, tweet_mode="extended")
    except ValueError:
        print("Unwanted value from file, using default value")
        tweets = twitter_key.api.mentions_timeline(tweet_mode="extended")
    except Exception as error:
        print("Unknown error!", error)
        tweets = None
    finally:
        return tweets

def populate_pawpal_tagname_dict():
    db_tagnames = db.get_pawpal_tagnames()
    for tagname in db_tagnames:
        key_tagname = tagname[0].lower()
        value_pawpal_id = tagname[1]
        pawpal_dict[key_tagname] = value_pawpal_id

def get_mentioned_pawpal(tweet):
    text = tweet.full_text
    mentioned_pals = []
    # extract each tagname from text
    hashtags = re.findall(r"#[a-zA-Z0-9]*", text)
    for hashtag in hashtags:
        tagname = hashtag[1:]
        if tagname in pawpal_dict.keys():
            pal_id = pawpal_dict[tagname]
            if pal_id not in mentioned_pals:
                mentioned_pals.append(pal_id)
    
    if mentioned_pals:
        return mentioned_pals
    else:
        return None

def send_tweet_to_db(tweet, pawid_list):
    try:
        # [Future Feature] : Profanity check
        tweet_id = tweet.id
        tweet_owner = tweet.user.screen_name
        tweet_text = tweet.full_text
        db.add_etreat_to_db(tweet_id,tweet_owner, tweet_text, pawid_list)
        
    except:
        print("Error sending tweet to database")

def reply_to_tweet(tweet, message):
    tweet_id = tweet.id
    user = tweet.user.screen_name
    print(f"replying to {user} with: ", message, tweet.full_text)

    full_message = f"@{user} {message}"
    twitter_key.api.update_status(full_message, tweet_id)
    time.sleep(8)

def retrieve_tweets():
    populate_pawpal_tagname_dict()
    try:
        if not bool(pawpal_dict):
            raise bot_except.NoTagNamesError
        
        #last_tweet_read = None
        tweets = get_mentioned_tweets()

        # Perform an action for each tweet obtained...
        for tweet in reversed(tweets):
            last_tweet_read = tweet.id
            mentioned_pals = get_mentioned_pawpal(tweet)
            if mentioned_pals:
                send_tweet_to_db(tweet, mentioned_pals)
                reply_to_tweet(tweet, "thank you! Check out our website to view your E-Treat!")
            store_last_seen_id(last_tweet_read)

    except bot_except.NoTagNamesError as error:
        print(error)
    except Exception as error:
        pass 

begin = True
count = 0
while begin:
    if count == 80:
        begin = False
    print("Retrieving tweets!")
    retrieve_tweets()
    time.sleep(12)
    count += 1
    