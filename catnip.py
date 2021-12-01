# catnip

from riotwatcher import LolWatcher, ApiError
import pandas as pd

from tinydb import TinyDB, Query

f = open("api.txt", "r")
key = f.read()[:-1]
f.close()
# print(key)

name = 'w1ld23'
lol = LolWatcher("%s" % (key))
region = 'na1'

db = TinyDB(name+'.json')

s = lol.summoner.by_name(region, name)
print(s)

m = lol.match.matchlist_by_puuid(region="americas", puuid=s.get("puuid"))
# print(m)

for mId in m:
#   print(mId);
#   participants = []
    match_detail = lol.match.by_id("americas", mId)
    Match = Query()
    matchId = match_detail.get('metadata').get('matchId')
    if(not db.search(Match.id == matchId)) :
        db.insert({
            'id': matchId,
            'queue': match_detail.get('info').get('queueId')
        })
#   #print(match_detail)
#   for row in match_detail.get('info').get('participants'):
#       #print(row);
#       participants_row = {}
#       participants_row['champion'] = row.get('championId')
#       participants_row['name'] = row.get('summonerName')
#       participants_row['spell1'] = row.get('summoner1Id')
#       participants_row['spell2'] = row.get('summoner2Id')
#       participants_row['win'] = row.get('win')
#       participants_row['kills'] = row.get('kills')
#       participants_row['deaths'] = row.get('deaths')
#       participants_row['assists'] = row.get('assists')
#       participants_row['totalDamageDealt'] = row.get('totalDamageDealt')
#       participants_row['goldEarned'] = row.get('goldEarned')
#       participants_row['champLevel'] = row.get('champLevel')
#       participants_row['totalMinionsKilled'] = row.get('totalMinionsKilled')
#       participants_row['item0'] = row.get('item0')
#       participants_row['item1'] = row.get('item1')
#       participants.append(participants_row)
#   df = pd.DataFrame(participants)
#   #print(df)
