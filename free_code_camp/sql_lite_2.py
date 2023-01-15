from urllib.request import urlopen
import urllib.error
import twurl
import sqlite3
import json
import ssl

TWITTER_URL =  'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('create table if not exists Twitter (name TEXT, retrieved INTEGER, friends INTEGER)')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('select name from Twitter where retrieved = 0 limit 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)

    cur.execute('update Twitter set retrieved=1 where name = ?', (acct,)) # set chosen name to retrieved

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('select friends from Twitter where name = ? limit 1', (friend,))

        try:
            count = cur.fetchone()[0]
            cur.execute('update Twitter set friends = ? where name = ?', (count+1, friend))
            countold += 1
        except:
            cur.execute('insert into Twitter (name, retrieved, friends) values (?, 0, 1)', (friend,))
            countnew += 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()

cur.close()





