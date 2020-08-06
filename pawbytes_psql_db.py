# This file is no longer used with the twitter bot.
import psycopg2
import json

DATA_FILE = open('db_data.json')
DATA = json.load(DATA_FILE)

DB_NAME = DATA["DB_NAME"]
DB_USER = DATA["DB_USER"]
DB_PASS = DATA["DB_PASS"]
DB_HOST = DATA["DB_HOST"]
DB_PORT = DATA["DB_PORT"]

def get_pawpal_tagnames():
    tagnames_sql = """ SELECT pawID, tagname  FROM pawpal_t;"""
    try:
        conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)
        cursor = conn.cursor()
        cursor.execute(tagnames_sql)
        rows = cursor.fetchall()
    except:
        print("error")
    finally:
        cursor.close()
        conn.close()
        return rows

def add_tweet_owner(tweet_id, paw_id):
    insert_tweet_ownership_sql = f"""INSERT INTO Tweet_Treat_Owner(tweetID, pawID) 
                            VALUES ({tweet_id}, {paw_id}) """
    
    try:
        conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)
        cursor = conn.cursor()
        cursor.execute(insert_tweet_ownership_sql)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as error:
        pass #print("error", error)

def add_tweet_to_db(tweet_id, tweet_owner, tweet_text):
    insert_tweet_sql = f""" INSERT INTO Tweet_Treat(tweetID, tweet_owner, tweet_text) 
                            VALUES ({tweet_id}, '{tweet_owner}', '{tweet_text}')  """
    try:
        conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)
        cursor = conn.cursor()
        cursor.execute(insert_tweet_sql)

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as error:
        pass #print("error", error)

