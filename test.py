import cassiopeia
from cassiopeia import Summoner, Champions

cassiopeia.set_riot_api_key("RGAPI-38e12277-90ca-4f48-8e37-fe8de1d4f266")

all_champions = Champions(region="NA")
teemo = all_champions["Teemo"]
a_teemo_game = Summoner(name = "w1ld23", region = "NA").match_history[teemo]
